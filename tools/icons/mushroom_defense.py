"""버섯 마을 수비대 — a red-capped mushroom fort with an acorn cannon, defending a winding path from marching ants."""
from .common import icon, lg, rg, sparkle

def ant(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" filter="url(#sh2)">'
            '<g stroke="#2a1a1a" stroke-width="4" stroke-linecap="round">'
            '<path d="M-6 -2 L-20 -12 M-6 4 L-22 4 M-6 10 L-20 20 M6 -2 L20 -12 M6 4 L22 4 M6 10 L20 20 M-4 -20 L-12 -34 M4 -20 L12 -34"/></g>'
            '<circle cx="0" cy="-16" r="9" fill="#3a2a2a"/><circle cx="0" cy="2" r="8" fill="#3a2a2a"/><ellipse cx="0" cy="22" rx="12" ry="14" fill="#3a2a2a"/>'
            '<ellipse cx="-4" cy="17" rx="4" ry="6" fill="#fff" opacity=".25"/><circle cx="-3" cy="-18" r="2.5" fill="#fff"/><circle cx="4" cy="-18" r="2.5" fill="#fff"/></g>')

def build():
    defs = (lg("grass", (0, "#9ae070"), (1, "#4aa040"))
            + lg("path", (0, "#f0d098"), (1, "#c89858"))
            + rg("cap", (0, "#ff8a7a"), (.6, "#e8303a"), (1, "#a8101a"), cx=.35, cy=.3)
            + lg("stem", (0, "#fffaf0"), (1, "#e8d4b0"))
            + rg("acorn", (0, "#e8b878"), (1, "#9a6028"), cx=.35, cy=.3)
            + rg("sun", (0, "#fff8c0", .9), (1, "#fff8c0", 0)))
    O = 'stroke="#5a1a10" stroke-width="6" stroke-linejoin="round"'
    art = f'''
<rect width="512" height="512" fill="url(#grass)"/>
<circle cx="420" cy="60" r="200" fill="url(#sun)"/>
<g opacity=".35" fill="#3a8a30">{''.join(f'<path d="M{x} {y} l-6 -16 l6 8 l4 -18 l4 18 l6 -8 l-6 16 z"/>' for x, y in [(60, 120), (440, 300), (300, 470), (90, 470), (470, 450), (210, 90)])}</g>
<!-- path -->
<path d="M-20 150 Q120 140 160 230 T320 330 Q390 360 400 520" stroke="#8a5a2a" stroke-width="96" fill="none" stroke-linecap="round" opacity=".5"/>
<path d="M-20 150 Q120 140 160 230 T320 330 Q390 360 400 520" stroke="url(#path)" stroke-width="80" fill="none" stroke-linecap="round"/>
<path d="M-20 150 Q120 140 160 230 T320 330 Q390 360 400 520" stroke="#a87840" stroke-width="4" stroke-dasharray="4 18" fill="none" opacity=".5"/>
{ant(40, 150, .95, 85)}{ant(120, 175, 1.05, 120)}{ant(178, 262, 1.15, 140)}
<!-- acorn shot flying -->
<g filter="url(#sh2)"><ellipse cx="190" cy="92" rx="14" ry="17" fill="url(#acorn)" transform="rotate(60 190 92)"/><path d="M198 76 q12 8 2 24" stroke="#5a3a1a" stroke-width="9" fill="none" stroke-linecap="round"/></g>
<g stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"><path d="M216 92 l26 12 M210 112 l22 8"/></g>
<!-- mushroom fort -->
<g transform="translate(350 250)">
  <g filter="url(#sh)">
    <path d="M-62 30 Q-70 150 -58 170 L58 170 Q70 150 62 30 Z" fill="url(#stem)" {O}/>
    <path d="M-150 40 Q-150 -120 0 -130 Q150 -120 150 40 Q0 70 -150 40 Z" fill="url(#cap)" {O}/>
  </g>
  <g fill="#fff"><ellipse cx="-80" cy="-40" rx="26" ry="20"/><ellipse cx="10" cy="-88" rx="22" ry="16"/><ellipse cx="80" cy="-20" rx="20" ry="16"/><ellipse cx="-20" cy="0" rx="14" ry="11"/></g>
  <path d="M-110 -50 Q-90 -100 -30 -112" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".45"/>
  <path d="M-22 170 V110 Q0 88 22 110 V170 Z" fill="#8a4a2a" stroke="#5a1a10" stroke-width="5"/>
  <circle cx="-34" cy="86" r="14" fill="#ffe08a" stroke="#5a1a10" stroke-width="5"/><path d="M-34 72 V100 M-48 86 H-20" stroke="#5a1a10" stroke-width="3"/>
  <!-- acorn cannon on top -->
  <g transform="translate(-60 -118) rotate(-150)">
    <rect x="-4" y="-14" width="66" height="28" rx="10" fill="#7a4a20" stroke="#3a1a08" stroke-width="5"/>
    <ellipse cx="62" cy="0" rx="8" ry="14" fill="#3a1a08"/>
  </g>
  <g filter="url(#sh2)"><ellipse cx="-60" cy="-112" rx="34" ry="30" fill="url(#acorn)" stroke="#5a2a08" stroke-width="5"/>
  <path d="M-96 -122 Q-60 -160 -24 -122 Q-60 -112 -96 -122 Z" fill="#6a3a14" stroke="#3a1a08" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-60 -146 v-14" stroke="#3a1a08" stroke-width="6" stroke-linecap="round"/></g>
</g>
<!-- shield badge -->
<g transform="translate(96 398)" filter="url(#sh)">
  <path d="M0 -62 L52 -42 Q52 30 0 62 Q-52 30 -52 -42 Z" fill="#ffd24a" stroke="#8a5a0a" stroke-width="6" stroke-linejoin="round"/>
  <path d="M0 -44 L36 -30 Q36 20 0 44 Q-36 20 -36 -30 Z" fill="#ffe88a"/>
  <path d="M-18 2 L-4 16 L22 -14" stroke="#8a5a0a" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
{sparkle(420, 70, 1.0)}{sparkle(160, 330, .55)}{sparkle(470, 200, .5)}
'''
    return icon(defs, art)
