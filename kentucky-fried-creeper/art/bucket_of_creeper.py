import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _bucket import PALETTE, body_rows  # noqa: E402
from pixelart import grid  # noqa: E402

OUTPUT = "assets/fried_creeper/textures/item/bucket_of_creeper.png"

CHICKEN = {
    "h": "#f0b450",  # crust highlight
    "c": "#c8781e",  # crust
    "s": "#8c4f12",  # crust shade
    "d": "#4a2a0e",  # crust outline
}


def render():
    return grid(PALETTE | CHICKEN, [
        "................",
        "..ddd.....ddd...",
        ".dhhcd.ddhhccd..",
        "dhccccdhhccccsd.",
    ] + body_rows())
