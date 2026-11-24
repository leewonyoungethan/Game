"""유성우 피하기 — a little white rocket weaving between blazing meteors in a violet night sky."""
from .common import icon, lg, rg, sparkle, stars

def meteor(x, y, r, ang=50, tail=3.2, hot=False):
    tl = r * tail
    cr = "".join(f'<circle cx="{x + dx * r}" cy="{y + dy * r}" r="{s * r}" fill="#000" opacity=".22"/>' for dx, dy, s in [(-.3, -.2, .22), (.25, .2, .17), (.1, -.45, .12)])
    return (f'<g transform="rotate({ang} {x} {y})"><path d="M{x} {y - r * .95} L{x - tl} {y} L{x} {y + r * .95} Z" fill="url(#tail{"H" if hot else ""})"/></g>'
            f'<circle cx="{x}" cy="{y}" r="{r * 1.25}" fill="url(#heat)"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#rock)" stroke="#3a1a10" stroke-width="{max(2, r * .08)}"/>{cr}'
            f'<path d="M{x - r * .6} {y - r * .45} A{r * .7} {r * .7} 0 0 1 {x - r * .05} {y - r * .78}" stroke="#ffd8b0" stroke-width="{r * .14}" fill="none" stroke-linecap="round" opacity=".7"/>')

def build():
    defs = (lg("sky", (0, "#1a1050"), (.6, "#3a1868"), (1, "#7a2a7a"))
            + rg("neb", (0, "#ff6ab8", .45), (1, "#ff6ab8", 0)) + rg("neb2", (0, "#6ad8ff", .35), (1, "#6ad8ff", 0))
            + rg("rock", (0, "#e8b48a"), (.6, "#a8644a"), (1, "#5a2a1a"), cx=.35, cy=.3)
            + rg("heat", (0, "#ffb44a", .55), (1, "#ff6a2a", 0))
            + lg("tail", (0, "#ff7a2a", 0), (.6, "#ffa24a", .6), (1, "#fff0a0", .95), x1=0, y1=0, x2=1, y2=0)
            + lg("tailH", (0, "#6ad8ff", 0), (.6, "#8af0ff", .6), (1, "#ffffff", .95), x1=0, y1=0, x2=1, y2=0)
            + lg("body", (0, "#b8c4ff"), (.45, "#ffffff"), (1, "#7a88e0"), x1=0, y1=0, x2=1, y2=0)
            + rg("win", (0, "#ffffff"), (.35, "#8af0ff"), (1, "#2a7ad8"), cx=.4, cy=.35)
            + lg("flame", (0, "#ffffff"), (.35, "#ffe06a"), (1, "#ff5a2a", 0), x1=0, y1=0, x2=0, y2=1))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<circle cx="120" cy="140" r="220" fill="url(#neb)"/><circle cx="430" cy="420" r="200" fill="url(#neb2)"/>
{stars(11, 70, area=(0, 0, 512, 512))}
{meteor(400, 110, 46)}{meteor(96, 300, 30)}{meteor(380, 400, 24)}{meteor(190, 70, 16)}{meteor(452, 250, 14, hot=True)}{meteor(70, 470, 18)}
<!-- rocket -->
<g transform="translate(232 286) rotate(-18)">
  <path d="M-22 92 Q0 200 22 92 Z" fill="url(#flame)"/>
  <path d="M-12 92 Q0 150 12 92 Z" fill="#fff" opacity=".9"/>
  <g filter="url(#sh)">
    <path d="M-34 20 L-82 86 L-30 82 Z M34 20 L82 86 L30 82 Z" fill="#ff5a7a" stroke="#7a1030" stroke-width="6" stroke-linejoin="round"/>
    <path d="M0 -120 C52 -78 50 40 38 96 L-38 96 C-50 40 -52 -78 0 -120 Z" fill="url(#body)" stroke="#2a3478" stroke-width="7" stroke-linejoin="round"/>
    <path d="M-38 96 L38 96 L32 112 L-32 112 Z" fill="#4a5ab8" stroke="#2a3478" stroke-width="6" stroke-linejoin="round"/>
    <path d="M0 -120 C18 -106 28 -90 34 -72 L-34 -72 C-28 -90 -18 -106 0 -120 Z" fill="#ff5a7a" stroke="#2a3478" stroke-width="6" stroke-linejoin="round"/>
  </g>
  <circle cx="0" cy="-14" r="30" fill="url(#win)" stroke="#2a3478" stroke-width="7"/>
  <circle cx="-9" cy="-23" r="8" fill="#fff" opacity=".9"/>
  <path d="M-24 -60 Q-30 0 -22 70" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".6"/>
</g>
<!-- near-miss streaks -->
<g stroke="#8af0ff" stroke-width="6" stroke-linecap="round" opacity=".85"><path d="M300 210 l30 -14 M312 236 l40 -16"/></g>
{sparkle(330, 220, .8, "#8af0ff")}{sparkle(470, 60, .55)}{sparkle(40, 120, .5)}
'''
    return icon(defs, art)
