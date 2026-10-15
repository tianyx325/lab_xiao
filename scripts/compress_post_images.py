"""One-shot: compress oversized JPEGs in a page bundle for faster Hugo/browser load."""
from pathlib import Path
from PIL import Image

ROOT = Path(r"content/post/South Wutai, Zhongnan Mountains")
EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def compress(path: Path, max_side: int, quality: int) -> None:
    before = path.stat().st_size
    with Image.open(path) as im0:
        im = im0.convert("RGB")
        w, h = im.size
        scale = min(1.0, max_side / max(w, h))
        if scale < 1.0:
            im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        out = path if path.suffix.lower() in {".jpg", ".jpeg"} else path.with_suffix(".jpg")
        tmp = out.with_suffix(".tmp.jpg")
        im.save(tmp, "JPEG", quality=quality, optimize=True, progressive=True)
        after = tmp.stat().st_size
        tmp.replace(out)
        if out != path and path.exists():
            path.unlink()
    print(f"{path.name}: {before/1024:.0f}KB -> {after/1024:.0f}KB")


def main() -> None:
    files = sorted(p for p in ROOT.rglob("*") if p.suffix.lower() in EXTS)
    print(f"found {len(files)} images under {ROOT}")
    for p in files:
        name = p.name.lower()
        max_side = 1200 if "featured" in name else 1600
        quality = 78 if "featured" in name else 80
        try:
            compress(p, max_side, quality)
        except Exception as e:
            print(f"FAIL {p}: {e}")


if __name__ == "__main__":
    main()
