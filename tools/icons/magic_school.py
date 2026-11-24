"""마법학교 3년 — a young witch in a starry hat waving a sparkling wand before a turreted academy under a crescent moon, an open spellbook glowing."""
from .common import icon, lg, rg, sparkle, stars, star_path

def build():
    defs = (lg("sky", (0, "#140a3a"), (.6, "#4a2a8a"), (1, "#9a5ab8"))
            + rg("moon", (0, "#fffbe0"), (1, "#ffe08a"))
            + lg("hat", (0, "#a87aff"), (1, "#5a2ab8"))
            + lg("robe", (0, "#7a4ae0"), (1, "#3a1a8a"))
            + rg("skin", (0, "#ffeedd"), (1, "#f8c8a8"))
            + lg("tower", (0, "#5a3aa0"), (1, "#2a1a5a"))
            + lg("roof", (0, "#ff8ac8"), (1, "#c83a8a"))
            + rg("book", (0, "#fff8d0", .95), (1, "#ffd27a", 0))
            + rg("tip", (0, "#ffffff"), (.5, "#fff0a0"), (1, "#ffd27a", 0)))
    towers = ""
    for x, w, h in [(300, 50, 230), (360, 62, 300), (430, 50, 210), (250, 40, 170)]:
        top = 470 - h
        towers += (f'<rect x="{x - w / 2}" y="{top}" width="{w}" height="{h + 60}" fill="url(#tower)"/>'
                   f'<path d="M{x - w * .7} {top} L{x} {top - w * 1.5} L{x + w * .7} {top} Z" fill="url(#roof)"/>'
                   + "".join(f'<rect x="{x - 6}" y="{wy}" width="12" height="18" rx="6" fill="#ffd27a" opacity=".9"/>' for wy in range(int(top) + 20, 450, 46)))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(21, 70, area=(0, 0, 512, 300))}
<circle cx="420" cy="86" r="44" fill="url(#moon)"/><circle cx="440" cy="72" r="40" fill="#1c0e46"/>
<g opacity=".95">{towers}</g>
<path d="M-10 470 Q256 430 522 470 V522 H-10 Z" fill="#2a1450"/>
<!-- witch -->
<g transform="translate(176 300)">
  <g filter="url(#sh)"><path d="M-84 210 Q-90 60 0 40 Q90 60 84 210 Z" fill="url(#robe)" stroke="#1a0a40" stroke-width="7" stroke-linejoin="round"/></g>
  <path d="M-10 46 L0 210 L10 46 Z" fill="#ffd27a" opacity=".8"/>
  <g filter="url(#sh)"><circle cx="0" cy="-10" r="70" fill="url(#skin)" stroke="#3a1a2a" stroke-width="7"/></g>
  <path d="M-72 -14 Q-80 -70 -30 -76 Q0 -40 30 -76 Q80 -70 72 -14 Q62 -48 34 -54 Q0 -20 -34 -54 Q-62 -48 -72 -14 Z" fill="#6a3a2a" stroke="#3a1a10" stroke-width="5" stroke-linejoin="round"/>
  <ellipse cx="-24" cy="2" rx="10" ry="14" fill="#2a1430"/><ellipse cx="26" cy="2" rx="10" ry="14" fill="#2a1430"/>
  <circle cx="-20" cy="-4" r="4.5" fill="#fff"/><circle cx="30" cy="-4" r="4.5" fill="#fff"/>
  <ellipse cx="-46" cy="26" rx="13" ry="8" fill="#ff8ab0" opacity=".55"/><ellipse cx="48" cy="26" rx="13" ry="8" fill="#ff8ab0" opacity=".55"/>
  <path d="M-12 30 Q2 44 16 30" stroke="#3a1a2a" stroke-width="6" fill="none" stroke-linecap="round"/>
  <!-- hat -->
  <g filter="url(#sh2)">
    <ellipse cx="0" cy="-66" rx="108" ry="24" fill="url(#hat)" stroke="#1a0a40" stroke-width="6"/>
    <path d="M-62 -72 Q-30 -150 10 -240 Q30 -200 70 -150 Q40 -130 62 -72 Z" fill="url(#hat)" stroke="#1a0a40" stroke-width="6" stroke-linejoin="round"/>
    <path d="M-62 -86 Q0 -70 62 -86 L62 -70 Q0 -54 -62 -70 Z" fill="#ffd27a" stroke="#1a0a40" stroke-width="4"/>
  </g>
  <path d="{star_path(18, -150, 16)}" fill="#ffe88a"/><path d="{star_path(-14, -112, 10)}" fill="#ffe88a"/>
  <!-- wand arm -->
  <path d="M60 90 Q110 70 130 20" stroke="#3a1a8a" stroke-width="26" fill="none" stroke-linecap="round"/>
  <circle cx="132" cy="14" r="15" fill="url(#skin)" stroke="#3a1a2a" stroke-width="5"/>
  <path d="M134 10 L190 -70" stroke="#7a4a2a" stroke-width="9" stroke-linecap="round"/>
  <circle cx="194" cy="-76" r="40" fill="url(#tip)"/>
  <path d="{star_path(194, -76, 16)}" fill="#fff"/>
</g>
<!-- sparkle trail -->
<g fill="#ffd27a">{''.join(f'<path d="{star_path(x, y, r)}" opacity="{o}"/>' for x, y, r, o in [(410, 170, 12, .95), (440, 230, 9, .8), (380, 120, 8, .7), (466, 160, 7, .6), (430, 290, 6, .5)])}</g>
<!-- open book -->
<g transform="translate(400 430)" filter="url(#sh2)">
  <circle cx="0" cy="-40" r="70" fill="url(#book)"/>
  <path d="M0 -4 Q-40 -24 -78 -12 L-78 34 Q-40 22 0 40 Z" fill="#fff8ec" stroke="#5a2a7a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M0 -4 Q40 -24 78 -12 L78 34 Q40 22 0 40 Z" fill="#fff8ec" stroke="#5a2a7a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-62 2 Q-36 -8 -14 4 M-62 16 Q-36 6 -14 18 M14 4 Q36 -8 62 2 M14 18 Q36 6 62 16" stroke="#c8a8e8" stroke-width="4" fill="none"/>
</g>
{sparkle(80, 80, .7)}{sparkle(250, 60, .5)}{sparkle(60, 300, .45)}
'''
    return icon(defs, art)
