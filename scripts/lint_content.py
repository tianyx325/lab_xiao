# -*- coding: utf-8 -*-
"""Validate site content against the data model (docs/DATA-MODEL.md).

Checks:
  E* errors   — model violations that break rendering or relations
  W* warnings — tolerated but should be cleaned up

Usage:
  py -3 scripts/lint_content.py            # exit 1 on errors
  py -3 scripts/lint_content.py --quiet    # errors only
"""
from __future__ import annotations

import argparse
import re as _re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

ALLOWED_USER_GROUPS = {"导师", "博士生", "硕士生", "研三", "研二", "研一", "博一", "博二", "博三", "本科生", "在读学生", "毕业生"}
ALLOWED_PUB_TYPES = {"article-journal", "paper-conference", "preprint",
                     "report", "thesis", "book", "book-section", "chapter"}
ALLOWED_PATENT_STATUS = {"granted", "pending"}
ALLOWED_PROJECT_STATUS = {"ongoing", "completed"}
ALLOWED_CCF = {"A", "B", "C"}
ALLOWED_PATENT_TYPE = {"invention", "utility", "design"}
ALLOWED_PROJECT_TYPE = {"vertical", "horizontal"}
ALLOWED_AWARD_LEVEL = {"national", "provincial", "university", "society"}
ALLOWED_AWARD_RANK = {"special", "first", "second", "third", "excellent", ""}
RESEARCH_BODY_SECTIONS = ("方向简介", "研究内容", "关键问题", "技术路线")

# ── 双语约定：中文 X.md 为默认语言，英文 X.en.md 为翻译版本 ─────────
# 受控词表 / 正文四段式按语言区分；其余枚举两语言共用
ALLOWED_USER_GROUPS_EN = {"Supervisor", "Ph.D. Students", "M.S. Year 1",
                          "M.S. Year 2", "M.S. Year 3", "Undergraduates",
                          "Current Students", "Alumni"}
RESEARCH_BODY_SECTIONS_EN = ("Direction Overview", "Research Topics",
                             "Key Challenges", "Technical Approach")
_ZH_RE = _re.compile(r"[\u4e00-\u9fff]")

# ── 字段契约（docs/DATA-MODEL.md v2）：契约外字段 = 错误 ─────────────
# Hugo 内置通用键各类型均允许
_HUGO_COMMON = {"aliases", "draft", "weight", "lastmod", "description",
                "linkTitle", "subtitle", "show_breadcrumb"}
FIELD_CONTRACT: dict[str, set[str]] = {
    "authors": _HUGO_COMMON | {
        "title", "first_name", "last_name", "superuser", "role",
        "organizations", "bio", "research", "user_groups", "interests",
        "email", "social", "enroll_year", "personal_url", "destination"},
    "publication": _HUGO_COMMON | {
        "title", "authors", "date", "publishDate", "publication_types",
        "publication", "publication_short", "volume", "issue", "pages",
        "doi", "url_pdf", "url_html", "url_code", "url_dataset",
        "summary", "abstract", "featured", "research", "image", "tags",
        "paper_award", "ccf"},
    "patent": _HUGO_COMMON | {
        "title", "summary", "date", "application_date", "authors",
        "patent_number", "patent_status", "patent_type",
        "url_patent", "url_pdf"},
    "project": _HUGO_COMMON | {
        "title", "summary", "date", "date_end", "authors",
        "project_code", "project_type", "project_status", "funding",
        "url_external", "image", "tags"},
    "award": _HUGO_COMMON | {
        "title", "authors", "date", "summary", "level", "rank", "tags"},
    "research": _HUGO_COMMON | {
        "title", "date", "weight", "summary", "tags"},
    "post": _HUGO_COMMON | {
        "title", "summary", "date", "authors", "categories", "image"},
}
# publishDate 与 date 冗余，v2 已删——显式列为禁止项
FORBIDDEN_FIELDS = {"publishDate", "award_date", "research_focus",
                    "highlight_name", "projects", "external_link",
                    "project_kind", "sort"}

# ── slug 规范：<类型前缀>-<自然键>，小写字母/数字/连字符 ────────────
SLUG_RULES: dict[str, tuple[str, int]] = {
    # section: (正则, 最大长度)
    "project": (r"^proj-[a-z0-9-]+$", 60),
    "patent": (r"^zl-[0-9]+$", 40),
    "publication": (r"^\d{4}-[a-z0-9-]+$", 80),
    "authors": (r"^[a-z0-9-]+$", 40),
    "award": (r"^[a-z0-9-]+$", 60),
    "research": (r"^[a-z0-9-]+$", 40),
    "post": (r"^[a-z0-9-]+$", 80),
}
# 学籍推算基准：研一=本学年入学
from datetime import date as _date
_TODAY = _date.today()
_ACADEMIC_YEAR = _TODAY.year if _TODAY.month >= 9 else _TODAY.year - 1
_GROUP_BY_OFFSET = {0: "研一", 1: "研二", 2: "研三"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_fm(path: Path) -> dict | None:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return None
    parts = raw.split("\n---", 1)
    try:
        fm = yaml.safe_load(parts[0][3:]) or {}
    except yaml.YAMLError as e:
        err(f"YAML 解析失败: {path.relative_to(ROOT)} → {e}")
        return None
    return fm if isinstance(fm, dict) else {}


def load_section(section: str, glob: str = "*/index.md",
                 locale: str = "zh") -> dict[str, dict]:
    """Return {slug: front-matter} for a section (locale zh or en)."""
    out: dict[str, dict] = {}
    for path in sorted((CONTENT / section).glob(glob)):
        slug = path.parent.name
        fm = load_fm(path)
        if fm is None:
            err(f"E-title {section}/{slug} [{locale}]: front matter 缺失或非法")
            continue
        out[slug] = fm
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true", help="只输出错误")
    args = ap.parse_args()

    # ── 已知实体集（供外键校验） ──────────────────────────────
    members = load_section("authors", "*/_index.md")
    research_slugs = set(load_section("research").keys())
    publications = load_section("publication")
    patents = load_section("patent")
    projects = load_section("project")
    awards = load_section("award")
    posts = load_section("post")

    # 英文版（.en.md）——契约/slug/枚举同样执法，语义唯一性只看中文版
    en_members = load_section("authors", "*/_index.en.md", "en")
    en_publications = load_section("publication", "*/index.en.md", "en")
    en_patents = load_section("patent", "*/index.en.md", "en")
    en_projects = load_section("project", "*/index.en.md", "en")
    en_awards = load_section("award", "*/index.en.md", "en")
    en_posts = load_section("post", "*/index.en.md", "en")
    en_research = load_section("research", "*/index.en.md", "en")

    alias_file = ROOT / "data" / "lab_author_aliases.yaml"
    aliases: dict[str, str] = {}
    if alias_file.exists():
        raw = yaml.safe_load(alias_file.read_text(encoding="utf-8")) or {}
        aliases = {str(k): str(v) for k, v in raw.items()}
        for k, v in aliases.items():
            if v not in members:
                warn(f"W-alias 别名「{k}」指向不存在的成员 slug「{v}」")

    # ── 字段契约与 slug 规范（两语言统一执行） ────────────────
    all_sections: dict[str, dict[str, dict]] = {
        "authors": members, "publication": publications,
        "patent": patents, "project": projects, "award": awards,
        "research": load_section("research"), "post": posts,
        "authors@en": en_members, "publication@en": en_publications,
        "patent@en": en_patents, "project@en": en_projects,
        "award@en": en_awards, "research@en": en_research,
        "post@en": en_posts,
    }
    for section_key, pages in all_sections.items():
        section, _, locale = section_key.partition("@")
        locale = locale or "zh"
        contract = FIELD_CONTRACT.get(section, set())
        slug_re, max_len = SLUG_RULES.get(section, (r"^[a-z0-9-]+$", 60))
        for slug, fm in pages.items():
            for key in fm:
                key = str(key)
                if key in FORBIDDEN_FIELDS:
                    err(f"E-contract {section}/{slug} [{locale}]: 禁用字段「{key}」"
                        f"（v2 已废弃，请迁移）")
                elif contract and key not in contract:
                    err(f"E-contract {section}/{slug} [{locale}]: 契约外字段「{key}」"
                        f"（合法字段见 docs/DATA-MODEL.md）")
            if not _re.fullmatch(slug_re, slug):
                err(f"E-slug {section}/{slug}: 不符合命名规范 {slug_re}")
            elif len(slug) > max_len:
                err(f"E-slug {section}/{slug}: 超长（>{max_len}）")

    # ── 双语配对：中文页与英文页一一对应 ─────────────────────
    zh_sets = {"authors": members, "publication": publications,
               "patent": patents, "project": projects, "award": awards,
               "research": research_slugs, "post": posts}
    en_sets = {"authors": en_members, "publication": en_publications,
               "patent": en_patents, "project": en_projects,
               "award": en_awards, "research": set(en_research),
               "post": en_posts}
    for section, zh_pages in zh_sets.items():
        for slug in sorted(zh_pages):
            if slug not in en_sets[section]:
                err(f"E-i18n {section}/{slug}: 缺英文版 .en.md")
        for slug in sorted(en_sets[section]):
            if slug not in zh_pages:
                err(f"E-i18n {section}/{slug} [en]: 英文版无对应中文页")
        # 英文页 title/summary 不应残留中文（venue 等专名字段除外）
        for slug, fm in sorted(en_sets[section].items() if
                               isinstance(en_sets[section], dict) else []):
            if not isinstance(fm, dict):
                continue
            for key in ("title", "summary"):
                val = fm.get(key)
                if isinstance(val, str) and _ZH_RE.search(val):
                    warn(f"W-i18n {section}/{slug} [en]: {key} 含中文"
                         f"「{val[:20]}…」，请确认是否漏译")

    def check_authors(section: str, slug: str, fm: dict) -> None:
        """authors 双轨制（见 DATA-MODEL 第 3 节）：成员 slug 与外协全名均合法。
        仅在写了别名映射中的变体时提醒改用 slug。"""
        vals = fm.get("authors") or []
        if not isinstance(vals, list):
            vals = [vals]
        if not vals:
            err(f"E-authors {section}/{slug}: authors 为空")
        for v in vals:
            v = str(v)
            if v in members:
                continue
            if v in aliases:
                warn(f"W-authors {section}/{slug}: 作者「{v}」是成员别名，"
                     f"应直接写 slug「{aliases[v]}」")

    def check_research_fk(section: str, slug: str, fm: dict) -> None:
        vals = fm.get("research") or []
        if not isinstance(vals, list):
            vals = [vals]
        for v in vals:
            if str(v) not in research_slugs:
                err(f"E-fk {section}/{slug}: research 引用「{v}」"
                    f"不存在（现有: {', '.join(sorted(research_slugs))}）")

    # ── 成员 ─────────────────────────────────────────────────
    if "admin" not in members:
        err("E-member 缺少 admin（实验室负责人）")
    supers = [s for s, fm in members.items() if fm.get("superuser")]
    if len(supers) > 1:
        err(f"E-member superuser 只能有一个，当前: {supers}")
    for slug, fm in members.items():
        if not fm.get("title"):
            err(f"E-member authors/{slug}: title 为空")
        if not fm.get("role"):
            warn(f"W-member authors/{slug}: role 为空")
        # v2：已废弃字段回归即提醒
        for legacy in ("research_focus", "highlight_name"):
            if legacy in fm:
                warn(f"W-member authors/{slug}: {legacy} 已废弃（展示由 "
                     f"research[] 派生），请删除")
        if "organizations" in fm and not fm.get("superuser"):
            warn(f"W-member authors/{slug}: organizations 已废弃"
                 f"（默认取 params.lab.org_name），请删除")
        groups = fm.get("user_groups") or []
        if not isinstance(groups, list):
            groups = [groups]
        if not groups:
            err(f"E-member authors/{slug}: user_groups 为空（成员页无法分组）")
        for g in groups:
            if str(g) not in ALLOWED_USER_GROUPS:
                err(f"E-member authors/{slug}: user_groups「{g}」不在受控词表: "
                    f"{', '.join(sorted(ALLOWED_USER_GROUPS))}")
        # 学籍与入学年份一致性（仅研一~研三）
        enroll = fm.get("enroll_year")
        if enroll:
            offset = _ACADEMIC_YEAR - int(enroll)
            expect = _GROUP_BY_OFFSET.get(offset)
            if expect and groups and str(groups[0]) != expect:
                warn(f"W-member authors/{slug}: enroll_year={enroll} 按学籍应为"
                     f"「{expect}」，当前分组为「{groups[0]}」")
        if fm.get("destination") and "毕业生" not in [str(g) for g in groups]:
            warn(f"W-member authors/{slug}: destination 仅有毕业生填写")
        check_research_fk("authors", slug, fm)

    # ── 英文成员：分组受控词表（英文侧） ─────────────────────
    for slug, fm in en_members.items():
        groups = fm.get("user_groups") or []
        if not isinstance(groups, list):
            groups = [groups]
        for g in groups:
            if str(g) not in ALLOWED_USER_GROUPS_EN:
                err(f"E-member authors/{slug} [en]: user_groups「{g}」不在英文"
                    f"受控词表: {', '.join(sorted(ALLOWED_USER_GROUPS_EN))}")

    # ── 论文 ─────────────────────────────────────────────────
    for slug, fm in publications.items():
        if not fm.get("title"):
            err(f"E-pub publication/{slug}: title 为空")
        if fm.get("date") is None:
            err(f"E-pub publication/{slug}: date 缺失（列表年份筛选依赖）")
        pt = fm.get("publication_types") or []
        if not isinstance(pt, list):
            pt = [pt]
        if not pt:
            err(f"E-pub publication/{slug}: publication_types 为空")
        for t in pt:
            if str(t) not in ALLOWED_PUB_TYPES:
                err(f"E-pub publication/{slug}: publication_types「{t}」非法")
        check_authors("publication", slug, fm)
        check_research_fk("publication", slug, fm)
        if "featured" not in fm:
            warn(f"W-pub publication/{slug}: 缺 featured 字段（默认按 false 处理）")
        if "publishDate" in fm:
            warn(f"W-pub publication/{slug}: publishDate 已废弃（与 date 冗余），请删除")
        ccf = str(fm.get("ccf") or "")
        if ccf and ccf not in ALLOWED_CCF:
            err(f"E-pub publication/{slug}: ccf「{ccf}」非法（A/B/C）")

    # ── 专利 ─────────────────────────────────────────────────
    seen_numbers: dict[str, str] = {}
    for slug, fm in patents.items():
        num = str(fm.get("patent_number") or "").strip()
        if not num:
            err(f"E-patent patent/{slug}: patent_number 缺失（自然键）")
        elif num in seen_numbers:
            err(f"E-patent patent_number 重复: {num} "
                f"（{seen_numbers[num]} 与 {slug}）")
        else:
            seen_numbers[num] = slug
        status = str(fm.get("patent_status") or "")
        if status and status not in ALLOWED_PATENT_STATUS:
            err(f"E-patent patent/{slug}: patent_status「{status}」非法")
        ptype = str(fm.get("patent_type") or "")
        if not ptype:
            err(f"E-patent patent/{slug}: patent_type 缺失（invention/utility/design）")
        elif ptype not in ALLOWED_PATENT_TYPE:
            err(f"E-patent patent/{slug}: patent_type「{ptype}」非法")
        for t in [str(x) for x in (fm.get("tags") or [])]:
            if t in ("发明专利", "已授权", "实用新型", "外观设计"):
                warn(f"W-patent patent/{slug}: tags 含「{t}」——类型与状态已由 "
                     f"patent_type/patent_status 表达，请从 tags 删除")
        check_authors("patent", slug, fm)

    # ── 项目 ─────────────────────────────────────────────────
    # v2：project_type 显式分类；纵向必须有课题号；资助类型走 funding 字段
    VERTICAL_MARKERS = ("基金", "重点", "面上", "青年", "联合", "重大",
                        "专项", "NSFC", "国家")
    seen_codes: dict[str, str] = {}
    for slug, fm in projects.items():
        code = str(fm.get("project_code") or "").strip()
        kind = str(fm.get("project_type") or "")
        if not kind:
            err(f"E-project project/{slug}: project_type 缺失（vertical/horizontal）")
        elif kind not in ALLOWED_PROJECT_TYPE:
            err(f"E-project project/{slug}: project_type「{kind}」非法")
        if kind == "vertical" and not code:
            err(f"E-project project/{slug}: 纵向项目缺少 project_code")
        if kind == "vertical" and not str(fm.get("funding") or "").strip():
            warn(f"W-project project/{slug}: 纵向项目建议填写 funding（资助类别）")
        if code:
            if code in seen_codes:
                err(f"E-project project_code 重复: {code} "
                    f"（{seen_codes[code]} 与 {slug}）")
            else:
                seen_codes[code] = slug
        for t in [str(x) for x in (fm.get("tags") or [])]:
            if any(m in t for m in VERTICAL_MARKERS):
                warn(f"W-project project/{slug}: tags 含资助类型「{t}」——"
                     f"请移入 funding 字段")
        status = str(fm.get("project_status") or "")
        if status and status not in ALLOWED_PROJECT_STATUS:
            err(f"E-project project/{slug}: project_status「{status}」非法")
        date_end = fm.get("date_end")
        if status == "ongoing" and date_end:
            try:
                y, m, d = [int(x) for x in str(date_end)[:10].split("-")]
                if _date(y, m, d) < _TODAY.replace(year=_TODAY.year - 1):
                    warn(f"W-project project/{slug}: date_end 已过一年仍为 ongoing，"
                         f"请确认状态")
            except ValueError:
                pass
        check_authors("project", slug, fm)

    # ── 奖项 ─────────────────────────────────────────────────
    LEVEL_TAG_WORDS = {"国家级", "省部级", "省级", "校级", "学会", "行业"}
    RANK_WORDS = ("特等", "一等", "二等", "三等")
    for slug, fm in awards.items():
        if "award_date" in fm:
            err(f"E-award award/{slug}: award_date 已废弃（date 即获奖日期），请删除")
        level = str(fm.get("level") or "")
        if not level:
            err(f"E-award award/{slug}: level 缺失（national/provincial/"
                f"university/society）")
        elif level not in ALLOWED_AWARD_LEVEL:
            err(f"E-award award/{slug}: level「{level}」非法")
        rank = str(fm.get("rank") or "")
        if rank and rank not in ALLOWED_AWARD_RANK:
            err(f"E-award award/{slug}: rank「{rank}」非法")
        for t in [str(x) for x in (fm.get("tags") or [])]:
            if t in LEVEL_TAG_WORDS or any(w in t for w in RANK_WORDS):
                warn(f"W-award award/{slug}: tags 含「{t}」——级别与等级已由 "
                     f"level/rank 表达，请从 tags 删除")
        check_authors("award", slug, fm)

    # ── 动态 ─────────────────────────────────────────────────
    for slug, fm in posts.items():
        if fm.get("date") is None:
            err(f"E-post post/{slug}: date 缺失")
        check_authors("post", slug, fm)

    # ── 研究方向：正文四段式约定（两语言各自执法） ───────────
    for slug in sorted(research_slugs):
        path = CONTENT / "research" / slug / "index.md"
        body = path.read_text(encoding="utf-8")
        missing = [s for s in RESEARCH_BODY_SECTIONS
                   if f"### {s}" not in body]
        if missing:
            warn(f"W-research research/{slug}: 正文缺四段式标题: "
                 f"{'、'.join(missing)}")
    for slug in sorted(en_research):
        path = CONTENT / "research" / slug / "index.en.md"
        body = path.read_text(encoding="utf-8")
        missing = [s for s in RESEARCH_BODY_SECTIONS_EN
                   if f"### {s}" not in body]
        if missing:
            warn(f"W-research research/{slug} [en]: 正文缺四段式标题: "
                 f"{', '.join(missing)}")

    # ── 汇总输出 ─────────────────────────────────────────────
    if not args.quiet:
        for w in warnings:
            print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n成员 {len(members)} · 论文 {len(publications)} · 专利 {len(patents)} · "
          f"项目 {len(projects)} · 奖项 {len(awards)} · 动态 {len(posts)} · "
          f"方向 {len(research_slugs)}")
    print(f"错误 {len(errors)} · 警告 {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
