#!/usr/bin/env python3
"""重建 docs/画廊索引.md：站点全量 works 快照 − 画廊已收 ＝ 索引墙。

数据源：站点源码仓库的 data/works.json（默认现下现用，可加 --works 指定本地快照）。
画廊已收：解析 docs/来源与版权.md「三之三」逐图总表里站内作品页链接的 slug。
死亡登记：scripts/dead-links.txt 里的 /works/<slug>.html保留条目只在标题后标注。

用法
  python scripts/build_gallery_index.py --works _maint/works.json
  python scripts/build_gallery_index.py --works _maint/works.json --check   # 只比对不写盘
"""

import argparse
import html
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://xn--pssy23gqgbz2d718b.com"
WORKS_URL = ("https://raw.githubusercontent.com/lmy414/bluedafeiyu"
             "/main/data/works.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

CHAR_NAMES = {
    "deepseek": "DeepSeek", "gpt": "GPT", "gemini": "Gemini", "claude": "Claude",
    "kimi": "Kimi", "other": "其他角色", "qwen": "Qwen", "doubao": "豆包",
    "glm": "GLM", "grok": "Grok", "git": "Git", "mistral": "Mistral",
    "minimax": "MiniMax", "stepfun": "阶跃星辰", "mimo": "MiMo", "opencode": "OpenCode",
    "huggingface": "Hugging Face", "zcode": "ZCode", "rwkv": "RWKV",
    "perplexity": "Perplexity", "hunyuan": "混元", "novelai": "NovelAI", "llama": "Llama",
}
TYPE_NAMES = {"standing": "立绘", "illustration": "插画", "meme": "梗图",
              "setting": "设定", "comic": "漫画", "other": "其他"}
TYPE_ORDER = ["standing", "illustration", "meme", "setting", "comic", "other"]
PER_ROW = 8


def load_works(path):
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    req = urllib.request.Request(WORKS_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def collected_site_slugs():
    """画廊已收里出自本站的 slug集合（三之三逐图总表，host 为本站的作品页链接）。"""
    prov = (ROOT / "docs" / "来源与版权.md").read_text(encoding="utf-8")
    sec = prov[prov.find("## 三之三"):prov.find("## 三之四")]
    out = set()
    for ln in sec.splitlines():
        if not ln.startswith("| `画廊/"):
            continue
        m = re.search(r"\]\((https?://[^)]+)\)", ln)
        if not m or urllib.request.urlsplit(m.group(1)).hostname != urllib.request.urlsplit(SITE).hostname:
            continue
        s = re.search(r"/works/([A-Za-z0-9_\-]+)\.html", m.group(1))
        if s:
            out.add(s.group(1))
    return out


def dead_slugs():
    reg = ROOT / "scripts" / "dead-links.txt"
    if not reg.exists():
        return set()
    out = set()
    for ln in reg.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        m = re.search(r"/works/([A-Za-z0-9_\-]+)\.html", ln.split("#")[0])
        if m:
            out.add(m.group(1))
    return out


def unsigned(work):
    return not ((work.get("origin") or {}).get("author") or "").strip()


def esc(s):
    return html.escape(s or "", quote=True)


def build(works, collected, dead, date):
    wall = [w for w in works if w.get("slug") and w["slug"] not in collected]
    wall.sort(key=lambda w: w["slug"])
    total = len(wall)
    n_unsigned = sum(1 for w in wall if unsigned(w))

    by_char = {}
    for w in wall:
        by_char.setdefault(w.get("characterId") or "other", []).append(w)
    order = sorted(by_char, key=lambda c: (-len(by_char[c]),
                                           min(w["slug"] for w in by_char[c])))

    type_total = Counter()
    for w in wall:
        type_total[(w.get("categoryIds") or ["other"])[0]] += 1

    L = []
    L.append("# 画廊索引")
    L.append("")
    L.append(f"画廊里收了 102 张，原站另有 **{total} 件没进画廊**。"
             f"这 {total} 件不是被漏掉了是**没法合规收**——"
             f"其中 **{n_unsigned} 件的作品页写着「原作者未标注」**，原站自己也不知道作者是谁。")
    L.append("")
    L.append("**转载一张查不到作者的作品，等于替它把署名义务永久丢掉。** 所以这一页只做索引：")
    L.append("")
    L.append("- 缩略图用**原站的预览图外链**，图仍然在原作者与站方的服务器上，本仓库不下载、不转发、不再分发")
    L.append("- 点任意一张都跳到原作品页，署名、授权、来源信息都在那边")
    L.append("")
    L.append("换句话说：**这里是一个导览图不是第二个仓库。**")
    L.append("")
    if dead & {w["slug"] for w in wall}:
        n_dead = len(dead & {w["slug"] for w in wall})
        L.append(f"> **原站会删图。** 索引墙里有 {n_dead} 件的原作品页已被站点删除"
                 f"（{date} 复核，标题标注「原作品页已下线」），"
                 f"链接登记在 `scripts/dead-links.txt`，外链体检会跳过它们；"
                 f"哪天恢复了，体检会提示把登记撤掉。")
        L.append("")
    L.append("## 怎么用这一页")
    L.append("")
    L.append("| 想做什么 | 怎么做 |")
    L.append("| --- | --- |")
    L.append("| 找某个角色的所有图 | 按下面的「按对象」跳，或直接用浏览器的页内搜索（Ctrl+F）搜角色名 |")
    L.append("| 找特定类型 | 按「按类型」跳：立绘 / 插画 / 梗图 / 设定 / 漫画 |")
    L.append("| 找到喜欢的图想收藏 | 点图进原作品页，那里能下载原图也能看到授权 |")
    L.append("| 想把它收进本仓库 | 先确认作者——查到作者后可提 issue我们按画廊规格收录 |")
    L.append("")
    L.append("## 按对象")
    L.append("")
    L.append("| 对象 | 未收件数 | 其中无署名 | 跳转 |")
    L.append("| --- | --- | --- | --- |")
    for c in order:
        name = CHAR_NAMES.get(c, c)
        members = by_char[c]
        u = sum(1 for w in members if unsigned(w))
        L.append(f"| **{name}** | {len(members)} | {u} | "
                 f"[看{name}的 {len(members)} 张](#{name}) |")
    L.append("")
    L.append("## 按类型")
    L.append("")
    L.append("| 类型 | 件数 |")
    L.append("| --- | --- |")
    for t in TYPE_ORDER:
        L.append(f"| {TYPE_NAMES[t]} | {type_total.get(t, 0)} |")
    L.append("")

    for c in order:
        name = CHAR_NAMES.get(c, c)
        members = by_char[c]
        u = sum(1 for w in members if unsigned(w))
        L.append(f"## {name}")
        L.append("")
        L.append(f"{len(members)} 件未收其中 {u} 件原站未署名。"
                 f"缩略图为原站预览图外链，点任意一张进原作品页。")
        L.append("")
        by_type = {}
        for w in members:
            by_type.setdefault((w.get("categoryIds") or ["other"])[0], []).append(w)
        present = [t for t in TYPE_ORDER if t in by_type]
        L.append("| 类型 | 件数 | 跳转 |")
        L.append("| --- | --- | --- |")
        for t in present:
            L.append(f"| {TYPE_NAMES[t]} | {len(by_type[t])} | "
                     f"[跳到{TYPE_NAMES[t]}](#{name}-{TYPE_NAMES[t]}) |")
        L.append("")
        for t in present:
            L.append(f"### {name} · {TYPE_NAMES[t]}")
            L.append("")
            rows = by_type[t]
            for i in range(0, len(rows), PER_ROW):
                L.append("<table><tr>")
                for w in rows[i:i + PER_ROW]:
                    author = (w.get("origin") or {}).get("author") or "未署名"
                    title = f"{w.get('name') or w['slug']} · {author}"
                    if w["slug"] in dead:
                        title += " · 原作品页已下线"
                    L.append(
                        f'<td align="center" width="12%">'
                        f'<a href="{SITE}/works/{w["slug"]}.html" title="{esc(title)}">'
                        f'<img src="{SITE}/{w.get("thumbnailPath") or ""}" width="90">'
                        f"</a></td>")
                L.append("</tr></table>")
                L.append("")
            L[-1] = L[-1]  # 保持每表后一个空行，由下一节头的空行自然形成
            # 去掉表与下节头之间的多余空行：下一节头前只留一个空行在下方逻辑处理
        # 节之间两个空行：上面每表后已有一个空行再补一个
        L.append("")

    # 末尾：去掉多余空行接页脚
    while L and L[-1] == "":
        L.pop()
    L.append("")
    L.append("---")
    L.append("")
    L.append("回到 [README](../README.md)｜[画廊](画廊.md)｜"
             "[来源与版权](来源与版权.md)｜[素材来源导航](素材来源导航.md)")
    return "\n".join(L) + "\n", total, n_unsigned


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--works", help="本地 works.json 快照路径（默认从站点仓库现下）")
    ap.add_argument("--check", action="store_true", help="只比对不写盘")
    ap.add_argument("--date", default="", help="复核日期YYYY-MM-DD（默认今天）")
    args = ap.parse_args()
    from datetime import date as d
    today = args.date or d.today().isoformat()

    works = load_works(args.works)
    collected = collected_site_slugs()
    dead = dead_slugs()
    text, total, n_unsigned = build(works, collected, dead, today)
    target = ROOT / "docs" / "画廊索引.md"

    if args.check:
        cur = target.read_text(encoding="utf-8")
        if cur == text:
            print(f"[通过] 索引墙与快照一致（{total} 件，未署名 {n_unsigned}）")
            return 0
        print(f"[偏差] 索引墙与快照不一致（快照应为 {total} 件，未署名 {n_unsigned}）")
        return 1

    target.write_text(text, encoding="utf-8", newline="")
    print(f"已重建 docs/画廊索引.md：{total} 件（未署名 {n_unsigned}），"
          f"站点快照 {len(works)} 件，画廊已收排除 {len(collected)} 件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
