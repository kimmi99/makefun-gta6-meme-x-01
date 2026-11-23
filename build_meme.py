#!/usr/bin/env python3
"""Build the WANTED-poster meme for make.fun's gta6-meme-x-01 bounty.

Rendered programmatically with Pillow (crisp text at the judge's 480px view,
which AI image generators cannot do). Uses make.fun's official ghost mark
(mark-1024.png, from https://make.fun/press/) as the mascot in the scene:
mugshot suspect, bounty-office clerk and reward payer.

Concept, from a live top-10 teardown on 2026-11-23: every leading entry was
a Leonida *bill for waiting* (receipt / citation / hospital bill / boarding
pass). Nobody used a WANTED poster, and "bounty" is make.fun's own mechanic,
so here the pitch is the joke: the reward for capturing GTA VI was paid by
my AI agent, with money it earned on make.fun.

Run: python3 build_meme.py  ->  meme.png (1080x1080)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
W = H = 1080
CREAM = (247, 240, 220)
INK = (24, 20, 26)
MAGENTA = (199, 24, 120)
RED = (200, 30, 40)
GREY = (90, 84, 78)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def centred(d, y, text, font, fill):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    ghost = Image.open(HERE / "mark-1024.png").convert("RGBA")

    # Frame
    d.rectangle([18, 18, W - 18, H - 18], outline=INK, width=6)
    d.rectangle([34, 34, W - 34, H - 34], outline=INK, width=2)

    # Top black bar: Leonida Bounty Office
    d.rectangle([34, 34, W - 34, 128], fill=INK)
    g = ghost.resize((84, 84))
    img.paste(g, (52, 40), g)
    d.text((152, 56), "LEONIDA BOUNTY OFFICE", font=F(SANS_B, 34), fill=(255, 255, 255))
    d.text((152, 94), "VICE CITY  \u2022  EST. 2013", font=F(SANS, 20), fill=(220, 200, 210))
    t = "POSTER No. 13-VI"
    d.text((W - 54 - d.textlength(t, font=F(MONO_B, 22)), 62), t, font=F(MONO_B, 22), fill=(255, 255, 255))

    # Headline
    centred(d, 138, "WANTED", F(SERIF_B, 150), INK)
    centred(d, 302, "DEAD OR DELAYED", F(SANS_B, 44), MAGENTA)
    centred(d, 362, "GRAND THEFT AUTO VI", F(SERIF_B, 58), INK)
    d.line([70, 448, W - 70, 448], fill=INK, width=3)

    # Charge sheet: the anchors every winning entry shares
    items = [
        ("CRIME", "Stealing 13 years of our lives"),
        ("TIME STOLEN", "4,811 days  \u2022  since Sep 17, 2013"),
        ("LAST SEEN", "In trailers only \u2014 87 sightings"),
        ("ESCAPED TWICE", "Fall 2025  \u2022  May 2026"),
        ("ACCOMPLICES", "Jason & Lucia \u2014 still at large"),
    ]
    y = 472
    for label, val in items:
        d.text((70, y), label, font=F(SANS_B, 21), fill=GREY)
        d.text((70, y + 26), val, font=F(SANS_B, 27), fill=INK)
        y += 76

    # Mugshot: the ghost, suspect everywhere
    box = [748, 462, 1010, 724]
    d.rectangle(box, outline=INK, width=4, fill=(238, 232, 214))
    for i, hlabel in enumerate(["6'0\"", "5'6\"", "5'0\"", "4'6\""]):
        yy = 486 + i * 56
        d.line([748, yy, 786, yy], fill=INK, width=3)
        d.text((752, yy - 24), hlabel, font=F(MONO, 15), fill=GREY)
    g = ghost.resize((196, 196))
    img.paste(g, (788, 486), g)
    d.rectangle([748, 682, 1010, 724], fill=INK)
    t = "SUSPECT: EVERYWHERE"
    d.text((748 + (262 - d.textlength(t, font=F(MONO_B, 18))) / 2, 693), t, font=F(MONO_B, 18), fill=(255, 255, 255))

    # CAPTURED stamp, rotated over the poster's lower right
    stamp = Image.new("RGBA", (520, 118), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([6, 6, 514, 112], radius=14, outline=RED + (255,), width=7)
    t = "CAPTURED NOV 19, 2026"
    sd.text(((520 - sd.textlength(t, font=F(SANS_B, 31))) / 2, 40), t, font=F(SANS_B, 31), fill=RED + (255,))
    img.paste(stamp.rotate(5, expand=True, resample=Image.BICUBIC), (462, 676),
              stamp.rotate(5, expand=True, resample=Image.BICUBIC))

    # Bottom magenta banner: the pitch, in the poster's own voice
    d.rectangle([34, 862, W - 34, H - 34], fill=MAGENTA)
    g = ghost.resize((150, 150))
    img.paste(g, (58, 884), g)
    d.text((228, 884), "REWARD PAID BY MY AI AGENT", font=F(SANS_B, 37), fill=(255, 255, 255))
    d.text((228, 930), "with real money it earned winning bounties on", font=F(SANS, 25), fill=(255, 235, 245))
    d.rounded_rectangle([228, 968, 512, 1032], radius=32, fill=(255, 255, 255))
    t = "make.fun"
    d.text((228 + (284 - d.textlength(t, font=F(SANS_B, 40))) / 2, 979), t, font=F(SANS_B, 40), fill=INK)
    d.text((536, 984), "This poster IS a bounty.\nMy agent just collected it.", font=F(SANS_B, 24), fill=(255, 255, 255))

    out = HERE / "meme.png"
    img.save(out)
    print("saved", out, img.size)


if __name__ == "__main__":
    main()
