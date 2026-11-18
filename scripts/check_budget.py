#!/usr/bin/env python3
"""Performance budget check for the built site.

Run after `hugo --minify`. Fails when the shipped CSS/JS exceeds the
agreed limits, so visual effects cannot silently grow the page weight.

    python scripts/check_budget.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")

BUDGETS = {
    "css_kb": 300,              # single wowchemy.css (minified)
    "vendor_js_kb": 185,        # vendor-bundle (jQuery + Bootstrap + instantpage)
    "home_local_js_kb": 240,
    "home_scripts": 16,
    "home_requests": 26,        # scripts + stylesheets + <img> on the homepage
    "largest_home_image_kb": 200,
}


def kb(n):
    return round(n / 1024, 1)


def main():
    css_files = glob.glob(os.path.join(PUBLIC, "css", "wowchemy.*.css"))
    if not css_files:
        print("FAIL: no built CSS found; run hugo --minify first")
        return 1
    css_size = max(os.path.getsize(p) for p in css_files)

    index = os.path.join(PUBLIC, "index.html")
    if not os.path.exists(index):
        print("FAIL: public/index.html missing")
        return 1
    html = open(index, encoding="utf-8", errors="ignore").read()
    srcs = re.findall(r'<script[^>]*src=["\']?([^"\'>\s]+)', html)
    scripts = len(srcs)
    requests = (
        len(srcs)
        + len(re.findall(r'<link[^>]*rel=["\']?stylesheet', html))
        + len(re.findall(r'<img[^>]*src=', html))
    )

    largest_image = 0
    for src in re.findall(r'<img[^>]*src=["\']?([^"\'>\s]+)', html):
        if not src.startswith("/"):
            continue
        path = os.path.join(PUBLIC, src.lstrip("/").split("?")[0])
        if os.path.exists(path):
            largest_image = max(largest_image, os.path.getsize(path))

    local = []
    for src in srcs:
        if not src.startswith("/") or not src.endswith(".js"):
            continue
        path = os.path.join(PUBLIC, src.lstrip("/").split("?")[0])
        if os.path.exists(path):
            local.append(path)

    local_total = sum(os.path.getsize(p) for p in local)
    vendor = [p for p in local if "vendor-bundle" in os.path.basename(p)]
    vendor_size = max((os.path.getsize(p) for p in vendor), default=0)

    checks = [
        ("css", kb(css_size), BUDGETS["css_kb"]),
        ("vendor_js", kb(vendor_size), BUDGETS["vendor_js_kb"]),
        ("home_local_js", kb(local_total), BUDGETS["home_local_js_kb"]),
        ("home_scripts", scripts, BUDGETS["home_scripts"]),
        ("home_requests", requests, BUDGETS["home_requests"]),
        ("largest_home_image", kb(largest_image), BUDGETS["largest_home_image_kb"]),
    ]

    failed = False
    for name, value, limit in checks:
        unit = "" if name in ("home_scripts", "home_requests") else " KB"
        ok = value <= limit
        failed = failed or not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {value}{unit} (limit {limit}{unit})")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())