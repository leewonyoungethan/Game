"""불을 밝혀라 — a 3x3 board of wire tiles at night: glowing golden circuits running from a lightning core to little houses whose windows light up."""
from .common import icon, lg, rg, sparkle, stars

T = 120; X0 = 76; Y0 = 108
# tile masks (N=1,E=2,S=4,W=8) for a solved 3x3 board, centre = power source; (1,2) is still dark (unrotated)
MASKS = [[2, 14, 8], [6, 15, 12], [1, 1, 8]]
KIND = {(0, 0): "house", (2, 0): "house", (0, 2): "house", (1, 2): "house", (2, 2): "house", (1, 1): "src"}
DARK = {(2, 2)}

def tile(c, r):
    x, y = X0 + c * T, Y0 + r * T
    cx, cy = x + T / 2, y + T / 2
    m = MASKS[r][c]; lit = (c, r) not in DARK
    arms = [(dx, dy) for b, dx, dy in [(1, 0, -1), (2, 1, 0), (4, 0, 1), (8, -1, 0)] if m & b]
    d = " ".join(f"M{cx} {cy} L{cx + dx * T / 2} {cy + dy * T / 2}" for dx, dy in arms)
    out = f'<rect x="{x + 6}" y="{y + 6}" width="{T - 12}" height="{T - 12}" rx="18" fill="{"#4a3e22" if lit else "#232a5a"}"/>'
    if lit:
        out += f'<path d="{d}" stroke="#ffd24a" stroke-width="26" stroke-linecap="round" filter="url(#glow)" opacity=".8"/>'
        out += f'<path d="{d}" stroke="url(#wire)" stroke-width="18" stroke-linecap="round"/><path d="{d}" stroke="#fffbe0" stroke-width="6" stroke-linecap="round"/>'
    else:
        out += f'<path d="{d}" stroke="#5a6290" stroke-width="18" stroke-linecap="round"/>'
    k = KIND.get((c, r))
    if k == "house":
        wall, roof, win = ("#f4e6cc", "#e0503a", "#ffe06a") if lit else ("#5a5e88", "#4a3a5e", "#1a1e3a")
        if lit:
            out += f'<circle cx="{cx}" cy="{cy}" r="58" fill="url(#halo)"/>'
        out += (f'<g transform="translate({cx} {cy + 6})" filter="url(#sh2)"><rect x="-30" y="-12" width="60" height="42" rx="5" fill="{wall}" stroke="#2a1a10" stroke-width="4"/>'
                f'<path d="M-40 -8 L0 -42 L40 -8 Z" fill="{roof}" stroke="#2a1a10" stroke-width="4" stroke-linejoin="round"/>'
                f'<rect x="-21" y="-2" width="18" height="16" fill="{win}" stroke="#2a1a10" stroke-width="3"/><rect x="5" y="4" width="15" height="26" fill="#7a4a2a" stroke="#2a1a10" stroke-width="3"/></g>')
    elif k == "src":
        out += (f'<circle cx="{cx}" cy="{cy}" r="70" fill="url(#halo)"/>'
                f'<g filter="url(#sh2)"><circle cx="{cx}" cy="{cy}" r="38" fill="url(#core)" stroke="#8a4a00" stroke-width="5"/></g>'
                f'<path d="M{cx + 6} {cy - 26} L{cx - 16} {cy + 4} L{cx - 2} {cy + 4} L{cx - 8} {cy + 26} L{cx + 16} {cy - 6} L{cx + 2} {cy - 6} Z" fill="#7a3a00" stroke="#7a3a00" stroke-width="3" stroke-linejoin="round"/>')
    else:
        out += f'<circle cx="{cx}" cy="{cy}" r="13" fill="{"#ffe88a" if lit else "#5a6290"}"/>'
    return out

def build():
    defs = (lg("sky", (0, "#0a0e30"), (1, "#2a1a5a"))
            + rg("moon", (0, "#fffbe0"), (1, "#ffe8a0"))
            + lg("wire", (0, "#ffe88a"), (1, "#ffb43a"))
            + rg("halo", (0, "#ffe08a", .6), (1, "#ffe08a", 0))
            + rg("core", (0, "#fffbe0"), (.6, "#ffd24a"), (1, "#ff9a2a"), cx=.38, cy=.32))
    tiles = "".join(tile(c, r) for r in range(3) for c in range(3))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(5, 50, area=(0, 0, 512, 120))}
<circle cx="440" cy="62" r="30" fill="url(#moon)"/><circle cx="452" cy="54" r="26" fill="#141a44"/>
<g filter="url(#sh)"><rect x="{X0 - 14}" y="{Y0 - 14}" width="{3 * T + 28}" height="{3 * T + 28}" rx="34" fill="#0e1236" stroke="#3a4280" stroke-width="4"/></g>
{tiles}
<!-- rotate hint on the dark tile -->
<g transform="translate({X0 + 2.5 * T} {Y0 + 2.5 * T})"><path d="M44 -30 A54 54 0 0 1 40 36" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".9"/><path d="M52 26 L38 44 L26 24 Z" fill="#fff" opacity=".9"/></g>
{sparkle(256, 230, .9, "#fffbe0")}{sparkle(60, 60, .5)}{sparkle(470, 470, .5)}
'''
    return icon(defs, art)
