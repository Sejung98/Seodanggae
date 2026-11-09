"""Draw assets/banner.gif: a seodang dog playing and reciting the Thousand Character Classic.

Run: python assets/build_banner.py   (needs Pillow)
"""
import math
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw

W, H, SCALE = 200, 64, 4
GROUND_Y = 50
FEET_Y = 60
MS_PER_FRAME = 80

COLORS = {
    "K": "#3b2a1e", "Y": "#dca845", "D": "#b57f2a", "L": "#f6e4b8",
    "N": "#1e1a18", "P": "#e86a7a", "W": "#ffffff",
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
STRETCHED = [
    ".KYYK.........KYYK..",
    "KYYK...........KYYK.",
    "KKK.............KKK.",
]
PASSING = [
    "..KYK........KYK....",
    "..KYK........KYK....",
    "..KKK........KKK....",
]
GATHERED = [
    "....KYK....KYK......",
    ".....KYK..KYK.......",
    ".....KKK..KKK.......",
]
RUN_LEGS = [STRETCHED, PASSING, GATHERED, PASSING]
SIT_BODY = [
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
TAIL_UP = {8: "KK", 9: "KYK", 10: ".KYK"}
TAIL_DOWN = {11: "KYK", 12: ".KY", 13: "..K"}

TIAN = [
    "#########",
    "....#....",
    "....#....",
    "#########",
    "....#....",
    "...#.#...",
    "..#...#..",
    ".#.....#.",
    "#.......#",
]
DI = [
    ".#....#..",
    ".#....#..",
    "###.#####",
    ".#..#.#.#",
    ".#..#.#.#",
    ".#..#.#.#",
    ".#..#.###",
    ".##.#....",
    "##..#####",
]
SEO = ["..#...#", "..#...#", ".#.#.##", "#...#.#", "......#", "......#"]
DANG = ["###.#..", "#...##.", "###.#..", "..###..", "..#.#..", "..###.."]


def stamp(img, rows, x, y, colors=COLORS, flip=False):
    width = max(len(r) for r in rows)
    px = img.load()
    for j, row in enumerate(rows):
        row = row.ljust(width, ".")
        for i, c in enumerate(row[::-1] if flip else row):
            if c != "." and 0 <= x + i < W and 0 <= y + j < H:
                px[x + i, y + j] = ImageColor.getrgb(colors[c])


def glyph(img, rows, x, y, color):
    stamp(img, rows, x, y, {"#": color})


def run_sprite(frame):
    return RUN_TOP + RUN_LEGS[frame % len(RUN_LEGS)]


def sit_sprite(tail_up):
    rows = list(SIT_BODY)
    for j, part in (TAIL_UP if tail_up else TAIL_DOWN).items():
        rows[j] = part + rows[j][len(part):]
    return rows


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
        tile = "#46545f" if x % 3 else "#37434d"
        d.line([x, top, x, bottom], fill=tile)
        d.point([x, bottom], fill="#26303a")
    d.rectangle([24, 9, 86, 11], fill="#26303a")  # ridge
    d.rectangle([21, 7, 25, 10], fill="#26303a")
    d.rectangle([85, 7, 89, 10], fill="#26303a")


def draw_sign(img, d):
    d.rectangle([45, 19, 65, 29], fill="#4a2c17", outline="#2a180c")
    glyph(img, SEO, 47, 21, "#f6e4b8")
    glyph(img, DANG, 56, 21, "#f6e4b8")


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
    draw_sign(img, d)
    d.rectangle([0, GROUND_Y, W, H], fill="#d6b67c")
    d.rectangle([0, GROUND_Y, W, GROUND_Y + 1], fill="#7fb069")
    for x, y in ((8, 55), (31, 61), (64, 57), (96, 62), (141, 56), (170, 61), (192, 55)):
        d.rectangle([x, y, x + 3, y], fill="#c09f63")
    d.rectangle([108, 57, 124, 59], fill="#a33b3b", outline="#3b2a1e")  # books
    d.rectangle([110, 54, 123, 56], fill="#2f6f8f", outline="#3b2a1e")
    d.rectangle([109, 51, 121, 53], fill="#e0b84c", outline="#3b2a1e")
    return img


def timeline():
    """One loop as (sprite, x, y, flip, bubble). The dog starts and ends off screen."""
    frames, n = [], 0

    def run(x0, x1, flip, step=3):
        nonlocal n
        direction = 1 if x1 > x0 else -1
        for x in range(x0, x1, direction * step):
            frames.append((run_sprite(n), x, FEET_Y - 14 - (n % 2), flip, None))
            n += 1

    def jump(x0, x1, flip, length=14, height=16):
        for k in range(length + 1):
            x = round(x0 + (x1 - x0) * k / length)
            lift = round(height * math.sin(math.pi * k / length))
            frames.append((run_sprite(0), x, FEET_Y - 14 - lift, flip, None))

    run(-26, 84, False)
    jump(84, 128, False)
    run(128, 150, False)
    run(150, 128, True, step=2)
    for k in range(40):  # sit and recite the first two characters of the classic
        bubble = TIAN if k < 18 else DI if k >= 20 else None
        frames.append((sit_sprite(k // 2 % 2 == 0), 128, FEET_Y - 14, True, bubble))
    jump(128, 84, True)
    run(84, -26, True)
    return frames


def draw_bubble(img, rows, x, y):
    d = ImageDraw.Draw(img)
    d.rectangle([x, y, x + 14, y + 14], fill="#ffffff", outline="#3b2a1e")
    d.rectangle([x + 6, y + 15, x + 7, y + 16], fill="#3b2a1e")
    glyph(img, rows, x + 3, y + 3, "#1e1a18")


def draw_butterfly(img, f, total):
    a = 2 * math.pi * f / total
    x = round(150 + 34 * math.sin(a))
    y = round(30 + 8 * math.sin(3 * a))
    d = ImageDraw.Draw(img)
    if f % 4 < 2:  # wings open
        d.rectangle([x - 3, y - 2, x - 1, y + 1], fill="#f2709c")
        d.rectangle([x + 1, y - 2, x + 3, y + 1], fill="#f2709c")
    else:  # wings folded
        d.rectangle([x - 1, y - 3, x - 1, y], fill="#f2709c")
        d.rectangle([x + 1, y - 3, x + 1, y], fill="#f2709c")
    d.line([x, y - 1, x, y + 1], fill="#3b2a1e")


def main():
    background = draw_background()
    plan = timeline()
    assert plan[0][1] <= -21 and plan[-1][1] <= -21, "loop must start and end off screen"
    frames = []
    for f, (sprite, x, y, flip, bubble) in enumerate(plan):
        img = background.copy()
        draw_butterfly(img, f, len(plan))
        stamp(img, sprite, x, y, flip=flip)
        if bubble:
            draw_bubble(img, bubble, x - 1, y - 19)
        frames.append(img.resize((W * SCALE, H * SCALE), Image.NEAREST))

    # A frame with the dog and a bubble on screen holds every color in the scene.
    sitting = next(i for i, step in enumerate(plan) if step[4])
    palette = frames[sitting].quantize(colors=64, dither=Image.Dither.NONE)
    out = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    path = Path(__file__).with_name("banner.gif")
    out[0].save(path, save_all=True, append_images=out[1:], duration=MS_PER_FRAME, loop=0, disposal=1)
    print(path.name, len(out), "frames", path.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
