# -*- coding: utf-8 -*-
"""Set authors' `research:` slugs from lab research pages (content/research/*)."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "content" / "authors"

# folder names under content/research/
# agent | low-light | depth | action
# Advisors (导师) keep free-text research_focus — do not list them here.
MAP: dict[str, list[str]] = {
    "chang-ya-xuan": ["depth"],
    "dai-xue-yang": ["depth", "low-light"],
    "du-kun": ["depth"],
    "guo-huan-huan": ["action"],
    "julianno": ["depth", "low-light"],
    "li-peng-qin": ["depth"],
    "li-wen-gai": ["low-light", "depth"],
    "tian-yunxiang": ["agent"],
    "tian-zhao-yang": ["depth"],
    "wang-long-hao": ["action"],
    "wang-xin-le": ["agent"],
    "wang-yi": ["low-light"],
    "xue-kai-xuan": ["low-light"],
    "xue-yi-rui": ["agent"],
    "zhai-qian-lin": ["action"],
    "zhang-heng-chang": ["agent"],
    "zhao-guan-zheng": ["agent"],
    "zhou-guang-bin": ["low-light", "depth"],
    "zhou-he-xin": ["agent"],
}


def set_or_insert_research(fm: str, slugs: list[str]) -> str:
    block = "research:\n" + "".join(f"  - {s}\n" for s in slugs)
    if re.search(r"^research:\s*$", fm, re.M) or re.search(
        r"^research:\s*\n(?:[ \t]+-[^\n]*\n)+", fm, re.M
    ):
        fm, n = re.subn(
            r"^research:\s*(?:\n(?:[ \t]+-[^\n]*)+)?\n?",
            block,
            fm,
            count=1,
            flags=re.M,
        )
        if n != 1:
            raise SystemExit("research replace failed")
        return fm
    # insert before user_groups if present, else before closing
    if re.search(r"^user_groups:", fm, re.M):
        return re.sub(r"^user_groups:", block + "user_groups:", fm, count=1, flags=re.M)
    return fm.rstrip() + "\n" + block


def main() -> None:
    for d in sorted(ROOT.iterdir()):
        if d.name not in MAP:
            raise SystemExit(f"unmapped author: {d.name}")
        f = d / "_index.md"
        text = f.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) < 3:
            raise SystemExit(f"bad front matter: {d.name}")
        fm = set_or_insert_research(parts[1], MAP[d.name])
        f.write_text(f"---{fm}---{parts[2]}", encoding="utf-8", newline="\n")
        print(d.name, "->", ", ".join(MAP[d.name]))


if __name__ == "__main__":
    main()
