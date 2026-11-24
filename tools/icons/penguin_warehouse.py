"""펭귄 창고 — a determined little penguin in a red scarf pushing a fish crate onto a glowing ice hole."""
from .common import icon, lg, rg, sparkle, bokeh

def build():
    defs = (
        lg("sky", (0, "#3a8ae0"), (.6, "#1a4a9a"), (1, "#0c2450"))
        + lg("ice", (0, "#f2fbff"), (1, "#b8e0f4"))
        + lg("wall", (0, "#6a9ad8"), (1, "#2a4a80"))
        + lg("crate", (0, "#f0b070"), (.5, "#c8783a"), (1, "#7a3e14"))
        + rg("hole", (0, "#0a2a5a"), (.65, "#1a6ab8"), (1, "#8ae8ff"))
        + rg("holeGlow", (0, "#8ae8ff", .7), (1, "#8ae8ff", 0))
        + rg("body", (0, "#4a5a80"), (.6, "#1e2a48"), (1, "#0c1428"), cx=.38, cy=.3)
        + rg("belly", (0, "#ffffff"), (1, "#dfe8f4"), cx=.45, cy=.3)
        + lg("scarf", (0, "#ff7a9a"), (1, "#d81a4a"))
        + lg("beak", (0, "#ffd06a"), (1, "#ff8a1a"))
    )
    O = 'stroke="#0a1428" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    floor = "".join(f'<rect x="{x}" y="{y}" width="96" height="96" fill="url(#ice)" stroke="#a8d0ea" stroke-width="2"/>' for x in range(16, 500, 96) for y in range(300, 520, 96))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{bokeh(4, "#ffffff", 40, 2, 5, (.4, .9), (0, 0, 512, 300))}
<g>{floor}</g>
<path d="M30 340 l40 -14 M180 420 l50 -16 M380 470 l40 -12" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<!-- snow wall blocks in back -->
{''.join(f'<g filter="url(#sh2)"><rect x="{x}" y="226" width="92" height="86" rx="14" fill="url(#wall)" stroke="#1a3060" stroke-width="4"/><rect x="{x}" y="226" width="92" height="28" rx="14" fill="#f4fbff"/></g>' for x in (-40, 56, 152, 248, 344, 440))}
<!-- glowing ice hole goal -->
<ellipse cx="396" cy="420" rx="110" ry="60" fill="url(#holeGlow)"/>
<ellipse cx="396" cy="420" rx="76" ry="40" fill="url(#hole)" stroke="#bff6ff" stroke-width="6"/>
<!-- crate being pushed -->
<g transform="translate(300 300) rotate(-3)" filter="url(#sh)">
  <rect x="0" y="0" width="128" height="120" rx="16" fill="url(#crate)" {O} stroke="#3a1c06"/>
  <path d="M0 40 H128 M0 80 H128" stroke="#5a2c0c" stroke-width="5" opacity=".55"/>
  <rect x="10" y="8" width="108" height="12" rx="6" fill="#fff" opacity=".3"/>
  <g transform="translate(64 60)"><ellipse cx="-6" cy="0" rx="30" ry="16" fill="#8ae8ff" stroke="#1a4a7a" stroke-width="4"/><path d="M20 0 L42 -16 L42 16 Z" fill="#8ae8ff" stroke="#1a4a7a" stroke-width="4" stroke-linejoin="round"/><circle cx="-20" cy="-3" r="4" fill="#0a1428"/></g>
</g>
<!-- penguin pushing -->
<g transform="translate(176 360) rotate(10)">
  <ellipse cx="10" cy="120" rx="70" ry="16" fill="#0c2a50" opacity=".35" filter="url(#b6)"/>
  <g filter="url(#sh)">
    <ellipse cx="0" cy="20" rx="78" ry="96" fill="url(#body)" {O}/>
    <ellipse cx="18" cy="38" rx="50" ry="70" fill="url(#belly)"/>
    <path d="M62 -2 Q130 0 134 -40 Q100 -20 60 -30 Z" fill="url(#body)" {O}/>
    <path d="M-60 0 Q-104 40 -92 90 Q-70 60 -54 40 Z" fill="url(#body)" {O}/>
    <ellipse cx="-10" cy="114" rx="30" ry="12" fill="url(#beak)" {O} stroke="#a85a00"/>
    <ellipse cx="44" cy="114" rx="30" ry="12" fill="url(#beak)" {O} stroke="#a85a00"/>
  </g>
  <circle cx="20" cy="-36" r="20" fill="#fff"/><circle cx="62" cy="-34" r="18" fill="#fff"/>
  <circle cx="28" cy="-36" r="10" fill="#0a1428"/><circle cx="68" cy="-34" r="9" fill="#0a1428"/>
  <circle cx="32" cy="-40" r="4" fill="#fff"/><circle cx="71" cy="-38" r="3.5" fill="#fff"/>
  <path d="M8 -58 L34 -50 M54 -50 L78 -56" stroke="#0a1428" stroke-width="6" stroke-linecap="round"/>
  <path d="M40 -18 L86 -8 L40 2 Z" fill="url(#beak)" stroke="#a85a00" stroke-width="5" stroke-linejoin="round"/>
  <ellipse cx="0" cy="-6" rx="12" ry="7" fill="#ff7a9a" opacity=".5"/>
  <path d="M-64 14 Q0 34 68 10 L66 34 Q0 54 -62 36 Z" fill="url(#scarf)" stroke="#8a0a2a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-40 30 L-64 92 L-36 88 L-22 36 Z" fill="url(#scarf)" stroke="#8a0a2a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-36 -60 Q-10 -90 30 -86" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".3"/>
</g>
<g stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"><path d="M80 300 h-40 M70 330 h-50 M90 360 h-34"/></g>
{sparkle(396, 410, .9, "#e8fbff")}{sparkle(460, 160, .6)}{sparkle(60, 120, .5)}
'''
    return icon(defs, art)
