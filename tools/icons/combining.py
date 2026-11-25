"""몬스터 합치기 — above a floating island, a fiery monster and a water monster pour swirling energy
into a glowing egg that cracks open, element orbs orbiting in a twilight sky."""
import math
from .common import icon, lg, rg, sparkle

ELEMS = [("#ff6a3a", "#ffd0a0"), ("#3aa8ff", "#c8ecff"), ("#ffd23a", "#fff6c0"), ("#4ad06a", "#c8ffc0"),
         ("#b07a4a", "#f0d0a8"), ("#5a3a9a", "#c8a8ff"), ("#fff0a0", "#ffffff"), ("#a04ad8", "#e8c0ff")]

def orb(x, y, r, i):
    a, b = ELEMS[i]
    return (f'<radialGradient id="orb{i}" cx=".35" cy=".3" r=".7"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{a}"/></radialGradient>'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r * 1.8:.0f}" fill="{a}" opacity=".25" filter="url(#b6)"/>'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="url(#orb{i})" stroke="#fff" stroke-width="3"/>'
            f'<ellipse cx="{x - r * .3:.0f}" cy="{y - r * .35:.0f}" rx="{r * .35:.0f}" ry="{r * .2:.0f}" fill="#fff" opacity=".8"/>')

def monster(x, y, s, body, belly, dark, flip=1, kind="fire"):
    O = f'stroke="{dark}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    deco = ('<path d="M-20 -66 C-30 -96 -6 -104 0 -124 C10 -104 34 -98 20 -66 Z" fill="url(#flameg)" stroke="#c8301a" stroke-width="5" stroke-linejoin="round"/>'
            if kind == "fire" else
            '<path d="M-6 -70 C-2 -100 26 -112 40 -104 C26 -94 22 -80 18 -66 Z" fill="#7ad8ff" stroke="#1a5aa8" stroke-width="5" stroke-linejoin="round"/>')
    return (f'<g transform="translate({x} {y}) scale({s * flip} {s})" filter="url(#sh)">{deco}'
            f'<path d="M-40 60 Q-58 -60 0 -70 Q58 -60 40 60 Q0 78 -40 60 Z" fill="{body}" {O}/>'
            f'<ellipse cx="0" cy="22" rx="26" ry="30" fill="{belly}"/>'
            f'<path d="M34 -4 Q70 -16 84 -40" stroke="{body}" stroke-width="20" fill="none" stroke-linecap="round"/>'
            f'<path d="M34 -4 Q70 -16 84 -40" {O} fill="none" stroke-width="5" opacity=".0"/>'
            f'<circle cx="86" cy="-42" r="11" fill="{body}" {O}/>'
            f'<path d="M-38 50 L-46 70 M-20 64 L-22 80 M20 64 L22 80" {O} fill="none"/>'
            f'<ellipse cx="-14" cy="-30" rx="11" ry="14" fill="#fff" stroke="{dark}" stroke-width="4"/><ellipse cx="16" cy="-30" rx="11" ry="14" fill="#fff" stroke="{dark}" stroke-width="4"/>'
            f'<circle cx="-11" cy="-27" r="6.5" fill="#1a0a20"/><circle cx="19" cy="-27" r="6.5" fill="#1a0a20"/><circle cx="-9" cy="-30" r="2.5" fill="#fff"/><circle cx="21" cy="-30" r="2.5" fill="#fff"/>'
            f'<path d="M-10 -6 Q2 6 14 -6" stroke="{dark}" stroke-width="5" fill="#fff" stroke-linecap="round"/>'
            f'<ellipse cx="-28" cy="-10" rx="8" ry="5" fill="#ff7aa0" opacity=".5"/><ellipse cx="30" cy="-10" rx="8" ry="5" fill="#ff7aa0" opacity=".5"/></g>')

def build():
    defs = (lg("sky", (0, "#2a1a6a"), (.5, "#7a3ab8"), (1, "#ff8ab8"))
            + rg("core", (0, "#ffffff"), (.25, "#fff0ff", .9), (.6, "#c87aff", .45), (1, "#c87aff", 0))
            + lg("swirlA", (0, "#ff7a3a", 0), (1, "#ffb05a", .95), x1=0, y1=0, x2=1, y2=0)
            + lg("swirlB", (0, "#3ab0ff", .95), (1, "#3ab0ff", 0), x1=0, y1=0, x2=1, y2=0)
            + rg("egg", (0, "#ffffff"), (.6, "#fff4e0"), (1, "#f0d8b8"), cx=.38, cy=.3)
            + lg("grass", (0, "#7ae06a"), (1, "#3aa84a")) + lg("rock", (0, "#a07a5a"), (1, "#5a3a2a"))
            + rg("fireb", (0, "#ffd0a0"), (.6, "#ff7a3a"), (1, "#d8401a"), cx=.38, cy=.3)
            + rg("waterb", (0, "#c8f0ff"), (.6, "#4ab0ff"), (1, "#1a6ad8"), cx=.38, cy=.3)
            + lg("flameg", (0, "#fff3a0"), (1, "#ff5a2a"), x1=0, y1=1, x2=0, y2=0))
    orbs = "".join(orb(256 + math.cos(a) * 214, 220 + math.sin(a) * 150, 17, i) for i, a in enumerate([k * math.tau / 8 - 2.3 for k in range(8)]))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g fill="#fff">{''.join(f'<circle cx="{(i * 97) % 512}" cy="{(i * 53) % 260}" r="{1 + (i % 3) * .7}" opacity="{.35 + (i % 4) * .15}"/>' for i in range(40))}</g>
<g fill="#ffd8f0" opacity=".55"><ellipse cx="70" cy="330" rx="90" ry="22"/><ellipse cx="450" cy="300" rx="80" ry="20"/></g>
{orbs}
<!-- floating island -->
<g filter="url(#sh)">
  <path d="M60 400 Q256 360 452 400 L420 430 Q330 520 256 512 Q170 520 92 430 Z" fill="url(#rock)"/>
  <path d="M120 450 L150 500 L170 455 Z M330 460 L350 505 L372 452 Z" fill="#4a2a1a" opacity=".6"/>
  <ellipse cx="256" cy="400" rx="198" ry="34" fill="url(#grass)"/>
</g>
<g fill="#ff8ab8"><circle cx="110" cy="398" r="5"/><circle cx="400" cy="402" r="5"/><circle cx="330" cy="410" r="4"/></g>
<!-- monsters -->
{monster(116, 318, .95, "url(#fireb)", "#ffe0c0", "#7a1a08", 1, "fire")}
{monster(396, 318, .95, "url(#waterb)", "#e0f4ff", "#0a3a7a", -1, "water")}
<!-- energy swirls into the egg -->
<path d="M196 274 C220 210 250 230 256 214" stroke="url(#swirlA)" stroke-width="16" fill="none" stroke-linecap="round"/>
<path d="M316 274 C292 210 262 230 256 214" stroke="url(#swirlB)" stroke-width="16" fill="none" stroke-linecap="round"/>
<circle cx="256" cy="210" r="120" fill="url(#core)"/>
<!-- cracking egg -->
<g transform="translate(256 210)" filter="url(#sh2)">
  <path d="M0 -70 C40 -70 60 -20 60 14 C60 50 34 72 0 72 C-34 72 -60 50 -60 14 C-60 -20 -40 -70 0 -70 Z" fill="url(#egg)" stroke="#a87a4a" stroke-width="5"/>
  <path d="M-58 0 L-38 -16 L-22 4 L-4 -18 L12 2 L30 -16 L44 2 L58 -8" stroke="#a87a4a" stroke-width="5" fill="none" stroke-linejoin="round"/>
  <circle cx="-26" cy="34" r="9" fill="#ff7a3a"/><circle cx="20" cy="44" r="8" fill="#3aa8ff"/><circle cx="2" cy="24" r="6" fill="#a04ad8"/><circle cx="34" cy="18" r="5" fill="#ffd23a"/>
  <path d="M-34 -40 Q-24 -58 -8 -62" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".8"/>
</g>
<g stroke="#fff6ff" stroke-width="6" stroke-linecap="round" opacity=".9">{''.join(f'<path d="M{256 + math.cos(a) * 88:.0f} {200 + math.sin(a) * 88:.0f} L{256 + math.cos(a) * 112:.0f} {200 + math.sin(a) * 112:.0f}"/>' for a in [-2.4, -1.57, -.75])}</g>
{sparkle(256, 118, 1.0, "#fff6ff")}{sparkle(176, 170, .6)}{sparkle(340, 160, .55)}{sparkle(60, 470, .45)}
'''
    return icon(defs, art)
