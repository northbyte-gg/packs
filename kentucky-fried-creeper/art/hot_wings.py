from pixelart import grid

OUTPUT = "assets/fried_creeper/textures/item/hot_wings.png"

PALETTE = {
    "o": "#3f1406",  # outline
    "h": "#ff9a3c",  # glaze highlight
    "c": "#e0521a",  # glaze
    "s": "#9c2e0c",  # glaze shade
    "f": "#ffe14a",  # flame speck
}


def render():
    return grid(PALETTE, [
        "................",
        "................",
        "..oooo..........",
        ".ohhcco.........",
        "ohhcfccoo.......",
        "ohccccccso......",
        "ocfcccccsso.....",
        ".osscccssso.....",
        "..ooosssoo......",
        ".....ooooooo....",
        "......ohhccoo...",
        ".....ohcccfcso..",
        ".....ocfccccsso.",
        "......osscccsso.",
        ".......oosssoo..",
        ".........ooooo..",
    ])
