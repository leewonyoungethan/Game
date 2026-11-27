"""Blockade — a glossy 9x9 board seen at an angle: a red pawn and a blue pawn face off while
golden wooden walls block the paths between the squares."""
from .common import icon, lg, rg, sparkle

def pawn(x, y, s, a, b, dark):
    gid = f"pw{a[1:]}"
    return (f'<radialGradient id="{gid}" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#ffffff"/><stop offset=".25" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>'
            f'<g transform="translate({x} {y}) scale({s})" filter="url(#sh)">'
            f'<ellipse cx="0" cy="40" rx="40" ry="14" fill="{b}" stroke="{dark}" stroke-width="5"/>'
            f'<path d="M-34 40 Q-30 0 -14 -10 L14 -10 Q30 0 34 40 Z" fill="url(#{gid})" stroke="{dark}" stroke-width="5" stroke-linejoin="round"/>'
            f'<ellipse cx="0" cy="-10" rx="20" ry="7" fill="{b}" stroke="{dark}" stroke-width="5"/>'
            f'<circle cx="0" cy="-36" r="26" fill="url(#{gid})" stroke="{dark}" stroke-width="5"/>'
            f'<ellipse cx="-9" cy="-46" rx="8" ry="5" fill="#fff" opacity=".7"/>'
            f'<path d="M-24 16 Q-18 2 -6 -4" stroke="#fff" stroke-width="5" fill="none" opacity=".45" stroke-linecap="round"/></g>')

def build():
    defs = (rg("bg", (0, "#4a5ad8"), (.6, "#22287a"), (1, "#0e1038"), cx=.5, cy=.35, r=.85)
            + lg("boardTop", (0, "#f4d8a8"), (1, "#d8a868"))
            + lg("boardSide", (0, "#a8682e"), (1, "#6a3a14"))
            + lg("wall", (0, "#ffe08a"), (.5, "#f0b030"), (1, "#c8801a"))
            + lg("wallTop", (0, "#fff3c0"), (1, "#ffd870")))
    N, S = 9, 32
    W = N * S
    cells = ""
    for r in range(N):
        for c in range(N):
            fill = "#e8c088" if (r + c) % 2 else "#f2d4a0"
            if r == 0: fill = "#ffb0b8" if c % 2 else "#ffc4ca"
            if r == N - 1: fill = "#b0ccff" if c % 2 else "#c4d8ff"
            cells += f'<rect x="{c * S + 2}" y="{r * S + 2}" width="{S - 4}" height="{S - 4}" rx="5" fill="{fill}"/>'
    # walls in board coordinates: (x, y, horizontal?)
    walls = [(2, 3, True), (5, 5, True), (6, 2, False), (3, 6, False), (1, 7, True)]
    wl = ""
    for wx, wy, h in walls:
        if h: wl += f'<rect x="{wx * S + 2}" y="{wy * S - 5}" width="{2 * S - 4}" height="10" rx="4" fill="url(#wall)" stroke="#8a5000" stroke-width="2.5"/>'
        else: wl += f'<rect x="{wx * S - 5}" y="{wy * S + 2}" width="10" height="{2 * S - 4}" rx="4" fill="url(#wall)" stroke="#8a5000" stroke-width="2.5"/>'
    # the board is drawn flat then put in perspective with a matrix
    board = (f'<rect x="-14" y="-14" width="{W + 28}" height="{W + 28}" rx="18" fill="url(#boardTop)" stroke="#6a3a14" stroke-width="5"/>'
             f'{cells}{wl}')
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
<g fill="#fff">{''.join(f'<circle cx="{(i * 97) % 512}" cy="{(i * 61) % 200}" r="{1 + (i % 3) * .6}" opacity="{.3 + (i % 4) * .12}"/>' for i in range(36))}</g>
<!-- board thickness -->
<ellipse cx="256" cy="420" rx="230" ry="26" fill="#000" opacity=".35"/>
<path d="M86 368 L450 368 L450 400 L86 400 Z" fill="url(#boardSide)" stroke="#4a2408" stroke-width="4"/>
<path d="M450 368 L399 172 L399 200 L450 400 Z" fill="#7a4418" stroke="#4a2408" stroke-width="4"/>
<g transform="matrix(1.15 0 0.16 .62 36 172) translate(14 14)" filter="url(#sh2)">{board}</g>
<!-- a big wall being placed, floating above the board -->
<g transform="translate(250 150) rotate(-8)" filter="url(#sh)">
  <rect x="-80" y="-14" width="160" height="34" rx="9" fill="url(#wall)" stroke="#8a5000" stroke-width="5"/>
  <rect x="-80" y="-26" width="160" height="16" rx="7" fill="url(#wallTop)" stroke="#8a5000" stroke-width="4"/>
  <path d="M-60 2 H40" stroke="#fff" stroke-width="5" opacity=".5" stroke-linecap="round"/>
</g>
<g stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"><path d="M200 196 v22 M250 196 v30 M300 190 v22"/></g>
{pawn(140, 236, 1.0, "#ff5a6a", "#c81a3a", "#6a0a18")}
{pawn(352, 306, 1.1, "#4a9aff", "#1a4ad8", "#0a1a6a")}
{sparkle(420, 120, .9, "#fff6c0")}{sparkle(80, 110, .55)}{sparkle(470, 440, .5)}
'''
    return icon(defs, art)
