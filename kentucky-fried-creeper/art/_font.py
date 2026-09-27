"""A 3x5 pixel font, capitals only: just the letters the sign and pack icon spell."""

GLYPHS = {
    "C": ["###", "#..", "#..", "#..", "###"],
    "D": ["##.", "#.#", "#.#", "#.#", "##."],
    "E": ["###", "#..", "##.", "#..", "###"],
    "F": ["###", "#..", "##.", "#..", "#.."],
    "I": ["###", ".#.", ".#.", ".#.", "###"],
    "K": ["#.#", "##.", "#..", "##.", "#.#"],
    "N": ["##.", "#.#", "#.#", "#.#", "#.#"],
    "P": ["##.", "#.#", "##.", "#..", "#.."],
    "R": ["##.", "#.#", "##.", "#.#", "#.#"],
    "T": ["###", ".#.", ".#.", ".#.", ".#."],
    "U": ["#.#", "#.#", "#.#", "#.#", "###"],
    "Y": ["#.#", "#.#", ".#.", ".#.", ".#."],
    " ": ["...", "...", "...", "...", "..."],
}


def text_width(text, scale=1):
    return (len(text) * 4 - 1) * scale


def draw_text(img, x, y, text, colour, scale=1):
    for i, ch in enumerate(text):
        for gy, row in enumerate(GLYPHS[ch]):
            for gx, px in enumerate(row):
                if px == "#":
                    for sy in range(scale):
                        for sx in range(scale):
                            img.putpixel((x + (i * 4 + gx) * scale + sx, y + gy * scale + sy), colour)
