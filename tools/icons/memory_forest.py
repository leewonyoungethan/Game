"""기억의 숲 — two matching fox cards flipping face-up in a sunlit forest, with leaf cards behind."""
from .common import icon, lg, rg, sparkle, bokeh

def card_back(x, y, rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#sh2)">'
            f'<rect x="-70" y="-94" width="140" height="188" rx="22" fill="url(#back)" stroke="#e8f8d8" stroke-width="7"/>'
            f'<rect x="-54" y="-78" width="108" height="156" rx="14" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="4" stroke-dasharray="10 8"/>'
            f'<path d="M0 -30 Q34 -10 0 40 Q-34 -10 0 -30 Z" fill="#d8ffb8" opacity=".85"/><path d="M0 -24 V36" stroke="#2a8a4a" stroke-width="4"/></g>')

def fox(cx, cy, s):
    return f'''<g transform="translate({cx} {cy}) scale({s})">
  <path d="M-46 -10 L-40 -62 L-12 -34 Z M46 -10 L40 -62 L12 -34 Z" fill="#ff8a2a" stroke="#5a1e04" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-38 -24 L-36 -50 L-20 -34 Z M38 -24 L36 -50 L20 -34 Z" fill="#5a1e04"/>
  <path d="M-52 -4 Q-48 -44 0 -44 Q48 -44 52 -4 Q46 34 0 52 Q-46 34 -52 -4 Z" fill="url(#foxFur)" stroke="#5a1e04" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-40 6 Q-20 -4 0 14 Q20 -4 40 6 Q30 38 0 50 Q-30 38 -40 6 Z" fill="#fff6ec"/>
  <ellipse cx="-18" cy="-6" rx="6" ry="8" fill="#2a0e04"/><ellipse cx="18" cy="-6" rx="6" ry="8" fill="#2a0e04"/>
  <circle cx="-16" cy="-9" r="2.4" fill="#fff"/><circle cx="20" cy="-9" r="2.4" fill="#fff"/>
  <ellipse cx="0" cy="18" rx="8" ry="6" fill="#2a0e04"/>
  <ellipse cx="-30" cy="10" rx="7" ry="4" fill="#ff7a9a" opacity=".5"/><ellipse cx="30" cy="10" rx="7" ry="4" fill="#ff7a9a" opacity=".5"/>
</g>'''

def card_front(x, y, rot, glow=True):
    g = f'<rect x="-84" y="-108" width="168" height="216" rx="30" fill="url(#matchGlow)"/>' if glow else ""
    return (f'<g transform="translate({x} {y}) rotate({rot})">{g}<g filter="url(#sh)">'
            f'<rect x="-70" y="-94" width="140" height="188" rx="22" fill="url(#front)" stroke="#9af06a" stroke-width="7"/></g>'
            f'{fox(0, 4, 1.05)}</g>')

def build():
    defs = (
        rg("bg", (0, "#9ae87a"), (.5, "#3a9a5a"), (1, "#0e3a1e"), cx=.5, cy=.1, r=1.05)
        + lg("back", (0, "#7ad88a"), (1, "#2a8a4a"), x2=1, y2=1)
        + lg("front", (0, "#fffdf4"), (1, "#e8f6d4"))
        + rg("foxFur", (0, "#ffc070"), (.6, "#ff8a2a"), (1, "#c8500a"), cx=.4, cy=.3)
        + rg("matchGlow", (0, "#fff6b0", .8), (.6, "#d8ff9a", .35), (1, "#d8ff9a", 0))
        + rg("sunbeam", (0, "#fffbe0", .5), (1, "#fffbe0", 0))
    )
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
<path d="M120 -20 L60 540 L180 540 Z M300 -20 L260 540 L380 540 Z" fill="#fffbe0" opacity=".08"/>
<circle cx="256" cy="40" r="220" fill="url(#sunbeam)"/>
{bokeh(12, "#e8ffd0", 18, 4, 16, (.15, .45))}
<g fill="#0c3018" opacity=".6"><path d="M0 512 L0 420 Q40 380 80 420 Q120 370 160 420 L160 512 Z"/><path d="M512 512 L512 410 Q470 370 430 410 Q390 380 360 420 L360 512 Z"/></g>
{card_back(150, 300, -18)}
{card_back(362, 300, 18)}
{card_front(190, 258, -8)}
{card_front(326, 258, 8)}
<g fill="#ffe680" stroke="#8a5a00" stroke-width="4" stroke-linejoin="round">
  <path d="M258 110 l10 -22 l10 22 l24 4 l-18 16 l6 24 l-22 -12 l-22 12 l6 -24 l-18 -16 Z" transform="translate(-10 0)"/>
</g>
<g transform="translate(110 450) rotate(-30)"><path d="M0 -26 Q22 -6 0 26 Q-22 -6 0 -26 Z" fill="#8ae06a" stroke="#2a7a2a" stroke-width="4"/><path d="M0 -20 V22" stroke="#2a7a2a" stroke-width="3"/></g>
<g transform="translate(420 100) rotate(40)"><path d="M0 -22 Q18 -4 0 22 Q-18 -4 0 -22 Z" fill="#ffb04a" stroke="#a8500a" stroke-width="4"/><path d="M0 -16 V18" stroke="#a8500a" stroke-width="3"/></g>
{sparkle(120, 150, .7)}{sparkle(410, 180, .6, "#fff6c0")}{sparkle(258, 430, .55)}
'''
    return icon(defs, art)
