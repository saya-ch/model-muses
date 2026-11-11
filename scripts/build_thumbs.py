#!/usr/bin/env python3
"""缩略图构建与体检：按文档声明的规格重新生成 thumbs，并校验是否已经一致。

规格（与 README「目录结构」一节一致）
  原画/thumbs/<name>.jpg        等比缩放进 220×320 的框，不放大，JPEG q90
  原画/画廊/<区>/thumbs/<x>.jpg 等比缩放，长边 320，不放大，JPEG q90

为什么画廊用 320 而不是 260：docs/画廊.md 里插画／梗图／设定／漫画四区的图按
width="240" 显示，竖版原图长边缩到 260 时宽度只有约 146px，被浏览器拉伸到 240
就是糊的；长边 320 时竖版宽约 240，正好一比一。

历史遗留：主表缩略图是两批脚本生成的——一批只卡宽 220（高到 394），一批只卡
高 320（宽 178～180），同一张原图会得出两种尺寸。这个脚本把两套规则收敛成一套。

用法
  python scripts/build_thumbs.py            # 体检，只报告差异，退出码 1 表示有偏差
  python scripts/build_thumbs.py --write    # 按规格重写全部缩略图
  python scripts/build_thumbs.py --write --only 画廊/立绘
"""

import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # 没装 Pillow 时只做「有没有」的检查，不判尺寸
    Image = None

ROOT = Path(__file__).resolve().parent.parent
MAIN_BOX = (220, 320)
GALLERY_LONG_EDGE = 320
QUALITY = 90
SECTIONS = ("立绘", "插画", "梗图", "设定", "漫画")
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp"}

problems = []
rebuilt = 0
skipped = 0


def fit_box(size, box):
    """等比缩放进框内，不放大。"""
    w, h = size
    scale = min(box[0] / w, box[1] / h)
    if scale >= 1:
        return (w, h)
    return (max(1, round(w * scale)), max(1, round(h * scale)))


def fit_long_edge(size, edge):
    """等比缩放使长边等于 edge，不放大。"""
    w, h = size
    if max(w, h) <= edge:
        return (w, h)
    factor = edge / max(w, h)
    return (max(1, round(w * factor)), max(1, round(h * factor)))


def target_for(src, is_main):
    if Image is None:
        return None
    with Image.open(src) as im:
        return fit_box(im.size, MAIN_BOX) if is_main else fit_long_edge(
            im.size, GALLERY_LONG_EDGE)


def write_thumb(src, dst, target):
    global rebuilt, skipped
    if dst.exists() and Image is not None:
        with Image.open(dst) as im:
            if im.size == target:
                skipped += 1
                return
    with Image.open(src) as im:
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        dst.parent.mkdir(parents=True, exist_ok=True)
        im.resize(target, Image.LANCZOS).save(dst, "JPEG", quality=QUALITY,
                                              optimize=True, progressive=True)
    rebuilt += 1


def check_thumb(src, dst, rel, is_main):
    if not dst.exists():
        problems.append(f"{rel}: 缩略图缺失")
        return
    if Image is None:
        return
    want = target_for(src, is_main)
    with Image.open(dst) as im:
        got = im.size
    if got != want:
        problems.append(f"{rel}: 实际 {got[0]}×{got[1]}，规格应 {want[0]}×{want[1]}")


def jobs(only=None):
    out = []
    for src in sorted((ROOT / "原画").glob("*.jpg")):
        rel = f"原画/thumbs/{src.stem.removesuffix('-ref')}.jpg"
        out.append((src, ROOT / rel, rel, True))
    for sec in SECTIONS:
        folder = ROOT / "原画" / "画廊" / sec
        for src in sorted(p for p in folder.iterdir()
                          if p.is_file() and p.suffix.lower() in IMG_EXT):
            rel = f"原画/画廊/{sec}/thumbs/{src.stem}.jpg"
            out.append((src, ROOT / rel, rel, False))
    if only:
        out = [j for j in out if j[2].startswith(f"原画/{only}")]
    return out


def orphans():
    main_thumbs = ROOT / "原画" / "thumbs"
    if main_thumbs.is_dir():
        for thumb in sorted(main_thumbs.glob("*.jpg")):
            if not (ROOT / "原画" / f"{thumb.stem}-ref.jpg").exists():
                problems.append(f"原画/thumbs/{thumb.name}: 找不到对应原图")
    for sec in SECTIONS:
        thumbs = ROOT / "原画" / "画廊" / sec / "thumbs"
        if not thumbs.is_dir():
            continue
        for thumb in sorted(thumbs.glob("*.jpg")):
            if not (ROOT / "原画" / "画廊" / sec / f"{thumb.stem}.jpg").exists():
                problems.append(f"原画/画廊/{sec}/thumbs/{thumb.name}: 找不到对应原图")


def check_main_specs():
    """主表的收图标准：白底、竖版、单人、全身。这里能机检前两条。"""
    if Image is None:
        return
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    line = next((ln for ln in readme.splitlines() if "分辨率" in ln), "")
    declared = {(int(w), int(h)) for w, h in re.findall(r"(\d+)[×x](\d+)", line)}
    actual = set()
    for src in sorted((ROOT / "原画").glob("*.jpg")):
        with Image.open(src) as im:
            actual.add(im.size)
            if im.height <= im.width:
                problems.append(f"原画/{src.name}: {im.size[0]}×{im.size[1]} 不是竖版，违反主表收图标准")
            px = im.convert("RGB")
            w, h = px.size
            for xy in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)):
                if min(px.getpixel(xy)) < 245:
                    problems.append(f"原画/{src.name}: {xy} 不是白底（{px.getpixel(xy)}），违反主表收图标准")
                    break
    if declared and declared != actual:
        for size in sorted(actual - declared):
            problems.append(f"README.md: 分辨率清单漏了 {size[0]}×{size[1]}")
        for size in sorted(declared - actual):
            problems.append(f"README.md: 分辨率清单多了 {size[0]}×{size[1]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="按规格重写缩略图")
    ap.add_argument("--only", help="只处理某个子目录，如 画廊/立绘")
    args = ap.parse_args()

    if Image is None:
        print("[注意] 未安装 Pillow：只检查缩略图是否存在，不校验尺寸（pip install pillow)")

    todo = jobs(args.only)
    for src, dst, rel, is_main in todo:
        if args.write:
            write_thumb(src, dst, target_for(src, is_main))
        else:
            check_thumb(src, dst, rel, is_main)
    orphans()
    if not args.only:
        check_main_specs()

    if args.write:
        print(f"重写 {rebuilt} 张，已在规格内跳过 {skipped} 张")
    if problems:
        print(f"[偏差] {len(problems)} 项")
        for item in problems:
            print(f"  - {item}")
        return 1
    print(f"[通过] {len(todo)} 张缩略图均在规格内")
    return 0


if __name__ == "__main__":
    sys.exit(main())
