# -*- coding: utf-8 -*-
"""Shared content I/O for lab migration / maintenance scripts."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

FM_RE = re.compile(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n?(.*)$", re.S)

# Legacy singular → repo plural (and identity for already-canonical keys).
SECTION_CANON = {
    "publication": "publications",
    "publications": "publications",
    "project": "projects",
    "projects": "projects",
    "post": "blog",
    "blog": "blog",
    "patent": "patent",
    "award": "award",
    "research": "research",
    "people": "people",
}


def normalize_section(name: str) -> str:
    key = (name or "").strip()
    return SECTION_CANON.get(key, key)


def load_fm(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def dump_yaml(data: dict) -> str:
    return yaml.safe_dump(
        data, allow_unicode=True, sort_keys=False, default_flow_style=False
    )


def write_page(out_dir: Path, name: str, fm: dict, body: str = "") -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    text = "---\n" + dump_yaml(fm) + "---\n"
    if body:
        if not body.startswith("\n"):
            text += "\n"
        text += body
        if not text.endswith("\n"):
            text += "\n"
    else:
        if not text.endswith("\n"):
            text += "\n"
    (out_dir / name).write_text(text, encoding="utf-8")


def write_fm_file(path: Path, fm: dict, body: str = "") -> None:
    write_page(path.parent, path.name, fm, body)
