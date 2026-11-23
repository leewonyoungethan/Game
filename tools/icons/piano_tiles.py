"""건반 소나기 — glossy black tiles raining onto a glowing piano keyboard."""
from .common import icon, lg, rg, bokeh, sparkle

def build():
    defs = (
        rg("bg", (0, "#ff6ad0"), (.45, "#8a34ff"), (1, "#1e0a6a"), cx=.3, cy=.15, r=1.05)
        + lg("tile", (0, "#5a5e74"), (.12, "#272a36"), (1, "#06070c"))
        + lg("tileEdge", (0, "#ffffff", .5), (1, "#ffffff", 0))
        + lg("streak", (0, "#c9b4ff", 0), (1, "#c9b4ff", .55))
        + lg("white", (0, "#ffffff"), (.8, "#ece8fa"), (1, "#c8c0e6"))
        + lg("black", (0, "#4a4c5a"), (.15, "#1a1b22"), (1, "#050508"))
        + lg("lit", (0, "#e6fbff"), (.5, "#6ad8ff"), (1, "#2a7aff"))
        + rg("litGlow", (0, "#7af0ff", .85), (1, "#7af0ff", 0))
        + lg("body", (0, "#2a1458"), (1, "#0c0428"))
        + lg("note", (0, "#fff6a8"), (.5, "#ffc234"), (1, "#e07400"))
        + rg("noteGlow", (0, "#ffd84a", .6), (1, "#ffd84a", 0))
    )
    # falling tiles in 4 lanes
    lanes = [118, 202, 286, 370]
    tiles = [(0, 40, 120), (2, -30, 150), (1, 150, 110), (3, 90, 130)]
    T = []
    for lane, y, h in tiles:
        x = lanes[lane]
        T.append(f'<rect x="{x+8}" y="{y-90}" width="68" height="90" fill="url(#streak)"/>'
                 f'<g filter="url(#sh2)"><rect x="{x}" y="{y}" width="84" height="{h}" rx="12" fill="url(#tile)" stroke="#000" stroke-opacity=".6" stroke-width="3"/></g>'
                 f'<rect x="{x+8}" y="{y+6}" width="10" height="{h-16}" rx="5" fill="#fff" opacity=".22"/>'
                 f'<rect x="{x+6}" y="{y+3}" width="72" height="5" rx="2.5" fill="url(#tileEdge)"/>')
    # keyboard in perspective (top edge narrower)
    top_y, bot_y = 352, 512
    keys = []
    n = 9
    for i in range(n):
        x0t = 70 + (372 / n) * i; x1t = 70 + (372 / n) * (i + 1)
        x0b = -20 + (552 / n) * i; x1b = -20 + (552 / n) * (i + 1)
        fill = "url(#lit)" if i == 4 else "url(#white)"
        keys.append(f'<path d="M{x0t+1.5:.1f} {top_y} L{x1t-1.5:.1f} {top_y} L{x1b-2:.1f} {bot_y} L{x0b+2:.1f} {bot_y} Z" fill="{fill}" stroke="#2a1458" stroke-width="3"/>')
    blacks = []
    for i in [0, 1, 3, 4, 5, 7]:
        f = i + .68
        x0t = 70 + (372 / n) * f; x1t = x0t + (372 / n) * .64
        x0b = -20 + (552 / n) * f; x1b = x0b + (552 / n) * .64
        yb = top_y + (bot_y - top_y) * .58
        xb0 = x0t + (x0b - x0t) * .58; xb1 = x1t + (x1b - x1t) * .58
        blacks.append(f'<path d="M{x0t:.1f} {top_y} L{x1t:.1f} {top_y} L{xb1:.1f} {yb:.1f} L{xb0:.1f} {yb:.1f} Z" fill="url(#black)" stroke="#000" stroke-width="2"/>'
                      f'<path d="M{x0t+4:.1f} {top_y+4} L{x0t+9:.1f} {top_y+4} L{xb0+8:.1f} {yb-8:.1f} L{xb0+3:.1f} {yb-8:.1f} Z" fill="#fff" opacity=".25"/>')
    kx = (70 + 372 / n * 4.5 + (-20 + 552 / n * 4.5)) / 2
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
{bokeh(21, "#ffffff", 16, 6, 30, (.06, .22))}
{''.join(T)}
<!-- keyboard -->
<path d="M54 336 L458 336 L540 512 L-28 512 Z" fill="url(#body)"/>
<path d="M54 336 L458 336" stroke="#c9a8ff" stroke-width="4" opacity=".7"/>
<g filter="url(#sh)">{''.join(keys)}{''.join(blacks)}</g>
<circle cx="{kx:.0f}" cy="420" r="120" fill="url(#litGlow)"/>
<ellipse cx="{kx:.0f}" cy="420" rx="70" ry="26" fill="none" stroke="#e6fbff" stroke-width="7" filter="url(#glowS)"/>
<ellipse cx="{kx:.0f}" cy="420" rx="110" ry="42" fill="none" stroke="#bff6ff" stroke-width="3" opacity=".6"/>
<g fill="#e6fbff">{''.join(f'<circle cx="{kx + dx:.0f}" cy="{420 + dy:.0f}" r="{r}"/>' for dx, dy, r in [(-120, -40, 4), (126, -30, 5), (-90, -70, 3), (96, -78, 4), (0, -96, 5)])}</g>
<!-- notes -->
<circle cx="430" cy="236" r="70" fill="url(#noteGlow)"/>
<g transform="translate(402 214) rotate(10)" filter="url(#sh2)" stroke="#6a3400" stroke-width="5" stroke-linejoin="round">
  <ellipse cx="-2" cy="74" rx="28" ry="21" fill="url(#note)" transform="rotate(-22 -2 74)"/>
  <ellipse cx="62" cy="58" rx="28" ry="21" fill="url(#note)" transform="rotate(-22 62 58)"/>
  <path d="M20 68 V-18 L84 -36 V52 L76 52 V-8 L28 4 V68 Z" fill="url(#note)"/>
</g>
<g transform="translate(70 250) rotate(-12)" filter="url(#sh2)" stroke="#6a3400" stroke-width="4" stroke-linejoin="round">
  <ellipse cx="0" cy="46" rx="20" ry="15" fill="url(#note)" transform="rotate(-22 0 46)"/>
  <path d="M15 42 V-20 Q40 -10 42 14 Q30 0 21 0 V42 Z" fill="url(#note)"/>
</g>
{sparkle(446, 120, .9, "#fff6c0")}{sparkle(56, 160, .6)}{sparkle(250, 300, .5, "#e6fbff")}
'''
    return icon(defs, art)
