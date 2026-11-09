"""Draw assets/banner.svg: a seodang dog wandering, sitting, and rolling around.

It is an animated SVG, not a GIF, because GitHub can hold GIFs behind a play button.

Run: python assets/build_banner.py   (needs Pillow)
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw

W, H = 200, 64
GROUND_Y = 50
FEET_Y = 60
SECONDS_PER_FRAME = 0.08

COLORS = {
    "K": "#3b2a1e", "Y": "#dca845", "D": "#b57f2a", "L": "#f6e4b8",
    "N": "#1e1a18", "P": "#e86a7a", "B": "#f2709c",
}

RUN_TOP = [
    "...............KK...",
    "..............KDDK..",
    ".............KYYYYKK",
    "KK...........KYNYYYYK",
    "KYK..........KYYYLLNK",
    ".KYKKKKKKKKKKKYLLLLK",
    "..KYYYYYYYYYYYYYKPK.",
    "..KYYYYYYYYYYYYYK.K.",
    "..KYYYYYYYYYYYYYK...",
    "..KYYYLLLLLLLYYYK...",
    "..KYYKKKKKKKKKYYK...",
]
SIT = [
    ".........KK.....",
    "........KDDK....",
    ".......KYYYYKK..",
    ".......KYNYYYYK.",
    ".......KYYYLLNK.",
    "........KYLLPK..",
    ".......KYYYKK...",
    "......KYYYYK....",
    ".....KYYYLLK....",
    "....KYYYYLLK....",
    "....KYYYYLLK....",
    "...KYYYYKYYK....",
    "...KYYYYKYYK....",
    "...KKKKKKKKK....",
]


def sit_with_tail(part):
    rows = list(SIT)
    for j, tail in part.items():
        rows[j] = tail + rows[j][len(tail):]
    return rows


def lie(eye, tail):
    return [
        ".............KK....",
        "............KDDK...",
        "...........KYYYYKK.",
        tail[0] + "...KKKKKKKY" + eye + "YYYYK",
        tail[1] + "KKYYYYYYYYYYYLLNK",
        ".KYYYYYYYYYYYYYLLK.",
        ".KYLYYYYYYYYYYKKK..",
        "..KKKKKKKKKKKKK....",
    ]


def on_back(legs):
    return legs + [
        "..KKKKKKKKKKKKKK.....",
        ".KLLLLLLLLLLLLLLKKKK.",
        ".KLLLLLLLLLLLLLLKYYYK",
        "KYYYYYYYYYYYYYYYKNYLK",
        "KYYYYYYYYYYYYYYYKYYPK",
        ".KKKKKKKKKKKKKKKKKKK.",
    ]


SPRITES = {
    "run0": RUN_TOP + [".KYYK.........KYYK..", "KYYK...........KYYK.", "KKK.............KKK."],
    "run1": RUN_TOP + ["..KYK........KYK....", "..KYK........KYK....", "..KKK........KKK...."],
    "run2": RUN_TOP + ["....KYK....KYK......", ".....KYK..KYK.......", ".....KKK..KKK......."],
    "sit0": sit_with_tail({8: "KK", 9: "KYK", 10: ".KYK"}),
    "sit1": sit_with_tail({11: "KYK", 12: ".KY", 13: "..K"}),
    "lie0": lie("N", ("K", "K")),
    "lie1": lie("N", (".", "K")),
    "nap0": lie("K", ("K", "K")),
    "nap1": lie("K", (".", "K")),
    "ball": [
        "....KKKKKKKK....",
        "..KKYYYYYYYYKK..",
        ".KYYYYYYLLYYYYK.",
        "KYYYNYYLLLLYYYYK",
        "KYYYYYLLLLLYYYYK",
        ".KYYYYYYLLYYYYK.",
        "..KKYYYYYYYYKK..",
        "....KKKKKKKK....",
    ],
    "back0": on_back(["....KK........KK.....", "....KYK......KYK.....", "....KYK......KYK....."]),
    "back1": on_back(["...KK............KK..", "....KYK........KYK...", ".....KYK......KYK...."]),
    "fly0": ["BB.BB", "BBKBB", "BB.BB", "..K.."],
    "fly1": [".B.B.", ".BKB.", ".BKB.", "..K.."],
}
RUN_CYCLE = ("run0", "run1", "run2", "run1")

SEO = ["..#...#", "..#...#", ".#.#.##", "#...#.#", "......#", "......#"]
DANG = ["###.#..", "#...##.", "###.#..", "..###..", "..#.#..", "..###.."]


def draw_hanok(d):
    d.rectangle([18, 45, 92, 49], fill="#9a9a94")  # stone base
    d.rectangle([20, 26, 90, 45], fill="#efe6cf")  # wall
    for x in (20, 37, 54, 72, 89):
        d.rectangle([x, 26, x + 1, 45], fill="#6b4226")
    for x0, x1 in ((24, 34), (76, 86)):  # paper windows
        d.rectangle([x0, 31, x1, 42], fill="#fbf6e6", outline="#6b4226")
        for x in range(x0 + 3, x1, 3):
            d.line([x, 31, x, 42], fill="#a37a4f")
        for y in (35, 38):
            d.line([x0, y, x1, y], fill="#a37a4f")
    d.rectangle([40, 31, 51, 45], fill="#7a4e2d", outline="#3b2a1e")  # doors
    d.rectangle([58, 31, 69, 45], fill="#7a4e2d", outline="#3b2a1e")
    for x in range(6, 105):  # roof with lifted eaves
        t = abs(x - 55) / 49
        top = int(11 + 13 * t**1.6 - 5 * t**10)
        bottom = int(27 - 6 * t**8)
        d.line([x, top, x, bottom], fill="#46545f" if x % 3 else "#37434d")
        d.point([x, bottom], fill="#26303a")
    d.rectangle([24, 9, 86, 11], fill="#26303a")  # ridge
    d.rectangle([21, 7, 25, 10], fill="#26303a")
    d.rectangle([85, 7, 89, 10], fill="#26303a")
    d.rectangle([45, 19, 65, 29], fill="#4a2c17", outline="#2a180c")  # sign
    for rows, gx in ((SEO, 47), (DANG, 56)):
        for j, row in enumerate(rows):
            for i, c in enumerate(row):
                if c == "#":
                    d.point([gx + i, 21 + j], fill="#f6e4b8")


def draw_tree(d):
    d.rectangle([177, 28, 181, GROUND_Y + 1], fill="#6b4226")
    d.line([179, 34, 170, 25], fill="#6b4226", width=2)
    d.ellipse([160, 4, 198, 32], fill="#4f8f4a")
    d.ellipse([166, 3, 190, 18], fill="#62a65a")
    for x, y in ((167, 14), (176, 9), (187, 13), (172, 24), (184, 23), (191, 20)):
        d.rectangle([x, y, x + 2, y + 2], fill="#e8742a")


def draw_background():
    img = Image.new("RGB", (W, H), "#bfe4f2")
    d = ImageDraw.Draw(img)
    for x, y, w in ((110, 7, 22), (136, 14, 14), (4, 5, 12)):  # clouds
        d.rectangle([x, y, x + w, y + 3], fill="#ffffff")
        d.rectangle([x + 3, y - 2, x + w - 4, y], fill="#ffffff")
    for x in range(W):  # far ridges
        y = int(30 + 7 * math.sin(x / 19) + 3 * math.sin(x / 7))
        d.line([x, y, x, GROUND_Y], fill="#8fbf9a")
    draw_tree(d)
    draw_hanok(d)
    d.rectangle([0, GROUND_Y, W, H], fill="#d6b67c")
    d.rectangle([0, GROUND_Y, W, GROUND_Y + 1], fill="#7fb069")
    for x, y in ((8, 55), (31, 61), (64, 57), (96, 62), (141, 56), (170, 61), (192, 55)):
        d.rectangle([x, y, x + 3, y], fill="#c09f63")
    d.rectangle([108, 57, 124, 59], fill="#a33b3b", outline="#3b2a1e")  # books
    d.rectangle([110, 54, 123, 56], fill="#2f6f8f", outline="#3b2a1e")
    d.rectangle([109, 51, 121, 53], fill="#e0b84c", outline="#3b2a1e")
    return img


def timeline():
    """One loop as (sprite, x, lift, flip). The dog starts and ends off screen."""
    frames, n = [], 0

    def go(x0, x1, step=2):
        nonlocal n
        flip = x1 < x0
        for x in range(x0, x1, -step if flip else step):
            frames.append((RUN_CYCLE[n % 4], x, n % 2, flip))
            n += 1

    def jump(x0, x1, length=14, height=16):
        for k in range(length + 1):
            x = round(x0 + (x1 - x0) * k / length)
            frames.append(("run0", x, round(height * math.sin(math.pi * k / length)), x1 < x0))

    def rest(name, x, count, flip, beat=3):
        for k in range(count):
            frames.append((f"{name}{k // beat % 2}", x, 0, flip))

    def still(name, x, count, flip):
        frames.extend((name, x, 0, flip) for _ in range(count))

    go(-22, 40)                      # wander in
    rest("sit", 40, 24, False)       # sit and wag
    go(40, 24)                       # wander back
    still("run1", 24, 6, True)       # look around
    go(24, 84, step=3)               # dash at the books
    jump(84, 128)
    go(128, 146, step=3)
    rest("lie", 146, 12, False)      # flop down
    still("ball", 146, 3, False)     # roll over
    for x in (146, 145, 144, 143, 142, 141):  # wriggle on its back
        rest("back", x, 8, False, beat=2)
    still("ball", 141, 3, False)
    rest("lie", 141, 12, True)       # rolled to face the other way
    still("ball", 141, 3, True)      # and back again
    for x in (142, 143, 144, 145):
        rest("back", x, 8, True, beat=2)
    still("ball", 145, 3, True)
    rest("sit", 145, 24, True)       # sit up
    go(145, 128)
    jump(128, 84)
    go(84, 58)
    rest("nap", 58, 42, True, beat=6)  # nap in the sun
    rest("sit", 58, 12, True)        # wake up
    go(58, -24, step=3)              # off to somewhere else
    return frames


def run_paths(pixels):
    """{color: path} for a grid of colors, merging each row's runs."""
    paths = {}
    for j, row in enumerate(pixels):
        i = 0
        while i < len(row):
            c = row[i]
            end = i
            while end < len(row) and row[end] == c:
                end += 1
            if c:
                paths.setdefault(c, []).append(f"M{i} {j}h{end - i}v1h-{end - i}z")
            i = end
    return "".join(f'<path fill="{c}" d="{"".join(p)}"/>' for c, p in paths.items())


def sprite_svg(rows, flip):
    width = max(len(r) for r in rows)
    grid = []
    for row in rows:
        row = row.ljust(width, ".")
        grid.append([COLORS.get(c) for c in (row[::-1] if flip else row)])
    return run_paths(grid)


def main():
    plan = timeline()
    assert plan[0][1] <= -21 and plan[-1][1] <= -21, "loop must start and end off screen"
    total = len(plan)
    duration = total * SECONDS_PER_FRAME

    background = draw_background()
    px = background.load()
    bg = run_paths([["#%02x%02x%02x" % px[x, y] for x in range(W)] for y in range(H)])

    used = sorted({(name, flip) for name, _, _, flip in plan} | {("fly0", False), ("fly1", False)})
    ids = {key: f"s{i}" for i, key in enumerate(used)}
    defs = "".join(f'<g id="{ids[k]}">{sprite_svg(SPRITES[k[0]], k[1])}</g>' for k in used)

    body = []
    for f, (name, x, lift, flip) in enumerate(plan):
        y = FEET_Y - len(SPRITES[name]) - lift
        a = 2 * math.pi * f / total
        fly_x = round(148 + 36 * math.sin(a)) - 2
        fly_y = round(30 + 8 * math.sin(3 * a)) - 2
        fly = ids[(f"fly{f // 2 % 2}", False)]
        body.append(
            f'<g class="f" style="animation-delay:{f * SECONDS_PER_FRAME:.2f}s">'
            f'<use href="#{fly}" x="{fly_x}" y="{fly_y}"/>'
            f'<use href="#{ids[(name, flip)]}" x="{x}" y="{y}"/></g>'
        )

    # Slight overlap between frames so rounding never leaves a frame with no dog.
    visible = 100 / total + 0.02
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W * 4}" height="{H * 4}" '
        'shape-rendering="crispEdges" role="img">'
        "<title>A dog wandering, sitting, and rolling around in front of a village school</title>"
        f"<style>.f{{visibility:hidden;animation:s {duration:.2f}s step-end infinite}}"
        f"@keyframes s{{0%{{visibility:visible}}{visible:.3f}%{{visibility:hidden}}}}</style>"
        f"<defs>{defs}</defs>{bg}{''.join(body)}</svg>\n"
    )
    path = Path(__file__).with_name("banner.svg")
    path.write_text(svg, encoding="utf-8", newline="\n")
    print(path.name, total, "frames", f"{duration:.1f}s", path.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
