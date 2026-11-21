#!/usr/bin/env python3
"""抓 GitHub traffic API（views / clones / referrers / paths，只保留 14 天）
并存成单日 JSON，供 workflow 提交到 `traffic` 分支。

用法（CI 内由 workflow 调用）
  GITHUB_TOKEN=... GITHUB_REPOSITORY=saya-ch/model-muses \
    python scripts/traffic_snapshot.py --out snapshots/2026-11-21.json

本地手动跑也可以（token 要有该仓库的 push 权限）。
"""

import argparse
import json
import os
import sys
import urllib.request

API = "https://api.github.com"


def get(path, token, repo):
    req = urllib.request.Request(
        f"{API}/repos/{repo}/traffic/{path}",
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json",
                 "User-Agent": "model-muses-traffic-snapshot"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--date", default="")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("需要 GITHUB_TOKEN 和 GITHUB_REPOSITORY 环境变量", file=sys.stderr)
        return 1
    if not args.date:
        from datetime import date
        args.date = date.today().isoformat()

    snap = {"date": args.date, "repo": repo}
    for key in ("views", "clones", "popular/referrers", "popular/paths"):
        try:
            snap[key.replace("/", "_")] = get(key, token, repo)
        except Exception as exc:  # noqa: BLE001 - 快照缺一项比全失败好
            snap[key.replace("/", "_")] = {"error": f"{type(exc).__name__}: {exc}"}

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"已写入 {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
