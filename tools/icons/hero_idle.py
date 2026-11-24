"""용사 키우기 — a chibi knight with a red plume swinging a glowing sword, gold coins bursting and a big level-up arrow behind."""
from .common import icon, lg, rg, sparkle, rays

def coin(x, y, r, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#sh2)"><ellipse rx="{r}" ry="{r}" fill="url(#coin)" stroke="#a86a00" stroke-width="{r * .14}"/>'
            f'<ellipse rx="{r * .62}" ry="{r * .62}" fill="none" stroke="#fff3b0" stroke-width="{r * .1}" opacity=".8"/><path d="M{-r * .18} {-r * .32} h{r * .36} v{r * .64} h{-r * .36} z" fill="#d8920a" opacity=".7"/></g>')

def build():
    defs = (rg("bg", (0, "#6a4ad8"), (.6, "#3a2a8a"), (1, "#1a1440"))
            + rg("coin", (0, "#fff6c0"), (.5, "#ffd24a"), (1, "#e8a010"), cx=.35, cy=.3)
            + lg("armor", (0, "#e8f0ff"), (.5, "#a8b8e8"), (1, "#6a7ac0"), x1=0, y1=0, x2=1, y2=1)
            + lg("blade", (0, "#ffffff"), (1, "#9ad8ff"), x1=0, y1=0, x2=1, y2=0)
            + rg("skin", (0, "#ffe8d0"), (1, "#f8c09a"))
            + lg("arrow", (0, "#9af07a"), (1, "#3ac05a"))
            + rg("swGlow", (0, "#bfefff", .9), (1, "#6ad0ff", 0)))
    O = 'stroke="#1e1a4a" stroke-width="7" stroke-linejoin="round"'
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .07, 16, 256, 260, 700)}
<!-- level-up arrow -->
<g transform="translate(400 300)" opacity=".95" filter="url(#sh2)"><path d="M-40 120 V10 H-80 L0 -90 L80 10 H40 V120 Z" fill="url(#arrow)" stroke="#1a6a2a" stroke-width="7" stroke-linejoin="round"/><path d="M-22 100 V0" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".5"/></g>
<!-- sword glow + blade -->
<g transform="translate(300 316) rotate(38)">
  <ellipse cx="0" cy="-120" rx="60" ry="150" fill="url(#swGlow)"/>
  <path d="M-16 0 L-14 -220 L0 -250 L14 -220 L16 0 Z" fill="url(#blade)" stroke="#2a4a7a" stroke-width="6" stroke-linejoin="round"/>
  <path d="M0 -10 V-226" stroke="#fff" stroke-width="5" opacity=".8"/>
  <rect x="-44" y="-6" width="88" height="18" rx="8" fill="url(#coin)" stroke="#7a4a00" stroke-width="5"/>
  <rect x="-9" y="10" width="18" height="44" rx="6" fill="#7a3a1a" stroke="#3a1a08" stroke-width="5"/>
  <circle cx="0" cy="60" r="12" fill="url(#coin)" stroke="#7a4a00" stroke-width="4"/>
</g>
<!-- knight -->
<g transform="translate(206 300)">
  <path d="M-60 -10 Q-120 60 -96 150 L-30 120 Z" fill="#e83a4a" stroke="#7a1020" stroke-width="7" stroke-linejoin="round"/>
  <g filter="url(#sh)"><rect x="-62" y="10" width="124" height="130" rx="34" fill="url(#armor)" {O}/></g>
  <rect x="-62" y="96" width="124" height="16" fill="#ffd24a" stroke="#1e1a4a" stroke-width="5"/>
  <g filter="url(#sh)"><circle cx="0" cy="-50" r="74" fill="url(#skin)" {O}/></g>
  <path d="M-80 -54 Q-82 -140 0 -142 Q82 -140 80 -54 L60 -54 Q54 -100 0 -104 Q-54 -100 -60 -54 Z" fill="url(#armor)" {O}/>
  <path d="M-10 -142 Q30 -210 90 -176 Q50 -170 24 -136 Z" fill="#e83a4a" stroke="#7a1020" stroke-width="6" stroke-linejoin="round"/>
  <ellipse cx="-24" cy="-44" rx="11" ry="15" fill="#1e1a2e"/><ellipse cx="28" cy="-44" rx="11" ry="15" fill="#1e1a2e"/>
  <circle cx="-20" cy="-50" r="4.5" fill="#fff"/><circle cx="32" cy="-50" r="4.5" fill="#fff"/>
  <path d="M-10 -10 Q4 4 18 -10" stroke="#1e1a2e" stroke-width="6" fill="none" stroke-linecap="round"/>
  <ellipse cx="-50" cy="-18" rx="14" ry="8" fill="#ff8a9a" opacity=".55"/><ellipse cx="54" cy="-18" rx="14" ry="8" fill="#ff8a9a" opacity=".55"/>
  <!-- shield -->
  <g transform="translate(-74 70)" filter="url(#sh2)"><path d="M-40 -46 H40 V0 Q40 40 0 60 Q-40 40 -40 0 Z" fill="#4a6ad8" stroke="#1e1a4a" stroke-width="7" stroke-linejoin="round"/><path d="M-8 -30 h16 v20 h20 v16 h-20 v30 h-16 v-30 h-20 v-16 h20 z" fill="#ffd24a"/></g>
  <circle cx="76" cy="40" r="22" fill="url(#skin)" {O}/>
</g>
{coin(84, 110, 34, -20)}{coin(150, 60, 22, 15)}{coin(440, 100, 28, 25)}{coin(60, 440, 26, 10)}{coin(470, 470, 20, -10)}
{sparkle(330, 60, .9, "#bfefff")}{sparkle(120, 200, .5)}{sparkle(470, 220, .5)}
'''
    return icon(defs, art)
