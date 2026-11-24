"""개구리 연잎 점프 — a cheerful frog mid-leap between lily pads, fireflies glowing over the pond."""
import math
from .common import icon, lg, rg, sparkle

def pad(cx, cy, r, notch, fill="url(#pad)", flower=None):
    a0, a1 = notch + .3, notch - .3 + 2 * math.pi
    x0, y0 = cx + r * math.cos(a0), cy + r * .82 * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * .82 * math.sin(a1)
    veins = "".join(f'<path d="M{cx} {cy} L{cx + r*.88*math.cos(a0 + i*(a1-a0)/8):.1f} {cy + r*.72*math.sin(a0 + i*(a1-a0)/8):.1f}"/>' for i in range(1, 8))
    fl = ""
    if flower:
        fx, fy = cx + r * .4 * math.cos(notch + math.pi), cy + r * .33 * math.sin(notch + math.pi)
        fl = "".join(f'<ellipse cx="{fx + 10*math.cos(k*math.pi/3):.1f}" cy="{fy + 8*math.sin(k*math.pi/3):.1f}" rx="11" ry="6" fill="{flower}" stroke="#a8306a" stroke-width="2" transform="rotate({k*60} {fx + 10*math.cos(k*math.pi/3):.1f} {fy + 8*math.sin(k*math.pi/3):.1f})"/>' for k in range(6)) + f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="6" fill="#ffd24a"/>'
    return (f'<ellipse cx="{cx+6}" cy="{cy+10}" rx="{r}" ry="{r*.82:.1f}" fill="#02241e" opacity=".45" filter="url(#b6)"/>'
            f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r*.82:.1f} 0 1 1 {x1:.1f} {y1:.1f} Z" fill="{fill}" stroke="#145a2a" stroke-width="5" stroke-linejoin="round"/>'
            f'<g stroke="#ffffff" stroke-opacity=".25" stroke-width="2.5">{veins}</g>'
            f'<ellipse cx="{cx - r*.35:.1f}" cy="{cy - r*.32:.1f}" rx="{r*.3:.1f}" ry="{r*.12:.1f}" fill="#fff" opacity=".3"/>' + fl)

def build():
    defs = (
        lg("water", (0, "#1a7a7a"), (.5, "#0e5560"), (1, "#062e38"))
        + rg("moonGlow", (0, "#e8fff6", .45), (1, "#e8fff6", 0))
        + rg("pad", (0, "#b8ff8a"), (.6, "#56c45c"), (1, "#2a8a3c"), cx=.35, cy=.3)
        + rg("frog", (0, "#c8ff9a"), (.55, "#5ad46a"), (1, "#2a9a3e"), cx=.4, cy=.32)
        + rg("belly", (0, "#ffffff"), (1, "#e8f8c8"), cx=.5, cy=.3)
        + rg("fly", (0, "#fffbd0", .95), (.4, "#fff28a", .5), (1, "#fff28a", 0))
        + lg("trail", (0, "#ffffff", 0), (1, "#ffffff", .5), x1=0, y1=1, x2=1, y2=0)
    )
    waves = "".join(f'<path d="M-10 {y} q30 -10 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0" stroke="#a8fff0" stroke-opacity=".1" stroke-width="3" fill="none"/>' for y in range(30, 520, 46))
    O = 'stroke="#145a2a" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"'
    art = f'''
<rect width="512" height="512" fill="url(#water)"/>
<circle cx="400" cy="70" r="200" fill="url(#moonGlow)"/>
{waves}
<g fill="#032a2e" opacity=".45"><ellipse cx="420" cy="300" rx="30" ry="11" transform="rotate(-20 420 300)"/><path d="M392 310 l-22 -14 l2 24 Z"/><ellipse cx="90" cy="190" rx="24" ry="9" transform="rotate(30 90 190)"/></g>
<g fill="none" stroke="#dffffa" stroke-opacity=".45" stroke-width="3"><ellipse cx="146" cy="404" rx="96" ry="34"/><ellipse cx="146" cy="404" rx="130" ry="48" stroke-opacity=".2"/></g>
{pad(146, 404, 104, -0.6, flower="#ff8ab8")}
{pad(392, 150, 78, 2.4)}
{pad(80, 118, 46, 0.8)}
<!-- jump arc -->
<path d="M170 360 Q250 150 360 150" stroke="url(#trail)" stroke-width="10" fill="none" stroke-dasharray="2 18" stroke-linecap="round"/>
<!-- frog mid-leap -->
<g transform="translate(270 238) rotate(28)">
  <ellipse cx="10" cy="120" rx="54" ry="16" fill="#02241e" opacity=".35" filter="url(#b6)"/>
  <g filter="url(#sh)" {O}>
    <path d="M-40 40 Q-90 70 -104 120 Q-80 112 -62 92 Q-50 76 -30 64 Z" fill="url(#frog)"/>
    <path d="M40 40 Q90 70 104 120 Q80 112 62 92 Q50 76 30 64 Z" fill="url(#frog)"/>
    <path d="M-44 -6 Q-84 -24 -96 -58 Q-74 -50 -58 -36 Z" fill="url(#frog)"/>
    <path d="M44 -6 Q84 -24 96 -58 Q74 -50 58 -36 Z" fill="url(#frog)"/>
    <ellipse cx="0" cy="10" rx="62" ry="68" fill="url(#frog)"/>
    <ellipse cx="0" cy="30" rx="38" ry="40" fill="url(#belly)" stroke-width="0"/>
    <circle cx="-34" cy="-52" r="28" fill="url(#frog)"/><circle cx="34" cy="-52" r="28" fill="url(#frog)"/>
  </g>
  <circle cx="-34" cy="-54" r="19" fill="#fff"/><circle cx="34" cy="-54" r="19" fill="#fff"/>
  <circle cx="-30" cy="-58" r="10" fill="#10201a"/><circle cx="38" cy="-58" r="10" fill="#10201a"/>
  <circle cx="-26" cy="-62" r="4" fill="#fff"/><circle cx="42" cy="-62" r="4" fill="#fff"/>
  <path d="M-26 -14 Q0 10 26 -14" stroke="#145a2a" stroke-width="6" fill="#d8305a" stroke-linecap="round" stroke-linejoin="round"/>
  <ellipse cx="-40" cy="-20" rx="11" ry="6" fill="#ff6a9a" opacity=".5"/><ellipse cx="40" cy="-20" rx="11" ry="6" fill="#ff6a9a" opacity=".5"/>
  <path d="M-30 -20 Q-48 0 -40 30" stroke="#fff" stroke-width="7" fill="none" opacity=".35" stroke-linecap="round"/>
</g>
<!-- fireflies -->
{''.join(f'<circle cx="{x}" cy="{y}" r="{r*3}" fill="url(#fly)"/><circle cx="{x}" cy="{y}" r="{r}" fill="#fffbd0"/>' for x, y, r in [(218, 96, 6), (470, 260, 5), (60, 300, 5), (330, 360, 4), (440, 450, 6), (150, 60, 4)])}
{sparkle(250, 150, .55, "#fffbd0")}{sparkle(470, 380, .5, "#e8fff6")}
'''
    return icon(defs, art)
