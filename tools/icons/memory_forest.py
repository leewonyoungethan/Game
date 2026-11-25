"""기억의 숲 — in a twilight enchanted forest full of fireflies, two matched fox cards glow gold,
while a third card flips mid-air to reveal a sleepy owl."""
from .common import icon, lg, rg, sparkle, star_path

def fox(s=1):
    O = 'stroke="#5a2408" stroke-width="5" stroke-linejoin="round"'
    return (f'<g transform="scale({s})">'
            f'<path d="M-46 -20 L-40 -66 L-12 -38 Z M46 -20 L40 -66 L12 -38 Z" fill="#ff8a3a" {O}/>'
            f'<path d="M-36 -30 L-34 -54 L-20 -38 Z M36 -30 L34 -54 L20 -38 Z" fill="#ffd8c0"/>'
            f'<path d="M-50 -18 Q-52 -48 0 -50 Q52 -48 50 -18 Q48 18 0 40 Q-48 18 -50 -18 Z" fill="url(#foxg)" {O}/>'
            f'<path d="M-30 6 Q-20 34 0 40 Q20 34 30 6 Q14 14 0 4 Q-14 14 -30 6 Z" fill="#fff4e8"/>'
            f'<ellipse cx="-18" cy="-12" rx="6" ry="8" fill="#2a1408"/><ellipse cx="18" cy="-12" rx="6" ry="8" fill="#2a1408"/>'
            f'<circle cx="-16" cy="-15" r="2.4" fill="#fff"/><circle cx="20" cy="-15" r="2.4" fill="#fff"/>'
            f'<ellipse cx="0" cy="12" rx="7" ry="5" fill="#2a1408"/><path d="M-8 20 Q0 26 8 20" stroke="#2a1408" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
            f'<ellipse cx="-32" cy="6" rx="7" ry="4" fill="#ff7a8a" opacity=".55"/><ellipse cx="32" cy="6" rx="7" ry="4" fill="#ff7a8a" opacity=".55"/></g>')

def owl(s=1):
    O = 'stroke="#3a2a4a" stroke-width="5" stroke-linejoin="round"'
    return (f'<g transform="scale({s})">'
            f'<path d="M-44 -30 L-36 -60 L-16 -42 Z M44 -30 L36 -60 L16 -42 Z" fill="#8a6ad8" {O}/>'
            f'<ellipse cx="0" cy="0" rx="48" ry="50" fill="url(#owlg)" {O}/>'
            f'<ellipse cx="0" cy="22" rx="28" ry="24" fill="#e8dcff"/>'
            f'<circle cx="-18" cy="-12" r="16" fill="#fff" stroke="#3a2a4a" stroke-width="4"/><circle cx="18" cy="-12" r="16" fill="#fff" stroke="#3a2a4a" stroke-width="4"/>'
            f'<path d="M-26 -12 Q-18 -6 -10 -12 M10 -12 Q18 -6 26 -12" stroke="#3a2a4a" stroke-width="4" fill="none" stroke-linecap="round"/>'
            f'<path d="M-6 2 L6 2 L0 12 Z" fill="#ffb03a" stroke="#8a4a00" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<g fill="#c8b8f0" opacity=".9"><path d="M-12 20 q4 6 8 0 M4 20 q4 6 8 0 M-4 32 q4 6 8 0" stroke="#a898d8" stroke-width="3" fill="none"/></g></g>')

def card(face, gold=False):
    border = "url(#goldb)" if gold else "#fff"
    glow = '<rect x="-84" y="-114" width="168" height="228" rx="24" fill="#ffd24a" opacity=".55" filter="url(#b14)"/>' if gold else ""
    return (f'{glow}<rect x="-74" y="-104" width="148" height="208" rx="20" fill="url(#cardf)" stroke="{border}" stroke-width="8"/>'
            f'<rect x="-60" y="-90" width="120" height="180" rx="14" fill="none" stroke="#d8c8a8" stroke-width="2.5" stroke-dasharray="6 6"/>{face}')

def back():
    leaf = ''.join(f'<path d="M0 0 C-14 -14 -12 -36 0 -44 C12 -36 14 -14 0 0 Z" fill="#a8f0a0" opacity=".85" transform="rotate({a})"/>' for a in (-50, 0, 50))
    return (f'<rect x="-74" y="-104" width="148" height="208" rx="20" fill="url(#cardb)" stroke="#fff" stroke-width="8"/>'
            f'<rect x="-60" y="-90" width="120" height="180" rx="14" fill="none" stroke="#bff4c8" stroke-width="3" opacity=".6"/>'
            f'<g transform="translate(0 16)">{leaf}<circle r="7" fill="#fff6c0"/></g>'
            f'<path d="{star_path(0, -56, 12, .45)}" fill="#fff6c0"/>')

def build():
    defs = (lg("sky", (0, "#1a3a5a"), (.55, "#2a6a6a"), (1, "#1a4a3a"))
            + rg("moonglow", (0, "#fffbe0", .9), (.3, "#d8ffe0", .35), (1, "#d8ffe0", 0))
            + lg("cardf", (0, "#fffdf4"), (1, "#f4e8cc"))
            + lg("cardb", (0, "#3ab86a"), (1, "#1a7a4a"))
            + lg("goldb", (0, "#fff3a0"), (.5, "#ffc83a"), (1, "#e8901a"))
            + rg("foxg", (0, "#ffc070"), (.7, "#ff8a3a"), (1, "#e0602a"), cx=.4, cy=.3)
            + rg("owlg", (0, "#c8b0ff"), (1, "#7a5ad0"), cx=.4, cy=.3)
            + rg("fly", (0, "#ffffd0"), (.3, "#f0ff8a", .8), (1, "#c8ff5a", 0)))
    trees = "".join(f'<path d="M{x} 512 L{x} {y} " stroke="{c}" stroke-width="{w}"/><circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/><circle cx="{x - r * .6}" cy="{y + r * .4}" r="{r * .7}" fill="{c}"/><circle cx="{x + r * .6}" cy="{y + r * .3}" r="{r * .75}" fill="{c}"/>'
                    for x, y, r, w, c in [(40, 140, 70, 24, "#174a3a"), (150, 110, 60, 20, "#1a5442"), (370, 120, 66, 22, "#1a5442"), (480, 150, 74, 26, "#174a3a"), (260, 90, 50, 16, "#20604a")])
    flies = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#fly)"/>' for x, y, r in [(80, 250, 20), (420, 220, 24), (300, 70, 16), (60, 420, 18), (470, 420, 22), (200, 40, 14), (130, 320, 12), (380, 360, 14)])
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<circle cx="256" cy="160" r="260" fill="url(#moonglow)"/>
<circle cx="256" cy="130" r="40" fill="#fffbe0" opacity=".9"/>
<g stroke-linecap="round">{trees}</g>
<path d="M-10 420 Q140 380 256 410 Q380 440 522 400 V522 H-10 Z" fill="#14402e"/>
<!-- mushrooms -->
<g><rect x="54" y="440" width="12" height="26" rx="5" fill="#fff0e0"/><path d="M36 444 Q60 410 84 444 Z" fill="#ff5a6a"/><circle cx="54" cy="432" r="4" fill="#fff"/><circle cx="68" cy="436" r="3" fill="#fff"/>
<rect x="452" y="446" width="10" height="22" rx="4" fill="#fff0e0"/><path d="M438 450 Q457 422 476 450 Z" fill="#ffb03a"/><circle cx="457" cy="440" r="3.5" fill="#fff"/></g>
{flies}
<!-- left matched card -->
<g transform="translate(140 300) rotate(-14)" filter="url(#sh)">{card(fox(1.05), gold=True)}</g>
<!-- right matched card -->
<g transform="translate(372 300) rotate(14)" filter="url(#sh)">{card(fox(1.05), gold=True)}</g>
<!-- flipping middle card: half back, half owl, squeezed horizontally -->
<g transform="translate(256 236) rotate(-4) scale(.62 1)" filter="url(#sh)">{card(owl(1.05))}</g>
<g stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8" fill="none"><path d="M196 140 q-30 30 -18 70"/><path d="M316 140 q30 30 18 70"/></g>
<!-- match burst -->
<g transform="translate(256 412)">
  <circle r="46" fill="#ffd24a" opacity=".35" filter="url(#b14)"/>
  <circle r="30" fill="url(#goldb)" stroke="#fff" stroke-width="5"/>
  <path d="M-13 1 L-3 11 L15 -9" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
{sparkle(190, 190, .7, "#fff6c0")}{sparkle(330, 420, .5)}{sparkle(440, 120, .6, "#d8ffe0")}{sparkle(70, 180, .5, "#d8ffe0")}
'''
    return icon(defs, art)
