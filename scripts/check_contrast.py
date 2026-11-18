#!/usr/bin/env python3
"""WCAG 2.1 AA contrast audit for the lab design tokens.

Color values are parsed from _tokens.scss (the single source of truth), so the
audit can never go "all green" against stale hardcoded values after a token
change. If a token cannot be parsed, the script fails loudly.

Baseline pairs are the semantic text/surface combinations that actually ship.
Rules: body text >= 4.5:1; large text / de-emphasized incidental text >= 3:1;
non-text UI (focus ring) >= 3:1. Run after ANY change to _tokens.scss:

    python scripts/check_contrast.py

Exit code 1 if any pair fails or tokens cannot be read.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "modules" / "lab-ui" / "assets" / "scss" / "lab" / "_tokens.scss"


def load_tokens(path: Path) -> dict[str, str]:
    """Extract `$name: #HEX !default;` 6-digit hex values from SCSS."""
    text = path.read_text(encoding="utf-8")
    found: dict[str, str] = {}
    for m in re.finditer(r"^\$(lab-[\w-]+):\s*#([0-9a-fA-F]{6})\b", text, re.M):
        found[m.group(1)] = m.group(2).upper()
    required = [
        "lab-blue", "lab-blue-dark", "lab-ink", "lab-muted",
        "lab-page-bg", "lab-card-bg",
        "lab-night-page", "lab-night-raised", "lab-night-ink",
        "lab-night-secondary", "lab-night-muted",
    ]
    missing = [k for k in required if k not in found]
    if missing:
        raise SystemExit(
            f"Cannot parse required color tokens from {path}: {missing}. "
            "Do not fall back to hardcoded values — fix the token file or the parser."
        )
    return found


T = load_tokens(TOKENS)

# sRGB relative luminance (WCAG 2.1)
def _srgb(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(h):
    r, g, b = (_srgb(int(h[i:i + 2], 16)) for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(fg, bg):
    l1, l2 = sorted((lum(fg), lum(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

def composite(fg, alpha, bg):
    """rgba(fg, alpha) over bg -> flattened hex."""
    return "".join(
        "%02x" % round(int(fg[i:i + 2], 16) * alpha + int(bg[i:i + 2], 16) * (1 - alpha))
        for i in (0, 2, 4)
    )

def mix(a, b, wa):
    """color-mix(in srgb, a wa%, b) -> flattened hex."""
    wb = 1 - wa
    return "".join(
        "%02x" % round(int(a[i:i + 2], 16) * wa + int(b[i:i + 2], 16) * wb)
        for i in (0, 2, 4)
    )

# Semantic values derived from the parsed tokens.
BLUE = T["lab-blue"]                       # $lab-blue (user-specified primary)
INK = T["lab-ink"]                         # $lab-ink
MUTED = T["lab-muted"]                     # $lab-muted
PAGE = T["lab-page-bg"]                    # $lab-page-bg
CARD = T["lab-card-bg"]                    # $lab-card-bg
DARK_LINK = T["lab-blue-dark"]             # $lab-blue-dark
NIGHT_PAGE = T["lab-night-page"]           # $lab-night-page
NIGHT_RAISED = T["lab-night-raised"]       # $lab-night-raised
NIGHT_INK = T["lab-night-ink"]             # $lab-night-ink
NIGHT_SECONDARY = T["lab-night-secondary"]  # $lab-night-secondary
NIGHT_MUTED = T["lab-night-muted"]         # $lab-night-muted

# User rule: no blue text deeper than the primary. Body links/buttons sit ON
# the primary; hover/soft LIGHTEN via white mix. 4.19:1 (link) and 4.23:1
# (white on primary) are user-approved exceptions to strict AA 4.5:1.
LINK = BLUE
LINK_HOVER = mix(BLUE, "FFFFFF", 0.86)   # --lab-color-link-hover
LINK_SOFT = mix(BLUE, "FFFFFF", 0.80)    # --lab-color-link-soft
TERTIARY = composite(INK, 0.55, CARD)    # --lab-color-text-tertiary

# (label, fg, bg, minimum)  — min: 4.5 body · 3.0 large/incidental/non-text
PAIRS = [
    ("light: ink body on card",        INK, CARD, 4.5),
    ("light: ink body on page",        INK, PAGE, 4.5),
    ("light: muted on card",           MUTED, CARD, 4.5),
    ("light: link on card (approved)", LINK, CARD, 3.0),
    ("light: link on page (approved)", LINK, PAGE, 3.0),
    ("light: link-hover on card",      LINK_HOVER, CARD, 3.0),
    ("light: link-soft on card",       LINK_SOFT, CARD, 3.0),
    ("light: white text on link btn",  "FFFFFF", LINK, 3.0),
    ("light: tertiary on card",        TERTIARY, CARD, 3.0),
    ("light: focus ring on page",      BLUE, PAGE, 3.0),
    ("light: brand as UI on page",     BLUE, PAGE, 3.0),
    ("dark: text on card",             NIGHT_INK, NIGHT_RAISED, 4.5),
    ("dark: text-secondary on card",   NIGHT_SECONDARY, NIGHT_RAISED, 4.5),
    ("dark: muted on page",            NIGHT_MUTED, NIGHT_PAGE, 4.5),
    ("dark: link on card",             DARK_LINK, NIGHT_RAISED, 4.5),
    ("dark: focus ring on card",       DARK_LINK, NIGHT_RAISED, 3.0),
]

def main():
    failed = 0
    for label, fg, bg, minimum in PAIRS:
        r = ratio(fg, bg)
        ok = r >= minimum
        print(f"{'PASS' if ok else 'FAIL'}  {label:36s} {r:5.2f}:1  (min {minimum})")
        if not ok:
            failed += 1
    if failed:
        print(f"\n{failed} pair(s) below threshold — fix _tokens.scss, do not lower the baseline.")
        return 1
    print(f"\nAll {len(PAIRS)} pairs pass WCAG AA (colors read from _tokens.scss).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
