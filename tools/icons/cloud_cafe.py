"""구름 카페 — a big pastel latte cup with heart latte-art floating on fluffy clouds, steam curling up, a strawberry cake slice beside it."""
from .common import icon, lg, rg, sparkle, heart_path

def build():
    defs = (lg("sky", (0, "#ffc8d8"), (.55, "#ffe0d0"), (1, "#c8d8ff"))
            + lg("cup", (0, "#ffffff"), (1, "#f0d8e0"), x1=0, y1=0, x2=1, y2=0)
            + rg("latte", (0, "#f8e0c0"), (.7, "#d8a070"), (1, "#a8683a"))
            + lg("plate", (0, "#ffffff"), (1, "#e8d8e8"))
            + lg("cake", (0, "#fff4e0"), (1, "#f8d8a8"))
            + rg("cloud", (0, "#ffffff"), (1, "#f4f0ff"), cx=.5, cy=.3))
    cloud = lambda x, y, s: f'<g transform="translate({x} {y}) scale({s})" fill="url(#cloud)"><ellipse cx="0" cy="0" rx="90" ry="40"/><circle cx="-44" cy="-20" r="40"/><circle cx="20" cy="-36" r="52"/><circle cx="66" cy="-10" r="36"/></g>'
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g opacity=".7">{cloud(90, 120, .55)}{cloud(430, 80, .45)}</g>
<!-- steam -->
<g stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".85">
  <path d="M210 150 C190 120 230 100 210 70"/><path d="M260 140 C240 100 290 84 266 46"/><path d="M310 150 C290 120 330 104 310 74"/>
</g>
<!-- base clouds -->
<g filter="url(#sh)">{cloud(256, 452, 1.7)}</g>
<!-- cup -->
<g filter="url(#sh)">
  <path d="M392 260 C470 250 470 360 380 350" stroke="#ffffff" stroke-width="28" fill="none" stroke-linecap="round"/>
  <path d="M392 260 C470 250 470 360 380 350" stroke="#e8c8d4" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/>
  <path d="M112 210 L400 210 Q396 360 330 400 L182 400 Q116 360 112 210 Z" fill="url(#cup)" stroke="#c8909a" stroke-width="7" stroke-linejoin="round"/>
</g>
<ellipse cx="256" cy="212" rx="144" ry="34" fill="#c8909a"/>
<ellipse cx="256" cy="212" rx="134" ry="27" fill="url(#latte)"/>
<g transform="translate(256 213) scale(1 .4)"><path d="{heart_path(0, 0, 70)}" fill="#fff8ec"/><path d="{heart_path(0, 6, 38)}" fill="#e8b888"/></g>
<path d="M140 250 Q150 340 196 380" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".8"/>
<!-- cup face -->
<g fill="#5a2a3a"><ellipse cx="216" cy="300" rx="9" ry="12"/><ellipse cx="296" cy="300" rx="9" ry="12"/></g>
<path d="M240 322 Q256 338 272 322" stroke="#5a2a3a" stroke-width="7" fill="none" stroke-linecap="round"/>
<ellipse cx="190" cy="324" rx="16" ry="9" fill="#ff8aa8" opacity=".55"/><ellipse cx="322" cy="324" rx="16" ry="9" fill="#ff8aa8" opacity=".55"/>
<!-- cake slice -->
<g transform="translate(96 404)" filter="url(#sh2)">
  <ellipse cx="0" cy="18" rx="62" ry="14" fill="url(#plate)" stroke="#c8a8c0" stroke-width="4"/>
  <path d="M-46 10 L46 10 L46 -34 L-46 -12 Z" fill="url(#cake)" stroke="#a8705a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-46 -2 L46 -2 L46 -14 L-46 -6 Z" fill="#ff8aa8"/>
  <path d="M-46 -12 L46 -34 L44 -42 L-46 -20 Z" fill="#fff" stroke="#a8705a" stroke-width="4" stroke-linejoin="round"/>
  <path d="M26 -62 Q40 -64 40 -48 Q34 -34 26 -40 Q16 -48 26 -62 Z" fill="#ff3a5a" stroke="#a81a3a" stroke-width="4"/>
  <path d="M30 -62 l4 -10" stroke="#3a8a3a" stroke-width="4" stroke-linecap="round"/>
</g>
{sparkle(420, 170, .8)}{sparkle(70, 250, .55)}{sparkle(360, 60, .5)}
'''
    return icon(defs, art)
