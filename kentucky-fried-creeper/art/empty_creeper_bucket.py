import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _bucket import PALETTE, body_rows  # noqa: E402
from pixelart import grid  # noqa: E402

OUTPUT = "assets/fried_creeper/textures/item/empty_creeper_bucket.png"


def render():
    return grid(PALETTE, [
        "................",
        "................",
        "................",
        ".oooooooooooooo.",
    ] + ["oiiiiiiiiiiiiiio"] + body_rows()[1:])
