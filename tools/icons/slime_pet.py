"""말랑 슬라임 키우기 — a glossy mint slime beaming on a pink rug, a floating heart, a jelly snack and a tiny crown."""
from .common import icon, lg, rg, sparkle, heart_path

def build():
    defs = (lg("bg", (0, "#ffe2d4"), (1, "#ffb8c8"))
            + rg("body", (0, "#ffffff"), (.22, "#b8ffe4"), (.7, "#5ae0b0"), (1, "#22a884"), cx=.36, cy=.28, r=.8)
            + lg("rug", (0, "#ff8ab0"), (1, "#e8608a"))
            + lg("jelly", (0, "#ffb0c8"), (1, "#ff5a8a"))
            + lg("crown", (0, "#fff0a0"), (1, "#f0a020"))
            + rg("halo", (0, "#ffffff", .7), (1, "#ffffff", 0)))
    O = 'stroke="#127a5e" stroke-width="7"'
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
<g fill="#ff9ab0" opacity=".35">{''.join(f'<circle cx="{x}" cy="{y}" r="7"/>' for y in range(40, 330, 56) for x in range(30 + (y // 56 % 2) * 28, 512, 56))}</g>
<circle cx="256" cy="250" r="230" fill="url(#halo)"/>
<rect y="372" width="512" height="140" fill="#d8a070"/>
<ellipse cx="256" cy="420" rx="230" ry="58" fill="url(#rug)"/>
<ellipse cx="256" cy="420" rx="196" ry="44" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="16 14" opacity=".8"/>
<ellipse cx="256" cy="420" rx="150" ry="22" fill="#000" opacity=".15"/>
<!-- slime -->
<g filter="url(#sh)">
  <path d="M96 412 C88 300 150 150 256 146 C362 150 424 300 416 412 Q256 440 96 412 Z" fill="url(#body)" {O}/>
</g>
<ellipse cx="176" cy="236" rx="30" ry="50" fill="#fff" opacity=".75" transform="rotate(28 176 236)"/>
<circle cx="214" cy="186" r="12" fill="#fff" opacity=".85"/>
<!-- face -->
<g fill="#1e1a2e">
  <ellipse cx="200" cy="300" rx="20" ry="27"/><ellipse cx="312" cy="300" rx="20" ry="27"/>
</g>
<circle cx="192" cy="288" r="8" fill="#fff"/><circle cx="304" cy="288" r="8" fill="#fff"/>
<circle cx="207" cy="308" r="3.5" fill="#fff"/><circle cx="319" cy="308" r="3.5" fill="#fff"/>
<ellipse cx="150" cy="336" rx="26" ry="15" fill="#ff7aa8" opacity=".55"/><ellipse cx="362" cy="336" rx="26" ry="15" fill="#ff7aa8" opacity=".55"/>
<path d="M232 334 Q256 362 280 334" stroke="#1e1a2e" stroke-width="9" fill="none" stroke-linecap="round"/>
<!-- crown -->
<g transform="translate(256 140) rotate(-8)" filter="url(#sh2)">
  <path d="M-52 10 L-58 -44 L-26 -18 L0 -58 L26 -18 L58 -44 L52 10 Z" fill="url(#crown)" stroke="#8a5a00" stroke-width="6" stroke-linejoin="round"/>
  <circle cx="0" cy="-8" r="9" fill="#ff5a8a" stroke="#8a5a00" stroke-width="3"/>
  <circle cx="-58" cy="-46" r="6" fill="#fff0a0"/><circle cx="0" cy="-60" r="6" fill="#fff0a0"/><circle cx="58" cy="-46" r="6" fill="#fff0a0"/>
</g>
<!-- heart -->
<g transform="translate(410 128) rotate(14)" filter="url(#sh2)"><path d="{heart_path(0, 0, 44)}" fill="#ff4a8a" stroke="#a81a4a" stroke-width="5"/></g>
<!-- jelly snack -->
<g transform="translate(86 404)" filter="url(#sh2)">
  <path d="M-34 0 L-26 -46 Q0 -60 26 -46 L34 0 Z" fill="url(#jelly)" stroke="#a81a4a" stroke-width="5" stroke-linejoin="round"/>
  <ellipse cx="0" cy="-48" rx="26" ry="8" fill="#ffd0dc"/><circle cx="0" cy="-60" r="10" fill="#e8304a" stroke="#a81a4a" stroke-width="4"/>
  <path d="M-16 -36 L-14 -10" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"/>
  <ellipse cx="0" cy="2" rx="44" ry="9" fill="#fff" stroke="#c8b0b8" stroke-width="3"/>
</g>
{sparkle(120, 110, .9)}{sparkle(452, 260, .6)}{sparkle(330, 90, .5)}
'''
    return icon(defs, art)
