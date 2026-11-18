#!/usr/bin/env python3
"""Translate CJK taxonomy terms (tags/categories) in EN front matter.

Hugo keeps a separate taxonomy namespace per language, so translated tags on
`index.en.md` only affect the English taxonomy pages; the Chinese site is
untouched. Only top-level `tags:` / `categories:` list items inside YAML front
matter are rewritten — author names, publication titles, abstracts, etc. are
left exactly as-is.

Usage:
    python scripts/migrate_en_taxonomy.py            # dry run (report only)
    python scripts/migrate_en_taxonomy.py --apply    # write changes
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ("publication", "patent", "award", "project", "post", "research")
CJK = re.compile(r"[\u4e00-\u9fff]")
YAML_SPECIAL = re.compile(r"[:#&*!|>'\"%@`{}\[\],]|^[-?]|\s$")

# Controlled vocabulary: Chinese taxonomy term -> English term.
VOCAB: dict[str, str] = {
    "三维重建": "3D Reconstruction",
    "中科院声学所": "Institute of Acoustics, CAS",
    "优秀类": "Excellent",
    "光场": "Light Field",
    "光场分析": "Light Field Analysis",
    "光场处理": "Light Field Processing",
    "光场成像": "Light Field Imaging",
    "光场特征": "Light Field Features",
    "光场特征提取": "Light Field Feature Extraction",
    "光场采集": "Light Field Capture",
    "光流估计": "Optical Flow Estimation",
    "全局运动聚合": "Global Motion Aggregation",
    "创新创业": "Innovation and Entrepreneurship",
    "动作识别": "Action Recognition",
    "图像优化": "Image Optimization",
    "图像处理": "Image Processing",
    "图像安全": "Image Security",
    "图像融合": "Image Fusion",
    "图像超分辨率": "Image Super-Resolution",
    "图卷积": "Graph Convolution",
    "场景识别": "Scene Recognition",
    "声学成像": "Acoustic Imaging",
    "多模态": "Multimodal",
    "多线索融合": "Multi-Cue Fusion",
    "大模型": "Large Models",
    "孪生网络": "Siamese Networks",
    "工程管理": "Engineering Management",
    "广州荣邦科技有限公司": "Guangzhou Rongbang Technology Co Ltd",
    "弱光图像增强": "Low-Light Image Enhancement",
    "弱光增强": "Low-Light Enhancement",
    "技术发明": "Technical Invention",
    "显著性检测": "Saliency Detection",
    "智能体": "Agents",
    "模式识别": "Pattern Recognition",
    "注意力机制": "Attention Mechanism",
    "活动": "Events",
    "深度估计": "Depth Estimation",
    "深度学习": "Deep Learning",
    "点云": "Point Cloud",
    "特征匹配": "Feature Matching",
    "特征描述符": "Feature Descriptors",
    "特征提取": "Feature Extraction",
    "特征表示": "Feature Representation",
    "目标检测": "Object Detection",
    "相关性卷表": "Correlation Volume",
    "相机阵列": "Camera Array",
    "系统标定": "System Calibration",
    "红外图像处理": "Infrared Image Processing",
    "编码成像": "Coded Imaging",
    "缺陷检测": "Defect Detection",
    "臻希企业管理": "Zhenxi Enterprise Management",
    "西北工业大学": "Northwestern Polytechnical University",
    "视觉显著性": "Visual Saliency",
    "计算成像": "Computational Imaging",
    "计算摄影": "Computational Photography",
    "计算机视觉": "Computer Vision",
    "软件开发": "Software Development",
    "通知公告": "Announcements",
    "鉴微": "Jianwei",
    "陕西省2020年度留学人员科技活动择优资助项目（优秀类）": (
        "Shaanxi 2020 Overseas Returnees Science and Technology Activity "
        "Grant (Excellent)"
    ),
    "陕西省自然科学基础研究计划": "Shaanxi Natural Science Basic Research Plan",
}

TAXONOMY_KEYS = {"tags", "categories"}
ITEM_RE = re.compile(r"^(\s*-\s+)(.+?)(\s*)$")
QUOTED_RE = re.compile(r'^"(.*)"$|^\'(.*)\'$')


def unquote(value: str) -> str:
    m = QUOTED_RE.match(value)
    if not m:
        return value
    return m.group(1) if m.group(1) is not None else m.group(2)


def quote_if_needed(value: str, was_quoted: bool) -> str:
    # Preserve quote style if present; otherwise add double quotes only when
    # the English value contains YAML-significant characters.
    if was_quoted:
        return f'"{value}"'
    if YAML_SPECIAL.search(value):
        return f'"{value}"'
    return value


def migrate(path: Path, apply: bool) -> tuple[int, list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return 0, []

    in_front = False
    current_key = ""
    changed = 0
    unmapped: list[str] = []
    out: list[str] = []

    for i, raw in enumerate(lines):
        line = raw.rstrip("\n")
        if i == 0:
            in_front = True
            out.append(raw)
            continue
        if in_front and line.strip() == "---":
            in_front = False
            out.append(raw)
            continue

        if in_front:
            # Top-level key: no leading whitespace, ends with ':'
            key_match = re.match(r"^([A-Za-z_][\w-]*):(\s|$)", line)
            if key_match:
                current_key = key_match.group(1)
                out.append(raw)
                continue

            if current_key in TAXONOMY_KEYS:
                m = ITEM_RE.match(line)
                if m:
                    prefix, value, suffix = m.group(1), m.group(2), m.group(3)
                    was_quoted = bool(QUOTED_RE.match(value))
                    bare = unquote(value)
                    if CJK.search(bare):
                        if bare in VOCAB:
                            new = quote_if_needed(VOCAB[bare], was_quoted)
                            out.append(prefix + new + suffix + ("\n" if raw.endswith("\n") else ""))
                            changed += 1
                        else:
                            unmapped.append(bare)
                            out.append(raw)
                        continue
        out.append(raw)

    if changed and apply:
        path.write_text("".join(out), encoding="utf-8")
    return changed, unmapped


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes")
    args = ap.parse_args()

    total = 0
    all_unmapped: set[str] = set()
    touched = 0
    for sec in SECTIONS:
        for p in sorted((ROOT / "content" / sec).glob("*/index.en.md")):
            n, unmapped = migrate(p, args.apply)
            if n:
                touched += 1
                total += n
                print(f"{'+' if args.apply else '~'} {n:2d}  {p.relative_to(ROOT)}")
            all_unmapped.update(unmapped)

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"\n[{mode}] {total} replacements across {touched} files.")
    if all_unmapped:
        print("UNMAPPED CJK taxonomy values:")
        for v in sorted(all_unmapped):
            print(f"  - {v}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
