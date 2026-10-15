#!/usr/bin/env python3
"""Sync Hugo native identity fields from params.lab (single source of truth).

Writes:
  - config/_default/hugo.yaml          → title
  - config/_default/languages.yaml     → zh.title, zh.params.description
  - config/_default/params.yaml        → marketing.seo.org_name/description,
                                         footer.copyright.notice

Usage:
  py -3 scripts/sync_lab_identity.py
  py -3 scripts/sync_lab_identity.py --dry-run
  py -3 scripts/sync_lab_identity.py --root .
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _load_lab(params_text: str) -> dict[str, str]:
    """Parse top-level lab: scalar keys (name, org_*, email, seo_description, …)."""
    m = re.search(r"(?m)^lab:\n((?:(?:[ \t]+.*)?\n)*)", params_text)
    if not m:
        raise SystemExit("params.yaml: could not find lab: block")
    block = m.group(1)
    lab: dict[str, str] = {}
    for line in block.splitlines():
        if re.match(r"^[ \t]{2}[a-z_]+:", line) and not line.strip().startswith("#"):
            km = re.match(r"^[ \t]{2}([a-z_]+):\s*(.*)$", line)
            if not km:
                continue
            key, raw = km.group(1), km.group(2).strip()
            if raw == "" or raw.startswith("|") or raw.startswith(">") or raw.startswith("["):
                continue
            if (raw.startswith("'") and raw.endswith("'")) or (
                raw.startswith('"') and raw.endswith('"')
            ):
                raw = raw[1:-1]
            lab[key] = raw
    for req in ("name", "org_name", "org_url", "seo_description"):
        if req not in lab or not lab[req]:
            raise SystemExit(f"params.yaml lab.{req} is required")
    return lab


def _replace_line_value(text: str, key_pattern: str, new_value: str, *, quoted: bool = False) -> str:
    """Replace `key: old` value on a matching line; preserve key indentation."""
    if quoted:
        repl = rf"\1'{_yaml_escape(new_value)}'"
    else:
        repl = rf"\1{new_value}"
    new_text, n = re.subn(
        rf"(?m)^([ \t]*{key_pattern}:\s*).*$",
        repl,
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"failed to update key matching /{key_pattern}/ (matches={n})")
    return new_text


def _yaml_escape(s: str) -> str:
    return s.replace("'", "''")


def _footer_notice(lab: dict[str, str]) -> str:
    return lab["name"]


def sync(root: Path, *, dry_run: bool) -> None:
    cfg = root / "config" / "_default"
    params_path = cfg / "params.yaml"
    hugo_path = cfg / "hugo.yaml"
    lang_path = cfg / "languages.yaml"

    params = params_path.read_text(encoding="utf-8")
    lab = _load_lab(params)
    notice = _footer_notice(lab)

    # --- params.yaml: marketing + footer (derived) ---
    new_params = params
    new_params = _replace_line_value(new_params, r"org_name", lab["name"], quoted=True)
    # First org_name under marketing.seo — but lab also has org_name.
    # Replace carefully: marketing block has org_name after site_type.
    # Re-read approach: replace marketing.seo fields by anchored context.

    # Reset and do context-aware replacements
    new_params = params

    def repl_marketing_org(text: str) -> str:
        pattern = (
            r"(marketing:\s*\n(?:[ \t]+.*\n)*?[ \t]+seo:\s*\n"
            r"(?:[ \t]+.*\n)*?[ \t]+org_name:\s*)([^\n]*)"
        )
        out, n = re.subn(
            pattern,
            rf"\1'{_yaml_escape(lab['name'])}'",
            text,
            count=1,
        )
        if n != 1:
            raise SystemExit(f"marketing.seo.org_name update failed (n={n})")
        return out

    def repl_marketing_desc(text: str) -> str:
        pattern = (
            r"(marketing:\s*\n(?:[ \t]+.*\n)*?[ \t]+seo:\s*\n"
            r"(?:[ \t]+.*\n)*?[ \t]+description:\s*)([^\n]*)"
        )
        out, n = re.subn(
            pattern,
            rf"\1'{_yaml_escape(lab['seo_description'])}'",
            text,
            count=1,
        )
        if n != 1:
            raise SystemExit(f"marketing.seo.description update failed (n={n})")
        return out

    def repl_footer_notice(text: str) -> str:
        pattern = r"([ \t]+notice:\s*)([^\n]*)"
        # Only the footer.copyright.notice — find footer: then notice
        fm = re.search(
            r"footer:\s*\n(?:[ \t]+.*\n)*?[ \t]+copyright:\s*\n(?:[ \t]+.*\n)*?[ \t]+notice:\s*[^\n]*",
            text,
        )
        if not fm:
            raise SystemExit("footer.copyright.notice not found")
        chunk = fm.group(0)
        new_chunk, n = re.subn(
            pattern,
            rf"\1'{_yaml_escape(notice)}'",
            chunk,
            count=1,
        )
        if n != 1:
            raise SystemExit("footer notice replace failed")
        return text[: fm.start()] + new_chunk + text[fm.end() :]

    new_params = repl_marketing_org(new_params)
    new_params = repl_marketing_desc(new_params)
    new_params = repl_footer_notice(new_params)

    # --- hugo.yaml title ---
    hugo = hugo_path.read_text(encoding="utf-8")
    new_hugo, n = re.subn(
        r"(?m)^(title:\s*).*$",
        rf"\1{lab['name']} # Website name (synced from lab.name)",
        hugo,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"hugo.yaml title update failed (n={n})")

    # --- languages.yaml ---
    lang = lang_path.read_text(encoding="utf-8")
    new_lang, n = re.subn(
        r"(?m)^([ \t]+title:\s*).*$",
        rf"\1{lab['name']}",
        lang,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"languages.yaml title update failed (n={n})")
    new_lang, n = re.subn(
        r"(?m)^([ \t]+description:\s*).*$",
        rf"\1{lab['seo_description']}",
        new_lang,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"languages.yaml description update failed (n={n})")

    changes = [
        ("params.yaml", params != new_params),
        ("hugo.yaml", hugo != new_hugo),
        ("languages.yaml", lang != new_lang),
    ]
    for name, changed in changes:
        print(f"{'[dry-run] ' if dry_run else ''}{name}: {'changed' if changed else 'unchanged'}")

    if dry_run:
        safe = notice.replace("\u00a9", "(c)")
        print("footer notice would be:")
        print(f"  {safe}")
        return

    if params != new_params:
        params_path.write_text(new_params, encoding="utf-8", newline="\n")
    if hugo != new_hugo:
        hugo_path.write_text(new_hugo, encoding="utf-8", newline="\n")
    if lang != new_lang:
        lang_path.write_text(new_lang, encoding="utf-8", newline="\n")
    print("sync_lab_identity: done")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    sync(args.root.resolve(), dry_run=args.dry_run)


if __name__ == "__main__":
    main()
