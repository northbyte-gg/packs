"""The 4x2 Kentucky Fried Creeper sign: 64x32, 16 px per block like vanilla paintings."""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from _font import draw_text, text_width  # noqa: E402
from pixelart import rgba  # noqa: E402

OUTPUT = "assets/fried_creeper/textures/painting/sign.png"

FRAME = rgba("#3a1010")
RED = rgba("#c8201e")
WHITE = rgba("#f4f0e8")
GREEN = rgba("#3e9a2e")



def render():
    img = Image.new("RGBA", (64, 32), RED)
    for x in range(64):
        for y in (0, 31):
            img.putpixel((x, y), FRAME)
    for y in range(32):
        for x in (0, 63):
            img.putpixel((x, y), FRAME)
    # Top line, white on red
    draw_text(img, (64 - text_width("KENTUCKY FRIED")) // 2, 3, "KENTUCKY FRIED", WHITE)
    # White band with the big green name
    for y in range(10, 23):
        for x in range(1, 63):
            img.putpixel((x, y), WHITE)
    draw_text(img, (64 - text_width("CREEPER", 2)) // 2, 12, "CREEPER", GREEN, scale=2)
    # Bucket stripes along the bottom
    for x in range(1, 63):
        colour = WHITE if (x // 4) % 2 == 0 else RED
        for y in range(25, 31):
            img.putpixel((x, y), colour)
    return img
