"""디펜스 게임 — a stone castle on a green hill guards a winding road; a cannon tower fires, a dragon tower
breathes fire and an archer tower looses arrows while bats and a crowned boss march in under a dusk sky."""
from .common import icon, lg, rg, sparkle, rays

def tower(x, y, w, h, roof="#3a6ad8", flag=None):
    out = (f'<g filter="url(#sh2)"><rect x="{x - w / 2}" y="{y - h}" width="{w}" height="{h}" fill="url(#stone)" stroke="#3a3040" stroke-width="5"/>'
           + "".join(f'<rect x="{x - w / 2 + i * w / 4}" y="{y - h - 14}" width="{w / 4 - 4}" height="16" fill="url(#stone)" stroke="#3a3040" stroke-width="4"/>' for i in range(0, 4, 2))
           + f'<rect x="{x - w / 2 - 4}" y="{y - h - 4}" width="{w + 8}" height="10" fill="#8a8494" stroke="#3a3040" stroke-width="4"/>'
           + f'<rect x="{x - 7}" y="{y - h * .6}" width="14" height="20" rx="7" fill="#2a2030"/></g>')
    if flag:
        out += f'<path d="M{x} {y - h - 14} V{y - h - 56}" stroke="#5a3a1a" stroke-width="4"/><path d="M{x} {y - h - 56} L{x + 30} {y - h - 48} L{x} {y - h - 40} Z" fill="{flag}"/>'
    return out

def build():
    defs = (lg("sky", (0, "#2a2a7a"), (.55, "#ff7a6a"), (1, "#ffc87a"))
            + rg("sun", (0, "#fff6c0"), (1, "#ffd27a", 0))
            + lg("hill", (0, "#7ad860"), (1, "#3a9a3a"))
            + lg("stone", (0, "#d8d0e0"), (1, "#8a8098"))
            + lg("road", (0, "#e8c890"), (1, "#c89a5a"))
            + lg("fire", (0, "#fff3a0"), (.4, "#ffb02a"), (1, "#ff3a1a", 0), x1=1, y1=0, x2=0, y2=1)
            + rg("boom", (0, "#ffffff"), (.3, "#ffe08a", .95), (1, "#ff6a2a", 0))
            + rg("dragon", (0, "#9af07a"), (1, "#2a9a4a"), cx=.35, cy=.3)
            + lg("cannon", (0, "#5a5a6a"), (1, "#2a2a34")))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{rays("#fff3c0", .08, 16, 120, 300, 700)}
<circle cx="120" cy="300" r="120" fill="url(#sun)"/>
<path d="M-10 330 L60 270 L120 300 L200 240 L280 300 L340 260 L420 310 L522 270 V340 H-10 Z" fill="#7a4a8a" opacity=".55"/>
<path d="M-10 330 Q120 290 256 320 Q400 350 522 310 V522 H-10 Z" fill="url(#hill)"/>
<!-- winding road -->
<path d="M522 360 Q380 350 360 410 Q340 470 200 460 Q90 452 60 522" stroke="#a87a3a" stroke-width="70" fill="none" opacity=".5"/>
<path d="M522 360 Q380 350 360 410 Q340 470 200 460 Q90 452 60 522" stroke="url(#road)" stroke-width="56" fill="none"/>
<!-- castle on the left -->
<g transform="translate(0 0)">
  {tower(70, 330, 64, 150, flag="#ff4a6a")}
  {tower(150, 330, 56, 110, flag="#ffd24a")}
  <g filter="url(#sh2)"><rect x="40" y="250" width="150" height="80" fill="url(#stone)" stroke="#3a3040" stroke-width="5"/>
  <path d="M95 330 V292 Q110 272 125 292 V330 Z" fill="#5a3a1a" stroke="#3a2010" stroke-width="4"/></g>
</g>
<!-- cannon tower firing -->
{tower(280, 360, 54, 80)}
<g transform="translate(286 268) rotate(-20)"><rect x="0" y="-10" width="50" height="20" rx="8" fill="url(#cannon)" stroke="#1a1a24" stroke-width="4"/></g>
<circle cx="352" cy="244" r="38" fill="url(#boom)"/>
<!-- dragon tower breathing fire -->
{tower(436, 290, 50, 70)}
<g transform="translate(436 196)" filter="url(#sh2)">
  <path d="M-26 20 Q-30 -20 0 -24 Q30 -20 26 20 Z" fill="url(#dragon)" stroke="#1a5a2a" stroke-width="5"/>
  <path d="M-10 -22 L-16 -42 L-2 -26 M10 -22 L16 -42 L2 -26" fill="#ffd24a" stroke="#8a5a00" stroke-width="3"/>
  <circle cx="-8" cy="-6" r="5" fill="#fff"/><circle cx="-8" cy="-6" r="2.5" fill="#1a1a1a"/><path d="M-26 6 L-34 8" stroke="#1a5a2a" stroke-width="4"/>
</g>
<path d="M406 196 C360 200 330 240 300 300 C340 270 370 250 410 214 Z" fill="url(#fire)" opacity=".95"/>
<!-- arrows -->
<g stroke="#5a3a1a" stroke-width="4" stroke-linecap="round">
  <path d="M190 200 L240 222"/><path d="M200 180 L252 196"/>
</g>
<g fill="#ffffff"><path d="M240 222 l-10 -8 l2 10 z"/><path d="M252 196 l-11 -6 l3 10 z"/></g>
<!-- enemies on the road -->
<g filter="url(#sh2)">
  <g transform="translate(330 440)"><circle r="20" fill="#7a5ad8" stroke="#2a1a5a" stroke-width="4"/><circle cx="-7" cy="-4" r="4" fill="#ffe06a"/><circle cx="7" cy="-4" r="4" fill="#ffe06a"/><path d="M-6 8 L0 4 L6 8" stroke="#2a1a5a" stroke-width="3" fill="none"/></g>
  <g transform="translate(430 372)"><ellipse rx="34" ry="28" fill="#e85a4a" stroke="#6a1a10" stroke-width="5"/><path d="M-20 -24 L-14 -44 L-4 -30 L4 -46 L12 -30 L22 -44 L24 -22 Z" fill="#ffd24a" stroke="#8a5a00" stroke-width="4" stroke-linejoin="round"/>
    <ellipse cx="-11" cy="-4" rx="6" ry="7" fill="#fff"/><ellipse cx="11" cy="-4" rx="6" ry="7" fill="#fff"/><circle cx="-10" cy="-2" r="3" fill="#1a1a1a"/><circle cx="12" cy="-2" r="3" fill="#1a1a1a"/><path d="M-10 14 L-4 10 L2 14 L8 10" stroke="#6a1a10" stroke-width="4" fill="none"/></g>
  <g transform="translate(230 470)"><circle r="16" fill="#5ac86a" stroke="#1a6a2a" stroke-width="4"/><circle cx="-5" cy="-3" r="3" fill="#1a1a1a"/><circle cx="5" cy="-3" r="3" fill="#1a1a1a"/></g>
</g>
<!-- bats -->
<g fill="#3a2a5a">{''.join(f'<path transform="translate({x} {y}) scale({s})" d="M0 0 Q-14 -14 -34 -10 Q-26 -2 -28 8 Q-18 2 -10 10 Q-4 2 0 6 Q4 2 10 10 Q18 2 28 8 Q26 -2 34 -10 Q14 -14 0 0 Z"/>' for x, y, s in [(380, 110, 1.1), (460, 150, .8), (300, 90, .7)])}</g>
{sparkle(352, 244, .8, "#fff6c0")}{sparkle(200, 120, .55)}{sparkle(470, 60, .5)}
'''
    return icon(defs, art)
