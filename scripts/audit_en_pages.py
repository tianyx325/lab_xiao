#!/usr/bin/env python3
"""Full EN page audit — structure, UI chrome, content gaps."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
CONTENT = ROOT / "content"

CJK = re.compile(r"[\u4e00-\u9fff]")

FORBIDDEN_UI = [
    "跳到正文",
    "搜索论文",
    "搜索项目",
    "搜索专利",
    "搜索奖项",
    "搜索新闻",
    "没有匹配的内容",
    "上一页",
    "下一页",
    "列表分页",
    "联系与招生",
    "招生信息",
    "友情链接",
    "回到顶部",
    "查看更多",
    "按分组筛选",
    "个人简介",
    "项目主页",
    "返回成员列表",
    "正在前往学术成果",
]


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def mostly_cjk(s: str) -> bool:
    if not s:
        return False
    compact = re.sub(r"\s+", "", s)
    cjk = len(CJK.findall(s))
    return cjk >= 2 and cjk / max(len(compact), 1) > 0.35


def count(html: str, pat: str) -> int:
    return len(re.findall(pat, html))


def panel_chunk(html: str, pid: str) -> str:
    # non-greedy until next panel or footer-ish
    m = re.search(
        rf'id="{pid}"[\s\S]*?(?=(?:id="lab-hub-panel-)|(?:<button type=button class="?lab-top-btn)|(?:</div></div><footer)|(?:</main>))',
        html,
    )
    if m:
        return m.group(0)
    m = re.search(rf"id={pid}[\s\S]*?(?=(?:id=lab-hub-panel-)|(?:lab-top-btn)|(?:<footer))", html)
    return m.group(0) if m else ""


def main() -> int:
    issues: list[tuple[str, str]] = []
    lines: list[str] = []

    # --- publications hub deep compare ---
    lines.append("=== Publications hub ===")
    for lang, p in [("ZH", PUBLIC / "publications/index.html"), ("EN", PUBLIC / "en/publications/index.html")]:
        t = read(p)
        lines.append(f"{lang}: list-item={count(t,'lab-list-item')} card-title={count(t,'lab-card-title')} row-title={count(t,'lab-row-title')} year-head={count(t,'lab-year-head')}")
        for pid in ("lab-hub-panel-pub", "lab-hub-panel-pat", "lab-hub-panel-award"):
            c = panel_chunk(t, pid)
            lines.append(
                f"  {pid}: list={count(c,'lab-list-item')} card={count(c,'lab-card-title')} row={count(c,'lab-row-title')} len={len(c)}"
            )

    zh_pub, en_pub = read(PUBLIC / "publications/index.html"), read(PUBLIC / "en/publications/index.html")
    for pid, label in [
        ("lab-hub-panel-pub", "papers"),
        ("lab-hub-panel-pat", "patents"),
        ("lab-hub-panel-award", "awards"),
    ]:
        zc = count(panel_chunk(zh_pub, pid), "lab-list-item")
        ec = count(panel_chunk(en_pub, pid), "lab-list-item")
        if zc != ec:
            issues.append(("publications", f"{label} list-item ZH={zc} EN={ec}"))

    # --- section landings ---
    lines.append("\n=== Section landings ===")
    sections = [
        ("", "home", [("member-cards", "lab-member-card-name"), ("card-titles", "lab-card-title")]),
        ("people", "people", [("member-cards", "lab-member-card-name")]),
        ("research", "research", [("card-titles", "lab-card-title")]),
        ("project", "project", [("list-items", "lab-list-item"), ("filters", "lab-list-filters")]),
        ("post", "post", [("list-items", "lab-list-item")]),
        ("contact", "contact", [("admit-cols", "lab-contact-admit-col")]),
    ]
    for rel, name, mets in sections:
        zh_p = PUBLIC / "index.html" if not rel else PUBLIC / rel / "index.html"
        en_p = PUBLIC / "en/index.html" if not rel else PUBLIC / "en" / rel / "index.html"
        zh, en = read(zh_p), read(en_p)
        if not en:
            issues.append((name, "EN HTML missing"))
            continue
        bits = []
        for label, pat in mets:
            zc, ec = count(zh, pat), count(en, pat)
            bits.append(f"{label}={zc}/{ec}")
            if zc != ec:
                issues.append((name, f"{label} ZH={zc} EN={ec}"))
        forbid = [s for s in FORBIDDEN_UI if s in en]
        if forbid:
            issues.append((name, f"ZH UI: {forbid}"))
        # brand
        if re.search(r"lab-navbar-brand[\s\S]{0,160}智能感知", en):
            issues.append((name, "navbar brand Chinese"))
        lines.append(f"/en/{rel or ''}: {', '.join(bits)}; forbid={forbid or 'ok'}")

    # home heads
    zh_h = re.findall(r"section-head[\s\S]{0,80}?<h2>([^<]+)", read(PUBLIC / "index.html"))
    en_h = re.findall(r"section-head[\s\S]{0,80}?<h2>([^<]+)", read(PUBLIC / "en/index.html"))
    lines.append(f"home heads ZH={zh_h} EN={en_h}")
    if len(zh_h) != len(en_h):
        issues.append(("home", f"section heads ZH={zh_h} EN={en_h}"))

    # --- all EN HTML: UI chrome + CJK titles (exclude tag/category taxonomies for title severity) ---
    lines.append("\n=== Full EN HTML sweep ===")
    en_pages = sorted((PUBLIC / "en").rglob("index.html"))
    ui_hits: dict[str, list[str]] = defaultdict(list)
    brand_hits = []
    cjk_main = []
    cjk_tax = []
    empty_main = []
    for p in en_pages:
        html = read(p)
        rel = str(p.relative_to(PUBLIC / "en")).replace("\\", "/")
        is_tax = rel.startswith("tag/") or rel.startswith("category/") or rel.startswith("publication_types/")
        if re.search(r"lab-navbar-brand[\s\S]{0,160}智能感知", html):
            brand_hits.append(rel)
        for s in FORBIDDEN_UI:
            if s in html:
                ui_hits[s].append(rel)
        # page h1
        h1 = re.findall(r"<h1[^>]*>([^<]+)</h1>", html)
        for h in h1:
            if mostly_cjk(h):
                (cjk_tax if is_tax else cjk_main).append((rel, h))
        # empty people-like: list body with no cards/items on content sections
        if not is_tax and rel.count("/") == 1 and rel.endswith("/index.html"):
            # section landing already checked
            pass

    lines.append(f"EN pages: {len(en_pages)}")
    lines.append(f"Chinese brand: {len(brand_hits)}")
    if brand_hits:
        issues.append(("brand", f"{len(brand_hits)} pages"))
    lines.append("UI chrome leaks:")
    if not ui_hits:
        lines.append("  (none)")
    for s, pages in sorted(ui_hits.items(), key=lambda x: -len(x[1])):
        lines.append(f"  {s}: {len(pages)} e.g. {pages[0]}")
        issues.append(("ui", f"{s} ×{len(pages)}"))

    lines.append(f"CJK h1 on main pages: {len(cjk_main)}")
    for rel, h in cjk_main[:20]:
        lines.append(f"  {rel}: {h}")
        issues.append(("cjk-h1", f"{rel}: {h}"))
    lines.append(f"CJK h1 on taxonomy pages: {len(cjk_tax)}")
    if cjk_tax:
        issues.append(("taxonomy", f"{len(cjk_tax)} tag/category pages still Chinese titles"))
        lines.append(f"  sample: {cjk_tax[:5]}")

    # --- detail page UI labels (i18n keys as English words) ---
    lines.append("\n=== Detail chrome samples ===")
    detail_checks = [
        ("publication", "en/publication", ["Authors", "Year", "Abstract", "Keywords", "作者", "摘要", "关键词"]),
        ("project", "en/project", ["Status", "PI", "Period", "状态", "负责人", "起止"]),
        ("patent", "en/patent", ["Inventors", "Patent no", "Status", "发明人", "专利号"]),
        ("award", "en/award", ["Awardees", "Year", "获奖人", "获奖年份"]),
        ("authors", "en/authors", ["Introduction", "Research outputs", "个人简介", "学术成果"]),
        ("research", "en/research", []),
        ("post", "en/post", ["Gallery", "图集"]),
    ]
    for section, prefix, keys in detail_checks:
        base = PUBLIC / Path(prefix)
        pages = sorted(base.glob("*/index.html"))[:4]
        if not pages:
            lines.append(f"{section}: no pages")
            continue
        for p in pages:
            html = read(p)
            rel = str(p.relative_to(PUBLIC)).replace("\\", "/")
            bad = [k for k in keys if CJK.search(k) and k in html]
            good = [k for k in keys if not CJK.search(k) and k in html]
            if bad:
                issues.append((f"detail:{section}", f"{p.parent.name}: still has {bad}"))
            lines.append(f"  {rel}: EN-labels={good or '-'} ZH-leak={bad or 'ok'}")

    # --- content translation coverage ---
    lines.append("\n=== Content .en.md coverage ===")
    care = ("publication", "patent", "award", "project", "post", "research", "authors")
    missing_en = []
    for sec in care:
        d = CONTENT / sec
        if not d.exists():
            continue
        for zh in d.rglob("index.md"):
            en = zh.with_name("index.en.md")
            if not en.exists():
                missing_en.append(str(zh.relative_to(CONTENT)))
        for zh in d.rglob("_index.md"):
            en = zh.with_name("_index.en.md")
            if not en.exists():
                missing_en.append(str(zh.relative_to(CONTENT)))
    lines.append(f"missing EN translations: {len(missing_en)}")
    for m in missing_en[:30]:
        lines.append(f"  {m}")
        issues.append(("missing-en", m))

    # --- Chinese body still on EN details (abstracts) ---
    lines.append("\n=== EN pages with mostly-CJK article body (sample) ---")
    body_cjk = []
    for section in ("publication", "project", "patent", "award", "post", "research", "authors"):
        for p in sorted((PUBLIC / "en" / section).glob("*/index.html")):
            html = read(p)
            # abstract / article-style
            chunks = re.findall(r"lab-article-abstract-body[\s\S]{0,800}|article-style[\s\S]{0,800}", html)
            text = re.sub(r"<[^>]+>", " ", " ".join(chunks))
            if mostly_cjk(text[:400]) and len(CJK.findall(text)) > 20:
                body_cjk.append(str(p.relative_to(PUBLIC / "en")))
    lines.append(f"likely untranslated bodies: {len(body_cjk)}")
    for b in body_cjk[:20]:
        lines.append(f"  {b}")
        issues.append(("body-cjk", b))

    # --- venue CJK (info) ---
    venues = re.findall(r"lab-row-venue[^>]*>([^<]+)", en_pub)
    cjk_v = [v for v in venues if CJK.search(v)]
    lines.append(f"\nEN publication venues CJK: {len(cjk_v)}/{len(venues)}")

    print("\n".join(lines))
    print(f"\n========== ISSUES ({len(issues)}) ==========")
    by = defaultdict(list)
    for k, v in issues:
        by[k].append(v)
    for k, vs in sorted(by.items()):
        print(f"\n[{k}] ({len(vs)})")
        for v in vs[:40]:
            print(f"  - {v}")
        if len(vs) > 40:
            print(f"  ... +{len(vs)-40}")

    out = ROOT / "scripts/_audit_en_report.txt"
    out.write_text("\n".join(lines) + "\n\n" + "\n".join(f"{a}\t{b}" for a, b in issues), encoding="utf-8")
    print(f"\nWrote {out}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
