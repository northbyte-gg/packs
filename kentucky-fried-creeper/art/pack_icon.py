"""pack.png: the Bucket of Creeper at 3x on a white plate, 64x64."""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from pixelart import load_script, rgba  # noqa: E402

OUTPUT = "pack.png"


def render():
    _, bucket = load_script(Path(__file__).with_name("bucket_of_creeper.py"))
    img = Image.new("RGBA", (64, 64), rgba("#c8201e"))
    for y in range(2, 62):
        for x in range(2, 62):
            img.putpixel((x, y), rgba("#f4f0e8"))
    big = bucket.resize((48, 48), Image.Resampling.NEAREST)
    img.alpha_composite(big, (8, 8))
    return img
