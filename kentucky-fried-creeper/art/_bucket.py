"""The striped bucket shared by bucket_of_creeper, empty_creeper_bucket and pack_icon.

Not a texture script itself (the leading underscore keeps render from running it).
"""

PALETTE = {
    "o": "#3a1010",  # outline
    "r": "#c8201e",  # stripe red
    "w": "#f4f0e8",  # stripe white
    "g": "#5cc14a",  # creeper panel
    "k": "#16300f",  # creeper face
    "i": "#7a1412",  # inside of the empty bucket
}

# Outline half-width per row, from row 4 (the rim) down; the bucket tapers toward the bottom.
_BODY = {5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 4, 13: 4}
_FACE = [
    "gggggggg",
    "gkkggkkg",
    "gkkggkkg",
    "gggkkggg",
    "ggkkkkgg",
    "ggkggkgg",
    "gggggggg",
]


def stripe(col):
    return "w" if ((col - 1) // 2) % 2 == 0 else "r"


def body_rows():
    """Rows 4 to 15 of a 16-wide bucket: rim, striped body with a creeper panel, base."""
    rows = ["o" * 16]
    for y, edge in _BODY.items():
        row = ["."] * 16
        row[edge - 1] = row[16 - edge] = "o"
        for x in range(edge, 16 - edge):
            if 4 <= x <= 11 and 6 <= y <= 12:
                row[x] = _FACE[y - 6][x - 4]
            else:
                row[x] = stripe(x)
        rows.append("".join(row))
    rows.append("....oooooooo....")
    rows.append("................")
    return rows
