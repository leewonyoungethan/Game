"""별빛 브레이커 — a smiling star-ball blazes upward on a comet trail and smashes into a glowing wall of neon bricks,
shards flying, above a neon paddle in a deep-space nebula."""
import math
from .common import icon, lg, rg, sparkle, star_path

COLS = ["#ff4a8a", "#ff8a3a", "#ffd24a", "#5ae07a", "#3ac8ff", "#9a6aff"]

def brick(x, y, w, h, col, gid):
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".35" stop-color="{col}"/><stop offset="1" stop-color="{col}" stop-opacity=".85"/></linearGradient>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{col}" opacity=".35" filter="url(#b6)"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="url(#{gid})" stroke="#fff" stroke-opacity=".55" stroke-width="2.5"/>'
            f'<rect x="{x + 6}" y="{y + 5}" width="{w * .45:.0f}" height="5" rx="2.5" fill="#fff" opacity=".7"/>')

def build():
    defs = (rg("space", (0, "#4a2a9a"), (.55, "#1e1050"), (1, "#080418"), cx=.5, cy=.35, r=.85)
            + rg("neb1", (0, "#ff4a9a", .55), (1, "#ff4a9a", 0)) + rg("neb2", (0, "#3ac8ff", .45), (1, "#3ac8ff", 0))
            + rg("ball", (0, "#ffffff"), (.35, "#fff3a0"), (1, "#ffb21a"), cx=.38, cy=.32)
            + rg("halo", (0, "#fff6c0", .95), (.4, "#ffd24a", .5), (1, "#ff8a2a", 0))
            + lg("trail", (0, "#ffd24a", 0), (.7, "#ffe88a", .55), (1, "#ffffff", .95), x1=0, y1=1, x2=1, y2=0)
            + lg("paddle", (0, "#c8f4ff"), (.5, "#5ad0ff"), (1, "#2a6ad8"))
            + rg("boom", (0, "#ffffff"), (.25, "#fff2a0", .95), (.6, "#ff8a3a", .45), (1, "#ff4a8a", 0)))
    bricks = ""
    bw, bh, gap = 72, 32, 8
    hole = {(3, 3), (3, 4), (2, 3), (3, 2), (4, 3)}
    for r in range(5):
        for c in range(-1, 7):
            if (r, c) in hole: continue
            x = c * (bw + gap) + (r % 2) * 40 - 8
            bricks += brick(x, 34 + r * (bh + gap), bw, bh, COLS[(r + c) % 6], f"br{r}_{c}")
    # impact point
    ix, iy = 268, 176
    shards = ""
    for i, (a, d, s) in enumerate([(-150, 120, 22), (-120, 150, 16), (-80, 140, 20), (-40, 130, 14), (-10, 110, 18), (200, 100, 12), (-60, 190, 12), (-170, 80, 14), (20, 150, 16)]):
        rad = math.radians(a); x = ix + math.cos(rad) * d; y = iy + math.sin(rad) * d * .7
        shards += f'<rect x="{x - s / 2:.0f}" y="{y - s * .3:.0f}" width="{s}" height="{s * .6:.0f}" rx="3" fill="{COLS[i % 6]}" stroke="#fff" stroke-opacity=".6" stroke-width="2" transform="rotate({a * 1.7:.0f} {x:.0f} {y:.0f})"/>'
    art = f'''
<rect width="512" height="512" fill="url(#space)"/>
<ellipse cx="90" cy="360" rx="220" ry="150" fill="url(#neb1)"/><ellipse cx="440" cy="300" rx="200" ry="170" fill="url(#neb2)"/>
<g fill="#fff">{''.join(f'<circle cx="{(i * 89) % 512}" cy="{(i * 61) % 512}" r="{.8 + (i % 3) * .7}" opacity="{.35 + (i % 4) * .15}"/>' for i in range(60))}</g>
<g>{bricks}</g>
<!-- impact -->
<circle cx="{ix}" cy="{iy}" r="120" fill="url(#boom)"/>
<g stroke="#fff6c0" stroke-width="6" stroke-linecap="round" opacity=".9">{''.join(f'<path d="M{ix + math.cos(math.radians(a)) * 54:.0f} {iy + math.sin(math.radians(a)) * 54:.0f} L{ix + math.cos(math.radians(a)) * 96:.0f} {iy + math.sin(math.radians(a)) * 96:.0f}"/>' for a in range(0, 360, 30))}</g>
{shards}
<!-- comet trail -->
<path d="M120 452 Q200 330 {ix - 22} {iy + 66} L{ix + 30} {iy + 70} Q228 360 168 468 Z" fill="url(#trail)" opacity=".9"/>
<g fill="#fff6c0">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}" opacity="{o}"/>' for x, y, r, o in [(150, 420, 5, .8), (180, 380, 4, .7), (130, 400, 3, .6), (210, 330, 4, .8), (240, 300, 3, .6)])}</g>
<!-- star ball -->
<g transform="translate({ix - 6} {iy + 56}) rotate(-12)">
  <circle r="86" fill="url(#halo)"/>
  <path d="{star_path(0, 0, 58, .52)}" fill="url(#ball)" stroke="#c8700a" stroke-width="6" stroke-linejoin="round" filter="url(#sh2)"/>
  <ellipse cx="-12" cy="-2" rx="6" ry="8.5" fill="#3a1a08"/><ellipse cx="14" cy="-2" rx="6" ry="8.5" fill="#3a1a08"/>
  <circle cx="-10" cy="-6" r="2.6" fill="#fff"/><circle cx="16" cy="-6" r="2.6" fill="#fff"/>
  <path d="M-8 12 Q1 22 10 12" stroke="#3a1a08" stroke-width="4.5" fill="#e84a4a" stroke-linecap="round"/>
  <ellipse cx="-26" cy="8" rx="7" ry="4.5" fill="#ff7a5a" opacity=".6"/><ellipse cx="28" cy="8" rx="7" ry="4.5" fill="#ff7a5a" opacity=".6"/>
</g>
<!-- power-up capsule -->
<g transform="translate(410 300) rotate(-18)" filter="url(#sh2)">
  <rect x="-34" y="-16" width="68" height="32" rx="16" fill="#5ae07a" stroke="#fff" stroke-width="4"/>
  <rect x="-34" y="-16" width="34" height="32" rx="16" fill="#3ac8ff"/><rect x="-26" y="-11" width="40" height="6" rx="3" fill="#fff" opacity=".6"/>
  <path d="{star_path(0, 0, 10, .45)}" fill="#fff"/>
</g>
<!-- paddle -->
<ellipse cx="200" cy="476" rx="150" ry="22" fill="#3ac8ff" opacity=".45" filter="url(#b14)"/>
<g filter="url(#sh2)"><rect x="70" y="454" width="250" height="34" rx="17" fill="url(#paddle)" stroke="#fff" stroke-width="4"/></g>
<rect x="92" y="460" width="150" height="8" rx="4" fill="#fff" opacity=".75"/>
<circle cx="92" cy="471" r="9" fill="#ff4a8a"/><circle cx="298" cy="471" r="9" fill="#ff4a8a"/>
{sparkle(430, 420, .8, "#bff4ff")}{sparkle(60, 250, .55)}{sparkle(470, 220, .5, "#ffd8f0")}
'''
    return icon(defs, art)
