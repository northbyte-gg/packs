"""Texture for the 3D Empty Creeper Bucket (head and hands), laid out as a 32x32 sheet.

Regions, in pixels, as models/item/empty_creeper_bucket_3d.json maps them:
    front     (0, 0)   16x10   striped wall with the creeper face; rim at the bottom
    side      (16, 0)  16x10   striped wall
    cap side  (0, 10)  12x3    the bucket's base, which sits on top when worn
    cap top   (16, 12) 12x12
    inside    (0, 16)  16x16   the dark inside, seen from below
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from _bucket import PALETTE, stripe  # noqa: E402
from pixelart import rgba  # noqa: E402

OUTPUT = "assets/fried_creeper/textures/item/empty_creeper_bucket_3d.png"

FACE = [
    "gggggg",
    "gkkgkk",
    "gkkgkk",
    "ggkkgg",
    "gkkkkg",
    "gkggkg",
]


def render():
    c = {k: rgba(v) for k, v in PALETTE.items()}
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    for ox, face in ((0, True), (16, False)):
        for y in range(10):
            for x in range(16):
                if y in (0, 9):
                    px = c["o"]
                elif face and 5 <= x <= 10 and 2 <= y <= 7:
                    px = c[FACE[y - 2][x - 5]]
                else:
                    px = c[stripe(x + 1)]
                img.putpixel((ox + x, y), px)
    for y in range(10, 13):
        for x in range(12):
            img.putpixel((x, y), c["o"] if y == 10 else c["r"])
    for y in range(12, 24):
        for x in range(16, 28):
            edge = x in (16, 27) or y in (12, 23)
            img.putpixel((x, y), c["o"] if edge else c["r"])
    for y in range(16, 32):
        for x in range(16):
            img.putpixel((x, y), c["i"])
    return img
