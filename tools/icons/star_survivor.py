"""별빛 서바이버 — a little star witch stands her ground in a moonlit forest clearing, staff blazing,
crescent moons orbiting her while ghosts, skulls, bats and slimes close in from every side."""
import math
from .common import icon, lg, rg, sparkle, star_path

def ghost(x, y, s, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" filter="url(#sh2)">'
            '<path d="M-30 30 L-30 -6 Q-30 -40 0 -40 Q30 -40 30 -6 L30 30 L20 22 L10 30 L0 22 L-10 30 L-20 22 Z" fill="url(#ghostg)" stroke="#5a6a9a" stroke-width="4" stroke-linejoin="round"/>'
            '<ellipse cx="-10" cy="-8" rx="5" ry="7" fill="#2a2a4a"/><ellipse cx="10" cy="-8" rx="5" ry="7" fill="#2a2a4a"/><ellipse cx="0" cy="8" rx="5" ry="6" fill="#2a2a4a"/></g>')

def skull(x, y, s, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" filter="url(#sh2)">'
            '<path d="M-28 4 Q-30 -36 0 -36 Q30 -36 28 4 Q26 14 16 16 L16 28 L-16 28 L-16 16 Q-26 14 -28 4 Z" fill="#f4eee0" stroke="#6a5a4a" stroke-width="4" stroke-linejoin="round"/>'
            '<circle cx="-11" cy="-6" r="8" fill="#3a1a2a"/><circle cx="11" cy="-6" r="8" fill="#3a1a2a"/><circle cx="-9" cy="-8" r="2.5" fill="#ff5a6a"/><circle cx="13" cy="-8" r="2.5" fill="#ff5a6a"/>'
            '<path d="M-3 6 L0 12 L3 6 Z" fill="#3a1a2a"/><path d="M-8 20 V28 M0 20 V28 M8 20 V28" stroke="#6a5a4a" stroke-width="3"/></g>')

def bat(x, y, s, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" filter="url(#sh2)">'
            '<path d="M0 -4 Q-20 -26 -54 -20 Q-44 -10 -46 4 Q-34 -2 -26 8 Q-18 0 -10 10 Z M0 -4 Q20 -26 54 -20 Q44 -10 46 4 Q34 -2 26 8 Q18 0 10 10 Z" fill="#6a4ab8" stroke="#2a1a5a" stroke-width="4" stroke-linejoin="round"/>'
            '<ellipse cx="0" cy="4" rx="14" ry="16" fill="#8a6ad8" stroke="#2a1a5a" stroke-width="4"/>'
            '<path d="M-10 -10 L-8 -20 L-2 -12 M10 -10 L8 -20 L2 -12" fill="#8a6ad8" stroke="#2a1a5a" stroke-width="3"/>'
            '<circle cx="-5" cy="2" r="3.5" fill="#ffe06a"/><circle cx="5" cy="2" r="3.5" fill="#ffe06a"/></g>')

def slime(x, y, s):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#sh2)">'
            '<path d="M-34 18 Q-36 -30 0 -32 Q36 -30 34 18 Q0 26 -34 18 Z" fill="url(#slimeg)" stroke="#1a7a3a" stroke-width="4"/>'
            '<ellipse cx="-14" cy="-14" rx="7" ry="4" fill="#fff" opacity=".6"/><circle cx="-9" cy="0" r="4.5" fill="#1a3a1a"/><circle cx="9" cy="0" r="4.5" fill="#1a3a1a"/>'
            '<path d="M-6 9 Q0 14 6 9" stroke="#1a3a1a" stroke-width="3" fill="none" stroke-linecap="round"/></g>')

def build():
    defs = (rg("bg", (0, "#3a7a4a"), (.5, "#1e4a2e"), (1, "#0a1e14"), cx=.5, cy=.52, r=.7)
            + rg("aura", (0, "#fff6c0", .85), (.35, "#ffd86a", .4), (1, "#ffd86a", 0))
            + rg("blast", (0, "#ffffff"), (.3, "#fff3a0", .9), (1, "#ffc83a", 0))
            + lg("hat", (0, "#b08aff"), (1, "#5a2ad0")) + lg("robe", (0, "#8a5aff"), (1, "#3a1a9a"))
            + rg("skin", (0, "#ffeedd"), (1, "#f8c8a8"))
            + rg("ghostg", (0, "#ffffff"), (1, "#c8d8ff"), cx=.4, cy=.3)
            + rg("slimeg", (0, "#c8ffb0"), (.6, "#5ad86a"), (1, "#2aa84a"), cx=.4, cy=.3))
    # ring of monsters
    foes = (ghost(78, 120, 1.25, -12) + skull(430, 96, 1.2, 10) + bat(96, 330, 1.1, 14) + slime(424, 400, 1.35)
            + bat(440, 250, .9, -16) + ghost(70, 460, 1.0, 8) + skull(250, 462, 1.05, 0) + slime(180, 64, .9) + bat(330, 50, .75, 8))
    moons = ""
    for i in range(3):
        a = i / 3 * math.tau + .6
        x, y = 256 + math.cos(a) * 118, 270 + math.sin(a) * 88
        moons += f'<g transform="translate({x:.0f} {y:.0f}) rotate({math.degrees(a) + 90:.0f})" filter="url(#glowS)"><path d="M-18 -16 A24 24 0 1 0 18 -16 A18 18 0 1 1 -18 -16 Z" fill="#fff6b0" stroke="#e8b83a" stroke-width="3"/></g>'
    gems = "".join(f'<path d="M{x} {y - 12} L{x + 8} {y} L{x} {y + 12} L{x - 8} {y} Z" fill="{c}" stroke="#fff" stroke-width="2" opacity=".95"/>' for x, y, c in [(150, 400, "#8af0a0"), (360, 170, "#7ae0ff"), (190, 200, "#8af0a0"), (340, 360, "#ff6ab8"), (300, 410, "#8af0a0"), (120, 250, "#7ae0ff")])
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
<g fill="#2a5a36" opacity=".6">{''.join(f'<path d="M{x} {y} l-5 -14 l5 6 l4 -16 l4 16 l5 -6 l-5 14 z"/>' for x, y in [(40, 230), (470, 330), (300, 300), (200, 360), (380, 470), (130, 170), (460, 170)])}</g>
<ellipse cx="256" cy="300" rx="150" ry="110" fill="#fff6c0" opacity=".08"/>
{gems}
{foes}
<!-- nova ring -->
<ellipse cx="256" cy="272" rx="150" ry="112" fill="none" stroke="#e0d0ff" stroke-width="6" opacity=".55"/>
<ellipse cx="256" cy="272" rx="150" ry="112" fill="none" stroke="#fff" stroke-width="2" opacity=".8" stroke-dasharray="4 14"/>
<circle cx="256" cy="272" r="150" fill="url(#aura)"/>
<!-- witch -->
<g transform="translate(250 290)">
  <ellipse cx="0" cy="70" rx="46" ry="12" fill="#000" opacity=".35"/>
  <g filter="url(#sh)">
    <path d="M-46 66 Q-50 0 0 -6 Q50 0 46 66 Z" fill="url(#robe)" stroke="#1a0a4a" stroke-width="6" stroke-linejoin="round"/>
    <circle cx="0" cy="-30" r="38" fill="url(#skin)" stroke="#3a1a2a" stroke-width="6"/>
  </g>
  <path d="M-38 -34 Q-40 -64 -8 -66 Q-30 -50 -38 -34 Z M38 -34 Q40 -64 8 -66 Q30 -50 38 -34 Z" fill="#ffcf6a"/>
  <ellipse cx="-13" cy="-26" rx="6" ry="9" fill="#2a1430"/><ellipse cx="14" cy="-26" rx="6" ry="9" fill="#2a1430"/>
  <circle cx="-11" cy="-30" r="2.6" fill="#fff"/><circle cx="16" cy="-30" r="2.6" fill="#fff"/>
  <path d="M-12 -8 Q0 4 14 -8" stroke="#3a1a2a" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M-16 -2 Q-24 -16 -8 -18" stroke="#3a1a2a" stroke-width="5" fill="none" stroke-linecap="round" opacity="0"/>
  <ellipse cx="-26" cy="-14" rx="8" ry="5" fill="#ff8ab0" opacity=".6"/><ellipse cx="28" cy="-14" rx="8" ry="5" fill="#ff8ab0" opacity=".6"/>
  <g filter="url(#sh2)">
    <ellipse cx="0" cy="-62" rx="62" ry="14" fill="url(#hat)" stroke="#1a0a4a" stroke-width="5"/>
    <path d="M-34 -66 Q-16 -112 14 -148 Q20 -112 36 -66 Z" fill="url(#hat)" stroke="#1a0a4a" stroke-width="5" stroke-linejoin="round"/>
    <path d="M-34 -72 Q0 -62 36 -72 L36 -62 Q0 -52 -34 -62 Z" fill="#ffd24a"/>
  </g>
  <path d="{star_path(14, -150, 14)}" fill="#ffe06a" stroke="#c88a0a" stroke-width="3"/>
  <!-- staff -->
  <path d="M40 40 L98 -70" stroke="#8a5a2a" stroke-width="9" stroke-linecap="round"/>
  <circle cx="40" cy="30" r="12" fill="url(#skin)" stroke="#3a1a2a" stroke-width="4"/>
</g>
<circle cx="350" cy="218" r="70" fill="url(#blast)"/>
<path d="{star_path(350, 218, 26)}" fill="#fff" stroke="#ffd24a" stroke-width="4"/>
<!-- bolts flying out -->
<g stroke-linecap="round">{''.join(f'<path d="M{350 + math.cos(a) * 40:.0f} {218 + math.sin(a) * 40:.0f} L{350 + math.cos(a) * 120:.0f} {218 + math.sin(a) * 120:.0f}" stroke="#fff6c0" stroke-width="7" opacity=".85"/>' for a in [-2.6, -1.6, -.6, .3])}</g>
{moons}
{sparkle(200, 150, .7, "#fff6c0")}{sparkle(470, 470, .5)}{sparkle(40, 40, .5)}
'''
    return icon(defs, art)
