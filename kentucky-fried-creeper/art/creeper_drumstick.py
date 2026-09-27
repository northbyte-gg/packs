from pixelart import grid

OUTPUT = "assets/fried_creeper/textures/item/creeper_drumstick.png"

PALETTE = {
    "o": "#4a2a0e",  # outline
    "h": "#f0b450",  # crust highlight
    "c": "#c8781e",  # crust
    "s": "#8c4f12",  # crust shade
    "g": "#4caf3a",  # creeper speck
    "b": "#f2ead8",  # bone
    "d": "#b8ad92",  # bone shade
}


def render():
    return grid(PALETTE, [
        "................",
        "........oooo....",
        "......oohhhco...",
        ".....ohhcgccco..",
        "....ohhccccgcso.",
        "....ohcgccccsso.",
        "...ohccccgccsso.",
        "...occccccccso..",
        "...ocgccccsso...",
        "...osscccssoo...",
        "....ossssoo.....",
        "...obooooo......",
        "..obdo..........",
        "obbdo...........",
        "obddo...........",
        ".oo.............",
    ])
