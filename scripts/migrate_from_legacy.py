# -*- coding: utf-8 -*-
"""Migrate authors/publications/projects/patents/awards/research (+ EN) into lab-xiao."""
from __future__ import annotations

import shutil
from pathlib import Path

from lab_io import dump_yaml, load_fm, normalize_section, write_page

LEGACY = Path(r"D:\code-tyx\lab-xiao\theme-research-group\theme-research-group-main")
SITE = Path(__file__).resolve().parents[1] / "site"
AUTHORS_OUT = SITE / "data" / "authors"


def copy_assets(src: Path, dst: Path) -> None:
    for asset in src.iterdir():
        if not asset.is_file():
            continue
        if asset.name.lower().endswith((".md", ".html")):
            continue
        shutil.copy2(asset, dst / asset.name)


def migrate_authors() -> int:
    AUTHORS_OUT.mkdir(parents=True, exist_ok=True)
    demo = AUTHORS_OUT / "me.yaml"
    if demo.exists():
        demo.unlink()
    n = 0
    for md in sorted((LEGACY / "content" / "authors").glob("*/_index.md")):
        slug = md.parent.name
        data, body = load_fm(md)
        # EN companion if present
        en_md = md.parent / "_index.en.md"
        en_data, en_body = load_fm(en_md) if en_md.exists() else ({}, "")

        title = str(data.get("title") or slug)
        given = str(data.get("first_name") or "")
        family = str(data.get("last_name") or "")
        role = str(data.get("role") or "").replace("\n", " / ")
        bio = str(data.get("bio") or "").strip() or body[:280]
        orgs = data.get("organizations") or []
        affiliations = []
        for org in orgs:
            if isinstance(org, dict) and org.get("name"):
                affiliations.append({"name": org["name"], "url": org.get("url") or ""})
        if not affiliations:
            affiliations = [
                {"name": "西安理工大学计算机科学与技术学院", "url": "https://jsj.xaut.edu.cn/"}
            ]
        links = []
        if data.get("email"):
            links.append(
                {"icon": "at-symbol", "url": f"mailto:{data['email']}", "label": "Email"}
            )
        author = {
            "schema": "hugoblox/author/v1",
            "slug": slug,
            "is_owner": bool(data.get("superuser")),
            "name": {
                "display": title,
                "given": given,
                "family": family,
                "alternate": "",
                "pronunciation": "",
                "pronouns": "",
            },
            "postnominals": [],
            "status": {"icon": ""},
            "role": role,
            "bio": bio,
            "affiliations": affiliations,
            "links": links,
            "interests": list(data.get("interests") or []),
            "education": [],
            "user_groups": list(data.get("user_groups") or []),
            "weight": int(data.get("weight") or 999),
        }
        if en_data:
            author["i18n"] = {
                "en": {
                    "name": {
                        "display": str(en_data.get("title") or title),
                        "given": str(en_data.get("first_name") or given),
                        "family": str(en_data.get("last_name") or family),
                    },
                    "role": str(en_data.get("role") or role).replace("\n", " / "),
                    "bio": str(en_data.get("bio") or en_body[:280] or bio),
                }
            }
        (AUTHORS_OUT / f"{slug}.yaml").write_text(dump_yaml(author), encoding="utf-8")
        media_dir = SITE / "assets" / "media" / "authors"
        media_dir.mkdir(parents=True, exist_ok=True)
        for av in md.parent.glob("avatar.*"):
            if av.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
                shutil.copy2(av, media_dir / f"{slug}{av.suffix.lower()}")
                break
        n += 1
    return n


def _pub_block(data: dict) -> dict:
    pub = data.get("publication")
    block = dict(pub) if isinstance(pub, dict) else {"name": str(pub or data.get("publication_short") or "").strip()}
    for key in ("volume", "issue", "pages"):
        if data.get(key) and key not in block:
            block[key] = data[key]
    if not block.get("name"):
        block.pop("name", None)
    return block


def _convert_pub_fm(data: dict) -> dict:
    fm: dict = {
        "title": data.get("title"),
        "authors": [str(a) for a in (data.get("authors") or [])],
        "date": data.get("date"),
        "publication_types": data.get("publication_types") or ["article-journal"],
        "publication": _pub_block(data),
        "summary": data.get("summary") or "",
        "abstract": data.get("abstract") or "",
        "featured": bool(data.get("featured")),
        "tags": list(data.get("tags") or []),
    }
    if data.get("doi"):
        fm["hugoblox"] = {"ids": {"doi": str(data["doi"])}}
    links = []
    mapping = (
        ("url_html", "url"),
        ("url_pdf", "pdf"),
        ("url_code", "code"),
        ("url_dataset", "dataset"),
    )
    for src, typ in mapping:
        if data.get(src):
            links.append({"type": typ, "url": data[src]})
    if links:
        fm["links"] = links
    for extra in ("ccf", "publication_short", "research"):
        if data.get(extra) is not None:
            fm[extra] = data[extra]
    return fm


FEATURED = {
    "2025-cedflow-plus",
    "2024-aaai-cedflow",
    "2022-tip-fdl-hcgh",
    "2014-cvpr-aliasing",
    "2024-spgfusion",
    "2026-fedd-net-lowlight",
}


def migrate_section_bundles(
    legacy_section: str,
    out_section: str,
    *,
    convert=None,
    drop_samples: tuple[str, ...] = (),
) -> int:
    out_section = normalize_section(out_section)
    src = LEGACY / "content" / legacy_section
    dst = SITE / "content" / out_section
    dst.mkdir(parents=True, exist_ok=True)
    for sample in drop_samples:
        p = dst / sample
        if p.exists():
            shutil.rmtree(p)
    n = 0
    for md in sorted(src.glob("*/index.md")):
        slug = md.parent.name
        data, body = load_fm(md)
        fm = convert(data) if convert else dict(data)
        if out_section == "publications" and slug in FEATURED:
            fm["featured"] = True
        out_dir = dst / slug
        write_page(out_dir, "index.md", fm, body)
        en = md.parent / "index.en.md"
        if en.exists():
            en_data, en_body = load_fm(en)
            en_fm = convert(en_data) if convert else dict(en_data)
            if out_section == "publications" and slug in FEATURED:
                en_fm["featured"] = True
            write_page(out_dir, "index.en.md", en_fm, en_body)
        copy_assets(md.parent, out_dir)
        n += 1
    for lang_suffix in ("", ".en"):
        src_idx = src / f"_index{lang_suffix}.md"
        if not src_idx.exists():
            continue
        data, body = load_fm(src_idx)
        data.pop("layout", None)
        write_page(dst, f"_index{lang_suffix}.md", data, body)
    return n


def migrate_research() -> int:
    src = LEGACY / "content" / "research"
    dst = SITE / "content" / "research"
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for md in sorted(src.glob("*/index.md")):
        slug = md.parent.name
        data, body = load_fm(md)
        out = dst / slug
        write_page(out, "index.md", data, body)
        en = md.parent / "index.en.md"
        if en.exists():
            en_data, en_body = load_fm(en)
            write_page(out, "index.en.md", en_data, en_body)
        copy_assets(md.parent, out)
        n += 1
    for lang_suffix in ("", ".en"):
        src_idx = src / f"_index{lang_suffix}.md"
        if src_idx.exists():
            data, body = load_fm(src_idx)
            write_page(dst, f"_index{lang_suffix}.md", data, body)
    return n


def migrate_posts() -> int:
    src = LEGACY / "content" / "post"
    dst = SITE / "content" / normalize_section("blog")
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for md in sorted(src.glob("*/index.md")):
        slug = md.parent.name
        data, body = load_fm(md)
        out = dst / slug
        write_page(out, "index.md", data, body)
        en = md.parent / "index.en.md"
        if en.exists():
            en_data, en_body = load_fm(en)
            write_page(out, "index.en.md", en_data, en_body)
        copy_assets(md.parent, out)
        n += 1
    return n


def main() -> None:
    if not LEGACY.is_dir():
        raise SystemExit(f"Legacy site not found: {LEGACY}")
    stats = {
        "authors": migrate_authors(),
        "publications": migrate_section_bundles(
            "publication",
            "publications",
            convert=_convert_pub_fm,
            drop_samples=("conference-paper", "journal-article", "preprint"),
        ),
        "projects": migrate_section_bundles("project", "projects"),
        "patents": migrate_section_bundles("patent", "patent"),
        "awards": migrate_section_bundles("award", "award"),
        "research": migrate_research(),
        "posts": migrate_posts(),
    }
    print(" ".join(f"{k}={v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()
