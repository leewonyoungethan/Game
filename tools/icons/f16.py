"""F16 스카이 스트라이커 — an F-16 blasting through the clouds, firing at an enemy jet."""
from .common import icon, lg, rg, stars, sparkle

def jet(hull, wing, canopy, stroke="#0e1830"):
    O = f'stroke="{stroke}" stroke-width="6" stroke-linejoin="round"'
    return f'''
  <path d="M0 -150 L22 -60 L150 6 L150 36 L26 26 L20 76 L66 104 L66 122 L0 112 L-66 122 L-66 104 L-20 76 L-26 26 L-150 36 L-150 6 L-22 -60 Z" fill="{wing}" {O}/>
  <path d="M0 -196 Q22 -150 24 -80 L20 120 L-20 120 L-24 -80 Q-22 -150 0 -196 Z" fill="{hull}" {O}/>
  <path d="M0 -150 Q14 -120 13 -78 L-13 -78 Q-14 -120 0 -150 Z" fill="{canopy}" {O}/>
'''

def build():
    defs = (
        lg("sky", (0, "#1c4aa8"), (.55, "#0e2564"), (1, "#050b26"))
        + lg("hull", (0, "#ffffff"), (.35, "#dfe6f2"), (.7, "#9aa8c0"), (1, "#5a6884"), x1=0, y1=0, x2=1, y2=0)
        + lg("wing", (0, "#b8c6dc"), (.5, "#8494b0"), (1, "#4a5874"), x1=0, y1=0, x2=1, y2=0)
        + lg("canopy", (0, "#f0fbff"), (.35, "#7ad0ff"), (1, "#0a3a80"))
        + lg("flame", (0, "#ffffff"), (.2, "#bff6ff"), (.5, "#3a9aff", .85), (1, "#2a6aff", 0))
        + rg("boom", (0, "#fffbe0"), (.25, "#ffe066"), (.55, "#ff7a1a", .9), (1, "#ff3a1a", 0))
        + lg("shot", (0, "#fff6b0", 0), (1, "#fffbe0"))
        + lg("enemyHull", (0, "#ff9aa8"), (.5, "#e02a44"), (1, "#7a0a1c"), x1=0, y1=0, x2=1, y2=0)
        + lg("enemyWing", (0, "#c8283c"), (1, "#5a0614"), x1=0, y1=0, x2=1, y2=0)
        + lg("cloud", (0, "#ffffff"), (1, "#bcd0f0"))
        + lg("missile", (0, "#ffffff"), (1, "#9aa6bc"), x1=0, y1=0, x2=1, y2=0)
    )
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(29, 50, (0, 0, 512, 512), .6, 1.8)}
<!-- clouds far below (parallax) -->
<g fill="url(#cloud)" opacity=".35" filter="url(#b6)">
  <ellipse cx="80" cy="420" rx="110" ry="34"/><ellipse cx="470" cy="300" rx="90" ry="28"/><ellipse cx="420" cy="480" rx="120" ry="34"/><ellipse cx="40" cy="200" rx="70" ry="22"/>
</g>
<g stroke="#bcd4ff" stroke-width="3" stroke-linecap="round" opacity=".4">
  <path d="M48 30 V110"/><path d="M466 120 V210"/><path d="M96 280 V350"/><path d="M430 340 V420"/><path d="M28 420 V500"/><path d="M490 20 V70"/>
</g>
<!-- enemy + explosion -->
<circle cx="112" cy="104" r="84" fill="url(#boom)"/>
<g fill="#ffd23a" stroke="#7a2a00" stroke-width="3"><path d="M84 88 l14 -8 l6 14 Z"/><path d="M140 126 l12 8 l-12 6 Z"/><path d="M126 70 l8 -12 l6 10 Z"/></g>
<g stroke="#fff6c0" stroke-width="4" stroke-linecap="round" opacity=".8"><path d="M112 104 l-48 -30 M112 104 l50 -36 M112 104 l-42 40 M112 104 l46 34"/></g>
<g transform="translate(396 92) rotate(180) scale(.42)" filter="url(#sh2)">{jet("url(#enemyHull)", "url(#enemyWing)", "#2a0a10", "#3a0610")}</g>
<!-- tracer fire -->
<g fill="url(#shot)">
  <rect x="226" y="30" width="10" height="74" rx="5"/><rect x="276" y="30" width="10" height="74" rx="5"/>
  <rect x="226" y="122" width="10" height="56" rx="5"/><rect x="276" y="122" width="10" height="56" rx="5"/>
</g>
<g filter="url(#glowS)" fill="#fffbe0"><circle cx="231" cy="32" r="5"/><circle cx="281" cy="32" r="5"/></g>
<!-- player jet -->
<g transform="translate(256 318)">
  <path d="M-16 112 L0 230 L16 112 Z" fill="url(#flame)"/>
  <ellipse cx="0" cy="124" rx="20" ry="14" fill="#dff8ff" filter="url(#glow)"/>
  <g filter="url(#sh)">{jet("url(#hull)", "url(#wing)", "url(#canopy)")}</g>
  <path d="M-5 -140 Q-12 -116 -9 -88" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".9"/>
  <path d="M-138 16 L-30 -40 M138 16 L30 -40" stroke="#fff" stroke-width="3" opacity=".45"/>
  <path d="M-20 -20 H20 M-20 40 H20" stroke="#5a6884" stroke-width="2" opacity=".6"/>
  <g stroke="#0e1830" stroke-width="4">
    <rect x="-104" y="-14" width="12" height="52" rx="6" fill="url(#missile)"/><rect x="92" y="-14" width="12" height="52" rx="6" fill="url(#missile)"/>
    <rect x="-150" y="-6" width="10" height="44" rx="5" fill="url(#missile)"/><rect x="140" y="-6" width="10" height="44" rx="5" fill="url(#missile)"/>
  </g>
  <circle cx="-150" cy="22" r="5" fill="#ff3a4a" filter="url(#glowS)"/><circle cx="150" cy="22" r="5" fill="#3aff8a" filter="url(#glowS)"/>
  <path d="M-8 60 h16 v14 h-16 Z" fill="#2a3a6a" opacity=".5"/>
</g>
<!-- near clouds whooshing by -->
<g fill="url(#cloud)" opacity=".85" filter="url(#b2)">
  <path d="M-20 512 Q20 450 90 466 Q120 430 170 456 Q200 444 220 470 L220 512 Z"/>
  <path d="M532 512 Q500 456 440 468 Q410 438 370 460 Q340 452 330 476 L330 512 Z"/>
</g>
{sparkle(446, 236, .75)}{sparkle(66, 260, .55)}
'''
    return icon(defs, art)
