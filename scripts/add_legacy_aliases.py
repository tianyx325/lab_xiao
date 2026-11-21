# -*- coding: utf-8 -*-
"""Add Hugo aliases so legacy Bootstrap URLs redirect to Kit paths.

Only touches default-language files (index.md / _index.md). Legacy site was
Chinese-first; EN pages must not get /en/... aliases (Hugo would nest en/en/).
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

SITE = Path(__file__).resolve().parents[1] / "site"
CONTENT = SITE / "content"
FM_RE = re.compile(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n?(.*)$", re.S)

MAPPINGS = (
    ("publications", "publication"),
    ("projects", "project"),
    ("blog", "post"),
    ("patent", "patent"),
    ("award", "award"),
    ("research", "research"),
    ("people", "people"),
)


def load(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        raise ValueError(f"no front matter: {path}")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def dump(data: dict) -> str:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)


def write(path: Path, data: dict, body: str) -> None:
    text = "---\n" + dump(data) + "---\n"
    if body and not body.startswith("\n"):
        text += "\n"
    text += body if body else ""
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def ensure_aliases(path: Path, aliases: list[str]) -> bool:
    data, body = load(path)
    existing = data.get("aliases") or []
    if not isinstance(existing, list):
        existing = [existing]
    merged = list(dict.fromkeys([*existing, *aliases]))
    if merged == existing:
        return False
    data["aliases"] = merged
    write(path, data, body)
    return True


def strip_en_prefixed_aliases(path: Path) -> bool:
    """Remove mistaken /en/... aliases from EN content files."""
    data, body = load(path)
    existing = data.get("aliases") or []
    if not isinstance(existing, list):
        existing = [existing] if existing else []
    cleaned = [a for a in existing if not (isinstance(a, str) and a.startswith("/en/"))]
    if cleaned == existing:
        if not cleaned and "aliases" in data:
            del data["aliases"]
            write(path, data, body)
            return True
        return False
    if cleaned:
        data["aliases"] = cleaned
    elif "aliases" in data:
        del data["aliases"]
    write(path, data, body)
    return True


def main() -> None:
    n = 0
    stripped = 0
    for new_sec, old_sec in MAPPINGS:
        sec_dir = CONTENT / new_sec
        if not sec_dir.is_dir():
            continue
        # Clean EN files first
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
