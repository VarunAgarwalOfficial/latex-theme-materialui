#!/usr/bin/env python3
"""Check that every text colour in theme.sty reads on its background.

Reads the colours and the places they are used straight from theme.sty, works
out each text and background pair (with xcolor's mixing rules), and fails if
any pair is under 4.5:1, the WCAG 2.2 AA level for body text.

Run: python3 contrast.py
"""

import re
import sys
from pathlib import Path

MINIMUM = 4.5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Colours a box can be made with. materialLightGrey is a background shade,
# not a box colour, so it is left out.
BOX_COLOURS = [
    "materialBlue",
    "materialIndigo",
    "materialGreen",
    "materialOrange",
    "materialRed",
    "materialGrey",
    "materialDarkGrey",
]


def luminance(rgb):
    def channel(value):
        c = value / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def mix(colour, percent, other):
    """xcolor's colour!percent!other: percent of colour, the rest other."""
    return tuple(c * percent / 100 + o * (100 - percent) / 100 for c, o in zip(colour, other))


def parse(theme):
    colours = {}
    for name, value in re.findall(r"\\definecolor\{(\w+)\}\{HTML\}\{([0-9A-Fa-f]{6})\}", theme):
        colours[name] = tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))
    return colours


def resolve(spec, colours, box=None):
    """Turn an xcolor spec like name, name!30 or #3!55!black into RGB."""
    parts = spec.split("!")
    base = colours[box] if parts[0] == "#3" else colours[parts[0]]
    if len(parts) == 1:
        return base
    other = WHITE
    if len(parts) == 3:
        other = BLACK if parts[2] == "black" else colours[parts[2]]
    return mix(base, float(parts[1]), other)


def one(pattern, theme):
    found = re.search(pattern, theme)
    if not found:
        sys.exit(f"contrast.py: theme.sty no longer matches {pattern!r}")
    return found.group(1)


def pairs(theme, colours):
    on_white = [
        ("link colour", one(r"\blinkcolor=([\w!#]+)", theme)),
        ("url colour", one(r"\burlcolor=([\w!#]+)", theme)),
        ("menu colour", one(r"\bmenucolor=([\w!#]+)", theme)),
        ("code keywords", one(r"keywordstyle=\\color\{([\w!#]+)\}", theme)),
        ("code comments", one(r"commentstyle=\\color\{([\w!#]+)\}", theme)),
        ("code strings", one(r"stringstyle=\\color\{([\w!#]+)\}", theme)),
        ("option names", one(r"\\textcolor\{([\w!#]+)\}\{#2\}", theme)),
    ]
    for label, spec in on_white:
        yield label, resolve(spec, colours), WHITE

    title = one(r"frametitlefont=\\bfseries\\color\{([\w!#]+)\}", theme)
    title_bg = one(r"frametitlebackgroundcolor=([\w!#]+)", theme)
    body_bg = one(r"\bbackgroundcolor=([\w!#]+)", theme)
    for box in BOX_COLOURS:
        yield f"{box} box title", resolve(title, colours, box), resolve(title_bg, colours, box)
        yield f"{box} box text", BLACK, resolve(body_bg, colours, box)


def main():
    theme = Path(__file__).with_name("theme.sty").read_text()
    colours = parse(theme)
    failed = []
    lowest = None
    for label, text, background in pairs(theme, colours):
        value = ratio(text, background)
        mark = "ok  " if value >= MINIMUM else "FAIL"
        print(f"{mark} {value:5.2f}:1  {label}")
        if value < MINIMUM:
            failed.append(label)
        if lowest is None or value < lowest[0]:
            lowest = (value, label)
    print(f"Lowest: {lowest[0]:.2f}:1 ({lowest[1]}). Needed: {MINIMUM}:1.")
    if failed:
        sys.exit(f"{len(failed)} pair(s) under {MINIMUM}:1")


if __name__ == "__main__":
    main()
