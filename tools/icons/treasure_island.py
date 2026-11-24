"""보물섬 탐사 — a tiny island with a palm tree, dig-site numbers and a glowing open treasure chest."""
from .common import icon, lg, rg, sparkle

def build():
    defs = (
        lg("sea", (0, "#3ad0f0"), (.6, "#1a8ab8"), (1, "#0a4a6a"))
        + rg("sun", (0, "#fffbe0", .9), (1, "#fffbe0", 0))
        + rg("sand", (0, "#fff2c8"), (.7, "#f0d08a"), (1, "#c89a50"), cx=.45, cy=.35)
        + lg("grass", (0, "#9af06a"), (1, "#3a9a3a"))
        + lg("trunk", (0, "#c08a4a"), (1, "#7a4a1a"), x1=0, y1=0, x2=1, y2=0)
        + lg("leaf", (0, "#7ae05a"), (1, "#1e7a2a"))
        + lg("chest", (0, "#c87a3a"), (1, "#7a3a12"))
        + lg("lid", (0, "#e09a5a"), (1, "#9a5020"))
        + lg("gold", (0, "#fff6b0"), (.5, "#ffd23a"), (1, "#d08a00"))
        + rg("goldGlow", (0, "#ffe680", .95), (.5, "#ffc634", .35), (1, "#ffc634", 0))
    )
    O = 'stroke="#3a1c06" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    waves = "".join(f'<path d="M-10 {y} q24 -10 48 0 t48 0 t48 0 t48 0 t48 0 t48 0 t48 0 t48 0 t48 0 t48 0 t48 0" stroke="#fff" stroke-opacity=".22" stroke-width="4" fill="none"/>' for y in (60, 110, 440, 490))
    tiles = []
    for i, (x, y, n, col) in enumerate([(98, 300, "1", "#2a7ad8"), (146, 300, "2", "#2a9a4a"), (98, 348, "", ""), (146, 348, "1", "#2a7ad8")]):
        tiles.append(f'<rect x="{x}" y="{y}" width="44" height="44" rx="9" fill="#f6e2b0" stroke="#b8904a" stroke-width="3"/>' + (f'<text x="{x+22}" y="{y+33}" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="28" fill="{col}">{n}</text>' if n else ""))
    for x, y in [(194, 300), (194, 348), (98, 396), (146, 396)]:
        tiles.append(f'<rect x="{x}" y="{y}" width="44" height="44" rx="9" fill="url(#grass)" stroke="#2a6a2a" stroke-width="3"/><rect x="{x+6}" y="{y+5}" width="32" height="7" rx="3.5" fill="#fff" opacity=".35"/>')
    art = f'''
<rect width="512" height="512" fill="url(#sea)"/>
<circle cx="420" cy="80" r="150" fill="url(#sun)"/>
{waves}
<ellipse cx="256" cy="380" rx="236" ry="112" fill="#fff" opacity=".35"/>
<g filter="url(#sh)"><ellipse cx="256" cy="366" rx="222" ry="100" fill="url(#sand)" stroke="#a87a3a" stroke-width="5"/></g>
<ellipse cx="200" cy="330" rx="150" ry="56" fill="#fff" opacity=".18"/>
{''.join(tiles)}
<!-- palm tree -->
<path d="M396 340 Q380 250 352 150" stroke="url(#trunk)" stroke-width="26" fill="none" stroke-linecap="round"/>
<path d="M392 320 l-18 -6 M384 280 l-18 -6 M374 240 l-18 -6 M364 200 l-16 -6" stroke="#5a3010" stroke-width="5" stroke-linecap="round"/>
<g {O} fill="url(#leaf)" stroke="#145a1e">
  <path d="M352 150 Q300 110 250 140 Q300 130 340 160 Z"/><path d="M352 150 Q330 80 270 70 Q320 100 344 150 Z"/>
  <path d="M352 150 Q400 90 460 110 Q400 116 360 158 Z"/><path d="M352 150 Q420 150 460 200 Q400 170 356 160 Z"/>
  <path d="M352 150 Q360 90 400 60 Q372 110 360 154 Z"/>
</g>
<circle cx="346" cy="162" r="10" fill="#6a3a12"/><circle cx="362" cy="166" r="10" fill="#7a4a1a"/>
<!-- X mark + chest -->
<path d="M246 392 l30 30 M276 392 l-30 30" stroke="#e8302a" stroke-width="10" stroke-linecap="round"/>
<circle cx="316" cy="356" r="110" fill="url(#goldGlow)"/>
<g filter="url(#sh)">
  <path d="M254 352 L378 352 L374 420 Q316 432 258 420 Z" fill="url(#chest)" {O}/>
  <path d="M254 352 Q256 300 316 296 Q376 300 378 352 Z" fill="url(#lid)" {O} transform="rotate(-26 254 352) translate(-6 -18)"/>
  <ellipse cx="316" cy="352" rx="60" ry="16" fill="url(#gold)" stroke="#8a5a00" stroke-width="4"/>
  <g fill="url(#gold)" stroke="#8a5a00" stroke-width="3"><circle cx="290" cy="342" r="12"/><circle cx="318" cy="336" r="13"/><circle cx="344" cy="344" r="11"/><circle cx="304" cy="326" r="10"/></g>
  <rect x="304" y="372" width="24" height="26" rx="5" fill="url(#gold)" stroke="#3a1c06" stroke-width="4"/>
  <path d="M260 388 H372" stroke="#3a1c06" stroke-width="5" opacity=".5"/>
</g>
<g fill="url(#gold)" stroke="#8a5a00" stroke-width="3"><circle cx="234" cy="452" r="11"/><circle cx="408" cy="430" r="9"/></g>
{sparkle(316, 300, 1.0, "#fff6c0")}{sparkle(380, 320, .6, "#fff6c0")}{sparkle(80, 160, .6)}{sparkle(200, 240, .45)}
'''
    return icon(defs, art)
