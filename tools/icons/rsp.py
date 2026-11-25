"""결전의 가위바위보 — a tense showdown under a spotlight: a bare fist (rock) slams against the rival's
black-gloved scissors, sparks and a shockwave bursting between them."""
from .common import icon, lg, rg, sparkle, rays

def fist(fill, dark, glove=False):
    # a chunky cartoon fist seen from the side, knuckles facing right
    O = f'stroke="{dark}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"'
    knuckles = "".join(f'<path d="M{40 + i * 2} {-46 + i * 30} q22 2 22 15 q0 13 -22 14" fill="{fill}" {O}/>' for i in range(4))
    return (f'<path d="M-120 -30 L-30 -40 L-30 40 L-120 34 Z" fill="{fill}" {O}/>'
            f'<path d="M-40 -56 Q40 -66 62 -34 Q74 0 62 40 Q40 76 -40 64 Q-60 0 -40 -56 Z" fill="{fill}" {O}/>'
            + knuckles +
            f'<path d="M-30 -10 Q0 -30 30 -20 Q44 -6 28 6 Q4 8 -20 4" fill="{fill}" {O}/>'
            f'<path d="M-28 -44 Q10 -56 40 -42" stroke="#fff" stroke-width="7" fill="none" opacity="{.2 if glove else .5}" stroke-linecap="round"/>')

def scissors(fill, dark):
    O = f'stroke="{dark}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"'
    return (f'<path d="M120 -30 L30 -40 L30 40 L120 34 Z" fill="{fill}" {O}/>'
            f'<path d="M40 -50 Q-30 -60 -50 -30 Q-60 10 -40 50 Q-10 70 40 60 Z" fill="{fill}" {O}/>'
            # two extended fingers in a V
            f'<path d="M-20 -30 L-150 -96 Q-168 -100 -170 -84 Q-168 -72 -156 -66 L-30 -6 Z" fill="{fill}" {O}/>'
            f'<path d="M-24 0 L-150 64 Q-166 72 -160 86 Q-152 96 -138 90 L-16 32 Z" fill="{fill}" {O}/>'
            # curled fingers
            f'<path d="M-36 44 q-22 6 -16 22 q8 10 26 2" fill="{fill}" {O}/>'
            f'<path d="M-140 -84 L-60 -44" stroke="#fff" stroke-width="5" opacity=".25" stroke-linecap="round"/><path d="M-140 74 L-60 34" stroke="#fff" stroke-width="5" opacity=".25" stroke-linecap="round"/>')

def build():
    defs = (rg("bg", (0, "#8a1a2a"), (.5, "#3a0a18"), (1, "#0a0208"), cx=.5, cy=.42, r=.75)
            + rg("spot", (0, "#fff0d0", .55), (1, "#fff0d0", 0))
            + rg("skin", (0, "#ffe2c8"), (.7, "#f4b48a"), (1, "#d88a5a"), cx=.35, cy=.3)
            + lg("glove", (0, "#4a4a5a"), (.5, "#1e1e28"), (1, "#0a0a10"))
            + rg("clash", (0, "#ffffff"), (.25, "#fff3a0", .95), (.6, "#ff8a3a", .5), (1, "#ff3a3a", 0)))
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffd0a0", .07, 18, 256, 250, 760)}
<ellipse cx="256" cy="40" rx="220" ry="320" fill="url(#spot)"/>
<!-- table edge -->
<path d="M-10 420 Q256 380 522 420 V522 H-10 Z" fill="#1a0a10"/>
<path d="M-10 420 Q256 380 522 420" stroke="#ff5a5a" stroke-width="4" opacity=".5" fill="none"/>
<!-- fist (rock), left -->
<g transform="translate(150 260) rotate(-8)" filter="url(#sh)">{fist("url(#skin)", "#6a2a10")}</g>
<!-- black glove scissors, right -->
<g transform="translate(398 250) rotate(4)" filter="url(#sh)">{scissors("url(#glove)", "#000")}</g>
<!-- clash -->
<circle cx="250" cy="250" r="110" fill="url(#clash)"/>
<g stroke="#fff6c0" stroke-width="7" stroke-linecap="round">
  <path d="M250 150 V176 M250 324 V350 M150 250 H174 M326 250 H350 M180 180 l18 18 M320 320 l-18 -18 M320 180 l-18 18 M180 320 l18 -18"/>
</g>
<g fill="#ffd24a">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(200, 140, 5), (310, 130, 4), (330, 370, 5), (180, 370, 4), (120, 200, 3), (390, 300, 3)])}</g>
<!-- VS badge -->
<g transform="translate(256 432) rotate(-6)" filter="url(#sh2)">
  <path d="M-62 -30 L70 -36 L60 30 L-70 34 Z" fill="#ffd24a" stroke="#5a1a00" stroke-width="6" stroke-linejoin="round"/>
  <path d="M-38 -16 L-22 20 L-6 -16 M30 -14 Q8 -20 10 -4 Q12 6 26 4 Q40 4 38 16 Q34 26 12 20" stroke="#5a1a00" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
{sparkle(250, 250, 1.1, "#ffffff")}{sparkle(90, 90, .5)}{sparkle(440, 110, .55)}
'''
    return icon(defs, art)
