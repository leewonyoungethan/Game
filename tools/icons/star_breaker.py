"""별빛 브레이커 — a glowing ball smashing through jewel-like bricks above a neon paddle."""
from .common import icon, lg, rg, stars, sparkle

ROWS = [("#ff7ab8", "#c42a78"), ("#ffb06a", "#d86a1a"), ("#ffe66a", "#d0a400"), ("#7cf09a", "#22a060"), ("#6ae2ff", "#1a8ac8")]

def build():
    defs = rg("sky", (0, "#3a2a9a"), (.55, "#14104a"), (1, "#05051a"), cx=.5, cy=.15, r=1)
    defs += "".join(lg(f"r{i}", (0, a), (1, b)) for i, (a, b) in enumerate(ROWS))
    defs += lg("metal", (0, "#e6eaf4"), (1, "#7a8098"))
    defs += lg("paddle", (0, "#4fd8ff"), (.5, "#8b5cff"), (1, "#ff6ad5"), x1=0, y1=0, x2=1, y2=0)
    defs += rg("ball", (0, "#ffffff"), (.3, "#d8f8ff"), (.6, "#4fd8ff", .55), (1, "#4fd8ff", 0))
    defs += lg("trail", (0, "#4fd8ff", 0), (1, "#bff4ff", .8), x1=0, y1=1, x2=1, y2=0)
    defs += rg("pglow", (0, "#8b5cff", .6), (1, "#8b5cff", 0))
    bricks, frags = [], []
    gone = {(1, 3), (1, 4), (2, 3), (2, 4), (2, 5), (3, 4), (0, 4)}
    for r in range(5):
        for c in range(6):
            x, y = 40 + c * 74, 70 + r * 40
            if (r, c) in gone: continue
            fill = "url(#metal)" if (r, c) in {(3, 0), (3, 5)} else f"url(#r{r})"
            bricks.append(f'<g filter="url(#sh2)"><rect x="{x}" y="{y}" width="68" height="32" rx="8" fill="{fill}" stroke="#0a0820" stroke-opacity=".45" stroke-width="3"/></g>'
                          f'<rect x="{x+6}" y="{y+5}" width="56" height="7" rx="3.5" fill="#fff" opacity=".45"/>')
            if (r, c) == (2, 1): bricks.append(f'<text x="{x+34}" y="{y+24}" text-anchor="middle" font-size="20" font-weight="900" fill="#fff" font-family="Arial, sans-serif">★</text>')
    # flying fragments from the broken gap
    import random
    rnd = random.Random(5)
    for i in range(14):
        x, y = rnd.uniform(270, 420), rnd.uniform(120, 240)
        c = ROWS[rnd.randrange(5)][0]
        frags.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{rnd.uniform(8,16):.0f}" height="{rnd.uniform(6,10):.0f}" rx="2" fill="{c}" transform="rotate({rnd.uniform(-60,60):.0f} {x:.0f} {y:.0f})" opacity=".9"/>')
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(7, 60, (0, 0, 512, 512), .5, 1.8)}
{''.join(bricks)}
{''.join(frags)}
<path d="M210 430 L346 214" stroke="url(#trail)" stroke-width="26" stroke-linecap="round"/>
<circle cx="346" cy="214" r="64" fill="url(#ball)"/>
<circle cx="346" cy="214" r="22" fill="#fff"/>
<circle cx="338" cy="206" r="7" fill="#fff" opacity=".9"/>
<ellipse cx="236" cy="452" rx="150" ry="40" fill="url(#pglow)"/>
<g filter="url(#sh)"><rect x="130" y="436" width="212" height="30" rx="15" fill="url(#paddle)" stroke="#0a0820" stroke-opacity=".5" stroke-width="3"/></g>
<rect x="146" y="441" width="180" height="7" rx="3.5" fill="#fff" opacity=".55"/>
{sparkle(346, 214, 1.2)}{sparkle(80, 380, .6)}{sparkle(460, 400, .5, "#ffd0f0")}
'''
    return icon(defs, art)
