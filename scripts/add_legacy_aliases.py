# -*- coding: utf-8 -*-
"""Add Hugo aliases so legacy Bootstrap URLs redirect to Kit paths.

Only touches default-language files (index.md / _index.md). Legacy site was
Chinese-first; EN pages must not get /en/... aliases (Hugo would nest en/en/).
"""
from __future__ import annotations

from pathlib import Path

from lab_io import load_fm, normalize_section, write_fm_file

SITE = Path(__file__).resolve().parents[1] / "site"
CONTENT = SITE / "content"

# (canonical section folder, legacy singular URL segment)
MAPPINGS = (
    ("publications", "publication"),
    ("projects", "project"),
    ("blog", "post"),
    ("patent", "patent"),
    ("award", "award"),
    ("research", "research"),
    ("people", "people"),
)


def ensure_aliases(path: Path, aliases: list[str]) -> bool:
    data, body = load_fm(path)
    if not data and "---" not in path.read_text(encoding="utf-8")[:4]:
        raise ValueError(f"no front matter: {path}")
    existing = data.get("aliases") or []
    if not isinstance(existing, list):
        existing = [existing]
    merged = list(dict.fromkeys([*existing, *aliases]))
    if merged == existing:
        return False
    data["aliases"] = merged
    write_fm_file(path, data, body)
    return True


def strip_en_prefixed_aliases(path: Path) -> bool:
    data, body = load_fm(path)
    existing = data.get("aliases") or []
    if not isinstance(existing, list):
        existing = [existing] if existing else []
    cleaned = [a for a in existing if not (isinstance(a, str) and a.startswith("/en/"))]
    if cleaned == existing:
        if not cleaned and "aliases" in data:
            del data["aliases"]
            write_fm_file(path, data, body)
            return True
        return False
    if cleaned:
        data["aliases"] = cleaned
    elif "aliases" in data:
        del data["aliases"]
    write_fm_file(path, data, body)
    return True


def main() -> None:
    n = 0
    stripped = 0
    for new_sec, old_sec in MAPPINGS:
        assert normalize_section(new_sec) == new_sec
        sec_dir = CONTENT / new_sec
        if not sec_dir.is_dir():
            continue
        for en_path in [sec_dir / "_index.en.md", *sec_dir.glob("*/index.en.md")]:
            if en_path.exists() and strip_en_prefixed_aliases(en_path):
                stripped += 1
        if new_sec == old_sec:
            continue
        idx = sec_dir / "_index.md"
        if idx.exists() and ensure_aliases(idx, [f"/{old_sec}/"]):
            n += 1
        for md in sec_dir.glob("*/index.md"):
            slug = md.parent.name
            if ensure_aliases(md, [f"/{old_sec}/{slug}/"]):
                n += 1
    print(f"updated={n} stripped_en={stripped}")


if __name__ == "__main__":
    main()
