#!/usr/bin/env python3
"""WANTED poster meme for gta6-meme-x-01. Rendered in-session, PIL only."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
CREAM = (247, 240, 220)
INK = (24, 20, 26)
MAGENTA = (199, 24, 120)
MAGENTA_D = (169, 16, 100)
GREEN = (18, 128, 60)
GREY = (90, 84, 78)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---- outer frame
d.rectangle([18, 18, W - 18, H - 18], outline=INK, width=6)
d.rectangle([34, 34, W - 34, H - 34], outline=INK, width=2)

# ---- top black bar
d.rectangle([34, 34, W - 34, 128], fill=INK)
ghost = Image.open("assets/mark-1024.png").convert("RGBA")
g_small = ghost.resize((84, 84))
img.paste(g_small, (52, 40), g_small)
d.text((152, 56), "LEONIDA BOUNTY OFFICE", font=F(SANS_B, 34), fill=(255, 255, 255))
d.text((152, 94), "VICE CITY  •  EST. 2013", font=F(SANS, 20), fill=(220, 200, 210))
t = "POSTER No. 13-VI"
tw = d.textlength(t, font=F(MONO_B, 22))
d.text((W - 54 - tw, 62), t, font=F(MONO_B, 22), fill=(255, 255, 255))

# ---- WANTED
t = "WANTED"
f = F(SERIF_B, 150)
tw = d.textlength(t, font=f)
d.text(((W - tw) / 2, 138), t, font=f, fill=INK)
t = "DEAD OR DELAYED"
f = F(SANS_B, 44)
tw = d.textlength(t, font=f)
d.text(((W - tw) / 2, 302), t, font=f, fill=MAGENTA)

# ---- suspect line
t = "GRAND THEFT AUTO VI"
f = F(SERIF_B, 58)
tw = d.textlength(t, font=f)
d.text(((W - tw) / 2, 362), t, font=f, fill=INK)
d.line([70, 448, W - 70, 448], fill=INK, width=3)

# ---- charge sheet (left) + mugshot ghost (right)
items = [
    ("CRIME", "Stealing 13 years of our lives"),
    ("TIME STOLEN", "4,811 days  •  since Sep 17, 2013"),
    ("LAST SEEN", "In trailers only — 87 sightings"),
    ("ESCAPED TWICE", "Fall 2025  •  May 2026"),
    ("ACCOMPLICES", "Jason & Lucia — still at large"),
]
y = 472
for label, val in items:
    d.text((70, y), label, font=F(SANS_B, 21), fill=GREY)
    d.text((70, y + 26), val, font=F(SANS_B, 27), fill=INK)
    y += 76

# mugshot box
box = [748, 462, 1010, 724]
d.rectangle(box, outline=INK, width=4, fill=(238, 232, 214))
for i, hlabel in enumerate(["6'0\"", "5'6\"", "5'0\"", "4'6\""]):
    yy = 486 + i * 56
    d.line([748, yy, 786, yy], fill=INK, width=3)
    d.text((752, yy - 24), hlabel, font=F(MONO, 15), fill=GREY)
g_big = ghost.resize((196, 196))
img.paste(g_big, (788, 486), g_big)
d.rectangle([748, 682, 1010, 724], fill=INK)
t = "SUSPECT: EVERYWHERE"
tw = d.textlength(t, font=F(MONO_B, 18))
d.text((748 + (262 - tw) / 2, 693), t, font=F(MONO_B, 18), fill=(255, 255, 255))

# ---- CAPTURED stamp (rotated)
stamp = Image.new("RGBA", (520, 118), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rounded_rectangle([6, 6, 514, 112], radius=14, outline=(200, 30, 40, 255), width=7)
t = "CAPTURED NOV 19, 2026"
f = F(SANS_B, 31)
tw = sd.textlength(t, font=f)
sd.text(((520 - tw) / 2, 40), t, font=f, fill=(200, 30, 40, 255))
stamp = stamp.rotate(5, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (462, 676), stamp)

# ---- bottom magenta banner
d.rectangle([34, 862, W - 34, H - 34], fill=MAGENTA)
g_med = ghost.resize((150, 150))
img.paste(g_med, (58, 884), g_med)
d.text((228, 884), "REWARD PAID BY MY AI AGENT", font=F(SANS_B, 37), fill=(255, 255, 255))
d.text((228, 930), "with real money it earned winning bounties on", font=F(SANS, 25), fill=(255, 235, 245))
# make.fun pill
pill = [228, 968, 512, 1032]
d.rounded_rectangle(pill, radius=32, fill=(255, 255, 255))
t = "make.fun"
f = F(SANS_B, 40)
tw = d.textlength(t, font=f)
d.text((228 + (284 - tw) / 2, 979), t, font=f, fill=INK)
d.text((536, 984), "This poster IS a bounty.\nMy agent just collected it.", font=F(SANS_B, 24), fill=(255, 255, 255))

img.save("meme/wanted-gta6.png")
print("saved meme/wanted-gta6.png", img.size)
