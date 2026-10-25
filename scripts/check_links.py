#!/usr/bin/env python3
"""外链体检：校验 README 与 docs/ 中出现的全部 http(s) 链接。

判定规则
  200 / 3xx  → 正常
  401 / 403  → 反爬或需登录，浏览器通常可访问，记入「待人工确认」而非失效
  429        → 触发限流，同样记入「待人工确认」
  404 / 410  → 真失效
  其余异常    → 网络抖动，记入「待人工确认」

用法：
  python scripts/check_links.py                # 输出到 stdout
  python scripts/check_links.py --output r.md  # 同时写入 Markdown 报告
退出码：存在真失效链接时为 1，否则为 0。
"""

import argparse
import concurrent.futures as futures
import glob
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
TIMEOUT = 20
# 文档里出现的、指向仓库自身或明显非资源页的链接，不做校验
SKIP_PREFIX = (
    "https://github.com/saya-ch/model-muses",
    "https://github.com/saya-ch/",
    "mailto:",
)

URL_RE = re.compile(r"https?://[^\s)\"'`<>｜（）〔〕【】]+")


def collect_urls():
    urls = {}
    targets = [os.path.join(ROOT, "README.md")] + sorted(
        glob.glob(os.path.join(ROOT, "docs", "*.md")))
    for path in targets:
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        with open(path, encoding="utf-8") as fh:
            for raw in URL_RE.findall(fh.read()):
                url = raw.rstrip(".,;>/)]}\u3002\uff0c\uff09\u3011\u3015`")
                if not url or url.startswith(SKIP_PREFIX):
                    continue
                # 含占位符的模板链接（如 <role>/<hash>），不是可访问的真实地址
                if any(ch in url for ch in "<>{}"):
                    continue
                # raw 只服务文件，目录型路径必然 404，属说明性引用
                if "raw.githubusercontent.com" in url and url.endswith("/originals"):
                    continue
                urls.setdefault(url, set()).add(rel)
    return urls


def probe(url, attempts=3):
    """HTTP 状态码是确定结论，直接返回；仅网络异常才重试。"""
    last = "未知异常"
    for attempt in range(attempts):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return url, resp.status, ""
        except urllib.error.HTTPError as exc:
            return url, exc.code, ""
        except Exception as exc:  # 网络异常、超时、DNS
            last = type(exc).__name__
            if attempt < attempts - 1:
                time.sleep(1.5 * (attempt + 1))
    return url, None, last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", help="Markdown 报告输出路径")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    urls = collect_urls()
    if not urls:
        print("未收集到任何链接")
        return 0

    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(probe, sorted(urls)))

    dead, uncertain, ok = [], [], 0
    for url, status, err in results:
        if status == 200 or (status and 300 <= status < 400):
            ok += 1
        elif status in (401, 403, 429):
            uncertain.append((url, status))
        elif status in (404, 410):
            dead.append((url, status))
        else:
            uncertain.append((url, err or "未知异常"))

    print(f"共 {len(urls)} 条链接：正常 {ok} · 失效 {len(dead)} · 待人工确认 {len(uncertain)}")
    if dead:
        print("\n[失效]")
        for url, code in dead:
            print(f"  {code}  {url}")
    if uncertain:
        print("\n[待人工确认]")
        for url, code in uncertain:
            print(f"  {code}  {url}")

    if args.output:
        lines = [
            "## 外链体检报告",
            "",
            f"自动检测 **{len(urls)}** 条链接：正常 {ok} · 失效 {len(dead)} · 待人工确认 {len(uncertain)}。",
            "",
        ]
        if dead:
            lines += ["### 失效链接", "", "| 状态 | 链接 | 出现位置 |", "| --- | --- | --- |"]
            for url, code in dead:
                where = "、".join(sorted(urls[url]))
                lines.append(f"| {code} | <{url}> | {where} |")
            lines.append("")
        if uncertain:
            lines += ["### 待人工确认（多为反爬或网络抖动）", ""]
            for url, code in uncertain:
                lines.append(f"- `{code}` <{url}>")
            lines.append("")
        with open(args.output, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines))

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
