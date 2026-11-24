"""꼬마 용 꼬리잡기 — a cute little green dragon slithering toward a shiny apple on a checkered meadow."""
from .common import icon, lg, rg, sparkle

def build():
    defs = (
        lg("sky", (0, "#9ae86a"), (1, "#3a9a3a"))
        + rg("apple", (0, "#ffb0a8"), (.5, "#f0303a"), (1, "#8a0a14"), cx=.35, cy=.3)
        + rg("head", (0, "#d8ffb8"), (.6, "#5ac86a"), (1, "#1e7a3a"), cx=.38, cy=.3)
        + lg("bodyL", (0, "#c8ffa8"), (1, "#3aa852"))
        + lg("horn", (0, "#fff2b0"), (1, "#e8a800"))
        + rg("gem", (0, "#ffffff"), (.5, "#7af0ff"), (1, "#1a8ac8"), cx=.35, cy=.3)
        + rg("appleGlow", (0, "#ffe680", .6), (1, "#ffe680", 0))
    )
    checker = "".join(f'<rect x="{x*64}" y="{y*64}" width="64" height="64" fill="#8ade6a"/>' for x in range(8) for y in range(8) if (x + y) % 2 == 0)
    body = "M60 452 C120 500 200 400 262 424 C330 450 380 470 410 410 C430 370 400 330 372 318"
    spikes = "".join(f'<path d="M{x} {y} l{dx} {dy} l{ex} {ey} Z" fill="url(#horn)" stroke="#8a5a00" stroke-width="4" stroke-linejoin="round"/>'
                     for x, y, dx, dy, ex, ey in [(110, 448, 6, -34, 18, 26), (196, 418, 4, -36, 20, 30), (276, 400, 10, -32, 14, 34), (356, 428, 14, -30, 6, 34), (420, 380, 30, -16, -8, 30)])
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g opacity=".55">{checker}</g>
<!-- apple -->
<circle cx="170" cy="200" r="120" fill="url(#appleGlow)"/>
<g filter="url(#sh)">
  <path d="M170 136 C116 108 76 160 92 214 C106 264 146 282 170 266 C194 282 234 264 248 214 C264 160 224 108 170 136 Z" fill="url(#apple)" stroke="#5a0610" stroke-width="6"/>
</g>
<path d="M170 136 Q172 108 186 90" stroke="#5a3010" stroke-width="9" fill="none" stroke-linecap="round"/>
<path d="M182 108 Q222 84 240 114 Q204 128 182 108 Z" fill="#5ad04a" stroke="#1e7a2a" stroke-width="5" stroke-linejoin="round"/>
<ellipse cx="128" cy="170" rx="14" ry="26" fill="#fff" opacity=".7" transform="rotate(20 128 170)"/>
<!-- body -->
{spikes}
<path d="{body}" fill="none" stroke="#14501e" stroke-width="78" stroke-linecap="round" filter="url(#sh)"/>
<path d="{body}" fill="none" stroke="url(#bodyL)" stroke-width="64" stroke-linecap="round"/>
<path d="{body}" fill="none" stroke="#efffe0" stroke-width="16" stroke-linecap="round" opacity=".5" transform="translate(-2 -14)"/>
<path d="M40 470 l-30 30 l44 -6 Z" fill="url(#horn)" stroke="#8a5a00" stroke-width="5" stroke-linejoin="round"/>
<!-- head facing the apple (to the upper left) -->
<g transform="translate(340 280) rotate(-18)">
  <g fill="url(#horn)" stroke="#8a5a00" stroke-width="5" stroke-linejoin="round"><path d="M10 -56 L40 -118 L44 -50 Z"/><path d="M56 -40 L104 -86 L84 -22 Z"/></g>
  <g filter="url(#sh)"><ellipse cx="20" cy="0" rx="82" ry="70" fill="url(#head)" stroke="#14501e" stroke-width="6"/></g>
  <ellipse cx="-44" cy="20" rx="44" ry="38" fill="#e8ffd0" stroke="#14501e" stroke-width="5"/>
  <circle cx="-66" cy="10" r="5.5" fill="#14501e"/><circle cx="-48" cy="4" r="5.5" fill="#14501e"/>
  <path d="M-70 42 Q-48 58 -22 44" stroke="#14501e" stroke-width="6" fill="none" stroke-linecap="round"/>
  <ellipse cx="-4" cy="-18" rx="19" ry="22" fill="#fff" stroke="#14501e" stroke-width="5"/><ellipse cx="44" cy="-20" rx="17" ry="20" fill="#fff" stroke="#14501e" stroke-width="5"/>
  <circle cx="-10" cy="-18" r="10" fill="#1a2a1a"/><circle cx="38" cy="-20" r="9" fill="#1a2a1a"/>
  <circle cx="-6" cy="-23" r="4" fill="#fff"/><circle cx="42" cy="-25" r="3.5" fill="#fff"/>
  <ellipse cx="68" cy="16" rx="14" ry="8" fill="#ff7a9a" opacity=".5"/>
  <path d="M-10 -60 Q30 -78 70 -54" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".4"/>
</g>
<!-- gem -->
<g transform="translate(424 110)" filter="url(#sh2)"><path d="M0 -32 L28 -6 L0 32 L-28 -6 Z" fill="url(#gem)" stroke="#0a4a7a" stroke-width="5" stroke-linejoin="round"/><path d="M-28 -6 H28" stroke="#0a4a7a" stroke-width="3" opacity=".5"/></g>
{sparkle(424, 104, .9)}{sparkle(250, 120, .6, "#fff6c0")}{sparkle(470, 470, .5)}
'''
    return icon(defs, art)
