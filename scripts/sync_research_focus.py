# -*- coding: utf-8 -*-
"""Add/update research_focus in author front matter from bio (markdown body untouched)."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORS = ROOT / "content" / "authors"


def focus_from_bio(bio: str) -> str:
    bio = re.sub(r"\s+", " ", (bio or "").strip())
    focus = ""
    for prefix in ("研究方向为", "研究方向：", "研究方向:"):
        if bio.startswith(prefix):
            focus = bio[len(prefix) :]
            break
    focus = re.sub(r"[。.]\s*$", "", focus).strip()
    if focus in ("", "待补充"):
        return ""
    return focus


def parse_file(text: str) -> tuple[dict[str, str], str, str] | None:
    """Return (simple scalar fields we care about as raw lines map), full fm, body."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        # also allow ---\r\n
        end = text.find("\n---\r\n", 4)
    if end < 0:
        return None
    fm = text[4:end]
    body = text[end + len("\n---\n") :]
    return {}, fm, body


def upsert_research_focus(fm: str, focus: str) -> str:
    line = f'research_focus: "{focus}"'
    if re.search(r"^research_focus\s*:", fm, re.M):
        return re.sub(r"^research_focus\s*:.*$", line, fm, count=1, flags=re.M)

    lines = fm.splitlines()
    out: list[str] = []
    inserted = False
    for i, ln in enumerate(lines):
        out.append(ln)
        if not inserted and re.match(r"^bio\s*:", ln):
            # bio may be multi-line quoted; if next lines are continuation, skip — our bios are single-line
            out.append(line)
            inserted = True
    if not inserted:
        out2: list[str] = []
        for ln in out:
            if not inserted and re.match(r"^user_groups\s*:", ln):
                out2.append(line)
                inserted = True
            out2.append(ln)
        out = out2
    if not inserted:
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def extract_bio(fm: str) -> str:
    m = re.search(r'^bio:\s*"([^"]*)"', fm, re.M)
    if m:
        return m.group(1)
    m = re.search(r"^bio:\s*(.+)$", fm, re.M)
    if m:
        return m.group(1).strip().strip("'")
    return ""


def main() -> None:
    global AUTHORS
    ap = argparse.ArgumentParser(description="Sync research_focus from bio into author front matter")
    ap.add_argument(
        "--authors",
        type=Path,
        default=ROOT / "content" / "authors",
        help="Authors content directory",
    )
    args = ap.parse_args()
    AUTHORS = args.authors.resolve()

    updated = 0
    skipped = 0
    for path in sorted(AUTHORS.glob("*/_index.md")):
        raw = path.read_text(encoding="utf-8")
        parsed = parse_file(raw)
        if not parsed:
            skipped += 1
            continue
        _, fm, body = parsed
        focus = focus_from_bio(extract_bio(fm))
        if not focus:
            skipped += 1
            continue
        new_fm = upsert_research_focus(fm, focus)
        new_text = f"---\n{new_fm}---\n\n{body.lstrip()}"
        if not new_text.endswith("\n"):
            new_text += "\n"
        if new_text != raw:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"OK {path.parent.name}: {focus}")
        else:
            skipped += 1
    print(f"done updated={updated} skipped={skipped}")


if __name__ == "__main__":
    main()
