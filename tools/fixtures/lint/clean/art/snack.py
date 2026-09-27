from pixelart import grid

OUTPUT = "assets/fixture/textures/item/snack.png"


def render():
    return grid({"a": "#c87828", "b": "#ffffff"}, [
        "ab",
        "ba",
    ])
