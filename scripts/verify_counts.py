#!/usr/bin/env python3
"""一致性校验：README / docs 里写死的数字，必须等于仓库里的实际文件数。

这个仓库是「索引 + 溯源」型资料库，正文里到处是「32 张」「102 张」
「1075 件」这类计数。图片进出一次，这些数字就会同时过期，而人工复查
很容易只改一处、漏掉其余几处（2026-11 就漏过两处）。所以把「数字」当成
可校验的断言，把磁盘当成唯一真相。

校验三类东西：
  1. 计数：README / docs/*.md 中出现的每个计数，等于磁盘同类文件的实际数量
  2. 覆盖：主表 32 行、画廊 102 条，每张图都被文档引用到，且每个引用都指向真实文件
  3. 内部一致：画廊分档授权表、画廊索引的按对象表，分项之和等于总表

用法：
  python scripts/verify_counts.py
退出码：存在不符时为 1，否则为 0。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ("立绘", "插画", "梗图", "设定", "漫画")
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}

problems = []
passed = 0


def images(folder):
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir()
                  if p.is_file() and p.suffix.lower() in IMG_EXT)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def check(label, text, rel, pattern, expected, group=1):
    """断言：rel 中与 pattern 匹配的第一处，其第 group 组等于 expected。"""
    global passed
    m = re.search(pattern, text)
    if not m:
        problems.append(f"{rel}: 没找到「{label}」的表述（磁盘实际 {expected}）")
        return None
    got = int(m.group(group))
    if got == expected:
        passed += 1
    else:
        problems.append(
            f"{rel}:{line_of(text, m.start())} 「{label}」写 {got}，磁盘实际 {expected}")
    return m


def main():
    global passed

    main_imgs = images(ROOT / "原画")
    main_thumbs = images(ROOT / "原画" / "thumbs")
    gallery = {s: images(ROOT / "原画" / "画廊" / s) for s in SECTIONS}
    gallery_total = sum(len(v) for v in gallery.values())

    readme = read("README.md")
    gal_doc = read("docs/画廊.md")
    idx_doc = read("docs/画廊索引.md")

    # ---- 画廊索引：条目数从缩略图墙数出来，未署名的从按对象表加总 ----
    idx_count = len(re.findall(r"<img ", idx_doc))
    idx_unsigned = 0
    rows = re.findall(r"^\| [^|\n]+ \| (\d+) \| (\d+) \|", idx_doc, re.M)
    for unsent, unsigned in rows:
        idx_unsigned += int(unsigned)

    # ---- 1. README 计数 ----
    check("副标题 standing portraits", readme, "README.md",
          r"(\d+) standing portraits", len(main_imgs))
    check("副标题画廊张数", readme, "README.md",
          r"\+ (\d+) more in the gallery", gallery_total)
    check("开头收录对象数", readme, "README.md", r"本仓库收录 (\d+) 个", len(main_imgs))
    check("画廊行张数", readme, "README.md",
          r"(\d+) 张，每张都能点开看原图", gallery_total)
    check("画廊索引行件数", readme, "README.md", r"\| (\d+) 件，点图进原作品页", idx_count)
    check("画廊索引行未署名", readme, "README.md", r"含 (\d+) 件原站未署名的", idx_unsigned)
    check("文档导航画廊索引件数", readme, "README.md",
          r"(?:原站|站内) (\d+) 件[^\n]*缩略图墙", idx_count)
    check("文档导航画廊索引未署名", readme, "README.md",
          r"缩略图墙[^\n]*含 (\d+) 件未署名", idx_unsigned)
    check("快速索引主表张数", readme, "README.md",
          r"\*\*主表收录\*\* \| (\d+) 张白底全身立绘", len(main_imgs))
    check("快速索引变体画廊张数", readme, "README.md",
          r"\*\*变体画廊\*\* \| 另有 (\d+) 张", gallery_total)
    check("目录结构主表张数", readme, "README.md",
          r"原画/\s+(\d+) 张完整立绘原画", len(main_imgs))
    check("目录结构画廊张数", readme, "README.md",
          r"原画/画廊/\s+(\d+) 张画廊图", gallery_total)

    # 文档导航那一行：五区分布 + 合计
    m = re.search(r"立绘 (\d+) / 插画 (\d+) / 梗图 (\d+) / 设定 (\d+) / 漫画 (\d+)，共 (\d+) 张",
                  readme)
    if not m:
        problems.append("README.md: 文档导航里的画廊分区表述缺失")
    else:
        got = [int(x) for x in m.groups()]
        want = [len(gallery[s]) for s in SECTIONS] + [gallery_total]
        if got == want:
            passed += 1
        else:
            problems.append(
                f"README.md:{line_of(readme, m.start())} 文档导航画廊分区写 "
                f"{' / '.join(map(str, got))}，磁盘实际 {' / '.join(map(str, want))}")

    # 目录结构里的五区分项
    for sec in SECTIONS:
        check(f"目录结构 {sec} 张数", readme, "README.md",
              rf"{sec}/\s+(\d+) 张", len(gallery[sec]))

    # ---- 2. docs/画廊.md 计数 ----
    check("画廊总量", gal_doc, "docs/画廊.md", r"目前 \*\*(\d+) 张\*\*", gallery_total)
    for sec in SECTIONS:
        check(f"一眼看全 {sec}", gal_doc, "docs/画廊.md",
              rf"\| \*\*{sec}\*\* \| (\d+) \|", len(gallery[sec]))
    for sec in SECTIONS:
        start = gal_doc.find(f"## {sec}")
        if start < 0:
            problems.append(f"docs/画廊.md: 缺少「## {sec}」小节")
            continue
        body = gal_doc[start:]
        m = re.search(r"共 (\d+) 张", body)
        if not m:
            problems.append(f"docs/画廊.md: 「## {sec}」小节没有写明张数")
        elif int(m.group(1)) != len(gallery[sec]):
            problems.append(
                f"docs/画廊.md:{line_of(gal_doc, start + m.start())} 「## {sec}」写 "
                f"{m.group(1)} 张，磁盘实际 {len(gallery[sec])}")
        else:
            passed += 1

    # 授权分档之和 = 画廊总数
    auth_start = gal_doc.find("## 授权")
    if auth_start < 0:
        problems.append("docs/画廊.md: 缺少「## 授权」小节")
    else:
        tiers = re.findall(r"^\| [^|\n]+ \| (\d+) \|", gal_doc[auth_start:], re.M)
        total_tiers = sum(int(t) for t in tiers)
        if total_tiers == gallery_total:
            passed += 1
        else:
            problems.append(
                f"docs/画廊.md: 授权分档合计 {total_tiers} 张，与画廊实际 {gallery_total} 张不符")

    # ---- 3. docs/画廊索引.md 计数 ----
    check("索引页画廊张数", idx_doc, "docs/画廊索引.md",
          r"画廊里收了 (\d+) 张", gallery_total)
    check("索引页未收件数", idx_doc, "docs/画廊索引.md",
          r"另有 \*\*(\d+) 件没进画廊\*\*", idx_count)
    check("索引页无署名件数", idx_doc, "docs/画廊索引.md",
          r"(\d+) 件的作品页写着", idx_unsigned)

    # ---- 4. 覆盖：主表与画廊的每张图都被文档引用 ----
    disk_main = {p.stem.removesuffix("-ref") for p in main_imgs}
    doc_main = set(re.findall(r"原画/([\w\-]+?)-ref\.jpg", readme))
    for miss in sorted(disk_main - doc_main):
        problems.append(f"README.md: 主表漏收原画/{miss}-ref.jpg")
    for extra in sorted(doc_main - disk_main):
        problems.append(f"README.md: 表格引用了不存在的原画/{extra}-ref.jpg")
    for p in main_imgs:
        if not (ROOT / "原画" / "thumbs" / f"{p.stem.removesuffix('-ref')}.jpg").exists():
            problems.append(f"原画/thumbs/: 缺少 {p.stem} 的缩略图")

    doc_gal = set(re.findall(
        r"原画/画廊/(立绘|插画|梗图|设定|漫画)/thumbs/([\w\-]+)\.jpg", gal_doc))
    disk_gal = {(s, p.stem) for s in SECTIONS for p in gallery[s]}
    for sec, stem in sorted(disk_gal - doc_gal):
        problems.append(f"docs/画廊.md: 漏收 原画/画廊/{sec}/{stem}.jpg")
    for sec, stem in sorted(doc_gal - disk_gal):
        problems.append(f"docs/画廊.md: 引用了不存在的 原画/画廊/{sec}/{stem}.jpg")
    for sec in SECTIONS:
        for p in gallery[sec]:
            if not (ROOT / "原画" / "画廊" / sec / "thumbs" / f"{p.stem}.jpg").exists():
                problems.append(f"原画/画廊/{sec}/thumbs/: 缺少 {p.stem} 的缩略图")

    # ---- 5. 来源与版权.md：逐图来源表自身的一致性 ----
    prov = read("docs/来源与版权.md")
    # 三之三 是画廊 102 张的逐图总表；三之五 会把其中 8 张再列一遍细节，不能重复计
    gal_zone = prov[prov.find("## 三之三"):prov.find("## 三之四")]
    prov_rows = [ln for ln in gal_zone.splitlines() if ln.startswith("| `画廊/")]
    if len(prov_rows) == gallery_total:
        passed += 1
    else:
        problems.append(
            f"docs/来源与版权.md: 画廊逐图来源表 {len(prov_rows)} 行，画廊实际 {gallery_total} 张")

    # 授权分布：逐图表的授权列加总 = docs/画廊.md 的七档表
    tier_counts = {}
    host_counts = {}
    HOST_MAP = (
        ("www.bilibili.com", "画师 B 站动态"),
        ("xn--pssy23gqgbz2d718b.com", "站点原图仓"),
        ("raw.githubusercontent.com", "GitHub 开源项目"),
        ("fisharchive.cc", "蓝色大肥鱼档案馆"),
    )
    authors, objects = set(), set()
    for ln in prov_rows:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 8:
            problems.append(f"docs/来源与版权.md: 表格列数不足 —— {cells[0]}")
            continue
        tier = cells[5].replace("*", "").strip()
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
        authors.add(cells[4])
        objects.add(cells[3])
        url = re.search(r"\]\((https?://[^)]+)\)", cells[7])
        host = (re.match(r"https?://([^/]+)", url.group(1)).group(1)
                if url else "")
        for known, bucket in HOST_MAP:
            if host == known:
                host_counts[bucket] = host_counts.get(bucket, 0) + 1
                break
        else:
            problems.append(f"docs/来源与版权.md: {cells[0]} 的出处域名未归类（{host or '无链接'}）")

    doc_tiers = {}
    if auth_start >= 0:
        for name, count in re.findall(r"^\| ([^|\n]+) \| (\d+) \|", gal_doc[auth_start:], re.M):
            doc_tiers[name.strip()] = int(count)
    if tier_counts == doc_tiers:
        passed += 1
    else:
        problems.append(
            "docs/来源与版权.md 逐图授权分布与 docs/画廊.md 七档表不符："
            f"逐图 {tier_counts} · 七档表 {doc_tiers}")

    check("画廊作者数", gal_doc, "docs/画廊.md",
          r"来自 \*\*(\d+) 位作者\*\*", len(authors))
    check("画廊覆盖对象数", gal_doc, "docs/画廊.md",
          r"覆盖 \*\*(\d+) 个对象\*\*", len(objects))

    # 四路来源的分布：域名统计 vs 正文写死的张数
    for label, pattern in (
            ("画师 B 站动态", r"画师 B 站动态 (\d+) 张"),
            ("站点原图仓", r"站点原图仓 (\d+) 张"),
            ("GitHub 开源项目", r"GitHub 开源项目 (\d+) 张"),
            ("蓝色大肥鱼档案馆", r"蓝色大肥鱼档案馆 (\d+) 张")):
        check(f"画廊来源·{label}", prov, "docs/来源与版权.md",
              pattern, host_counts.get(label, 0))
    if sum(host_counts.values()) != gallery_total:
        problems.append(
            f"docs/来源与版权.md: 四路来源合计 {sum(host_counts.values())} 张，"
            f"画廊实际 {gallery_total} 张")

    # 档案馆分批表之和 = 6.3 标题声明的张数
    batch_sec = prov[prov.find("### 6.3"):]
    batches = re.findall(r"^\| \**[^|\n]+\** \| \**\d{2}-\d{2}\** \| [^|\n]+ \| \**(\d+)\** \|",
                         batch_sec, re.M)
    declared = re.search(r"### 6\.3 收了 (\d+) 张", prov)
    if declared and batches:
        if int(declared.group(1)) == sum(int(b) for b in batches):
            passed += 1
        else:
            problems.append(
                f"docs/来源与版权.md: 6.3 标题写 {declared.group(1)} 张，"
                f"分批表实际加总 {sum(int(b) for b in batches)} 张")

    # 主表 32 张：每一张都要在逐图来源里出现（四、其他角色 收的是仓库外的 7 件，排除）
    other_zone = prov[prov.find("## 四、"):prov.find("## 五、")]
    main_zone = prov.replace(other_zone, "")
    prov_main = set(re.findall(r"`([\w\-]+)-ref\.jpg`", main_zone))
    for miss in sorted(disk_main - prov_main):
        problems.append(f"docs/来源与版权.md: 主表 {miss}-ref.jpg 没有逐图来源记录")

    # ---- 汇总 ----
    print(f"磁盘实际：主表 {len(main_imgs)} 张（缩略图 {len(main_thumbs)}）· "
          f"画廊 {gallery_total} 张 · 索引墙 {idx_count} 件（未署名 {idx_unsigned}）")
    if problems:
        print(f"\n[不符] 通过 {passed} 项 · 不符 {len(problems)} 项")
        for item in problems:
            print(f"  - {item}")
        return 1
    print(f"\n[通过] {passed} 项断言全部一致")
    return 0


if __name__ == "__main__":
    sys.exit(main())
