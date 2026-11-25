"""통통 농구 — a flaming basketball arcs into a glowing hoop under arena spotlights, the net swishing and confetti popping."""
from .common import icon, lg, rg, sparkle, rays

def build():
    defs = (rg("arena", (0, "#7a3ad8"), (.55, "#3a1a7a"), (1, "#140a30"), cx=.5, cy=.25, r=.9)
            + rg("spot", (0, "#fff6d0", .7), (1, "#fff6d0", 0))
            + rg("ball", (0, "#ffd0a0"), (.45, "#ff8a2a"), (1, "#b8400a"), cx=.36, cy=.3)
            + lg("fire", (0, "#fff6a0"), (.4, "#ffb02a"), (1, "#ff3a1a", 0), x1=0, y1=0, x2=1, y2=1)
            + lg("board", (0, "#ffffff", .95), (1, "#d8e4ff", .85))
            + lg("floor", (0, "#f0b070"), (1, "#c8742e"))
            + rg("halo", (0, "#fff2a0", .9), (1, "#ffb02a", 0)))
    confetti = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{w * .5}" rx="2" fill="{c}" transform="rotate({a} {x} {y})"/>'
                       for x, y, w, c, a in [(70, 90, 18, "#ff5a9a", 30), (130, 50, 14, "#5ad8ff", -20), (440, 160, 16, "#ffd24a", 50), (470, 90, 12, "#7af07a", -40),
                                             (40, 200, 12, "#ffd24a", 10), (300, 40, 14, "#ff8a3a", 60), (210, 110, 10, "#c08aff", -30), (480, 230, 12, "#ff5a9a", 20)])
    crowd = "".join(f'<circle cx="{x}" cy="{352 + (x * 7) % 14}" r="15" fill="hsl({(x * 37) % 360} 70% 58%)"/><rect x="{x - 13}" y="{364 + (x * 7) % 14}" width="26" height="30" rx="8" fill="hsl({(x * 37) % 360} 70% 50%)"/>' for x in range(10, 520, 30))
    net = "".join(f'<path d="M{304 + i * 22} 236 L{322 + i * 15} 318"/>' for i in range(7))
    net += "".join(f'<path d="M{306 + j * 4} {256 + j * 20} L{448 - j * 4} {256 + j * 20}"/>' for j in range(4))
    art = f'''
<rect width="512" height="512" fill="url(#arena)"/>
{rays("#ffffff", .06, 14, 256, 0, 700)}
<g>{''.join(f'<ellipse cx="{x}" cy="40" rx="120" ry="160" fill="url(#spot)" opacity=".5"/>' for x in (60, 256, 452))}</g>
<g fill="#fff6d0">{''.join(f'<circle cx="{x}" cy="22" r="8"/>' for x in (60, 158, 256, 354, 452))}</g>
<rect y="330" width="512" height="80" fill="#1e1040"/>
<g opacity=".85">{crowd}</g>
<rect y="400" width="512" height="112" fill="url(#floor)"/>
<g stroke="#a85a20" stroke-width="3" opacity=".35">{''.join(f'<path d="M{x} 400 L{x - 60} 512"/>' for x in range(0, 600, 56))}</g>
<path d="M120 512 Q256 430 512 470" stroke="#fff" stroke-width="7" fill="none" opacity=".8"/>
<!-- hoop -->
<rect x="470" y="150" width="20" height="270" fill="#8a92a8"/>
<g filter="url(#sh2)"><rect x="360" y="70" width="150" height="120" rx="12" fill="url(#board)" stroke="#fff" stroke-width="6"/></g>
<rect x="398" y="118" width="62" height="48" fill="none" stroke="#ff4a2a" stroke-width="7"/>
<circle cx="376" cy="236" r="110" fill="url(#halo)" opacity=".6"/>
<ellipse cx="376" cy="236" rx="78" ry="16" fill="none" stroke="#b82a0a" stroke-width="12"/>
<g stroke="#fff" stroke-width="4" stroke-linecap="round" fill="none" opacity=".95">{net}</g>
<ellipse cx="376" cy="236" rx="78" ry="16" fill="none" stroke="#ff5a2a" stroke-width="10" stroke-dasharray="250 400" stroke-dashoffset="-130"/>
<!-- dotted arc -->
<path d="M70 470 Q120 140 330 176" stroke="#fff" stroke-width="8" stroke-dasharray="2 20" stroke-linecap="round" fill="none" opacity=".75"/>
<!-- flaming ball -->
<g transform="translate(296 186) rotate(-30)">
  <path d="M0 -60 C-90 -40 -170 10 -200 60 C-150 40 -110 50 -80 60 C-120 80 -150 110 -170 140 C-100 100 -40 80 0 60 Z" fill="url(#fire)" opacity=".95"/>
</g>
<g filter="url(#sh)"><circle cx="300" cy="186" r="58" fill="url(#ball)" stroke="#5a1a04" stroke-width="5"/></g>
<g stroke="#4a1404" stroke-width="5" fill="none" stroke-linecap="round">
  <path d="M242 186 H358 M300 128 V244"/><path d="M262 142 Q290 186 262 230"/><path d="M338 142 Q310 186 338 230"/>
</g>
<path d="M266 160 Q276 140 300 136" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round" opacity=".55"/>
{confetti}
{sparkle(220, 290, .8, "#fff6c0")}{sparkle(440, 300, .6)}{sparkle(90, 290, .5)}
'''
    return icon(defs, art)
