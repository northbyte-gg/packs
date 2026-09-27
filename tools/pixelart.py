"""Shared helpers for texture scripts under <pack>/art/.

A texture script is a Python module with two names:

    OUTPUT = "assets/<ns>/textures/item/<name>.png"   # path inside the pack
    def render() -> PIL.Image.Image                     # the texture, RGBA

Most scripts build their image with grid(): a palette of single characters and a list of rows,
one character per pixel. "." is always transparent.
"""

import importlib.util
import io
from pathlib import Path

from PIL import Image

TRANSPARENT = (0, 0, 0, 0)


def rgba(value):
    """'#rrggbb' or '#rrggbbaa' -> (r, g, b, a)."""
    v = value.lstrip("#")
    if len(v) == 6:
        v += "ff"
    return tuple(int(v[i:i + 2], 16) for i in (0, 2, 4, 6))


def grid(palette, rows):
    """Render rows of palette characters into an RGBA image. Every row must be the same width."""
    width = len(rows[0])
    for i, row in enumerate(rows):
        if len(row) != width:
            raise ValueError(f"row {i} is {len(row)} wide, expected {width}")
    img = Image.new("RGBA", (width, len(rows)), TRANSPARENT)
    colours = {k: rgba(v) for k, v in palette.items()}
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == ".":
                continue
            if ch not in colours:
                raise ValueError(f"row {y} col {x}: {ch!r} is not in the palette")
            img.putpixel((x, y), colours[ch])
    return img


def png_bytes(img):
    """Encode deterministically: no metadata, fixed compression."""
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=False, compress_level=9)
    return buf.getvalue()


def same_pixels(a, b):
    return a.size == b.size and a.convert("RGBA").tobytes() == b.convert("RGBA").tobytes()


def load_script(path):
    """Import one art script and return (OUTPUT, image)."""
    path = Path(path)
    spec = importlib.util.spec_from_file_location(f"art_{path.stem}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    img = mod.render().convert("RGBA")
    return mod.OUTPUT, img


def art_scripts(pack):
    return sorted(p for p in (Path(pack) / "art").glob("*.py") if not p.name.startswith("_"))
