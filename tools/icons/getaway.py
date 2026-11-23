"""도둑차 대탈주 — a yellow getaway car drifting through a night intersection, sirens closing in."""
from .common import icon, lg, rg, sparkle

def car(body, roof, glass, stroke="#2a1a00"):
    """Top-down car, nose pointing up (-y), centred at 0,0, ~ 120x230."""
    O = f'stroke="{stroke}" stroke-width="6" stroke-linejoin="round"'
    return f'''
  <rect x="-66" y="-84" width="20" height="44" rx="7" fill="#0c0c12"/><rect x="46" y="-84" width="20" height="44" rx="7" fill="#0c0c12"/>
  <rect x="-66" y="52" width="20" height="46" rx="7" fill="#0c0c12"/><rect x="46" y="52" width="20" height="46" rx="7" fill="#0c0c12"/>
  <path d="M-52 -96 Q-56 -126 -20 -130 L20 -130 Q56 -126 52 -96 L60 92 Q60 122 24 124 L-24 124 Q-60 122 -60 92 Z" fill="{body}" {O}/>
  <path d="M-40 -60 Q0 -78 40 -60 L36 -20 L-36 -20 Z" fill="{glass}" {O}/>
  <path d="M-36 -20 L36 -20 L38 54 L-38 54 Z" fill="{roof}" {O}/>
  <path d="M-38 54 L38 54 L32 86 Q0 94 -32 86 Z" fill="{glass}" {O}/>
  <path d="M-30 -64 L-8 -70 L-22 -26 L-34 -26 Z" fill="#fff" opacity=".45"/>
  <path d="M-62 -40 l-12 -4 l2 12 Z M62 -40 l12 -4 l-2 12 Z" fill="{body}" {O}/>
'''

def build():
    defs = (
        lg("asph", (0, "#262a3c"), (1, "#0c0e18"), x2=1, y2=1)
        + rg("red", (0, "#ff2a48", .95), (.45, "#ff2a48", .4), (1, "#ff2a48", 0))
        + rg("blue", (0, "#2a78ff", .95), (.45, "#2a78ff", .4), (1, "#2a78ff", 0))
        + lg("body", (0, "#fff6a0"), (.3, "#ffd21a"), (.7, "#f0a400"), (1, "#a86a00"), x1=0, y1=0, x2=1, y2=0)
        + lg("roof", (0, "#ffe46a"), (1, "#d88a00"), x1=0, y1=0, x2=1, y2=0)
        + lg("glass", (0, "#a8dcff"), (.4, "#2a4a7a"), (1, "#0a1428"))
        + lg("cop", (0, "#ffffff"), (1, "#b8c2d6"), x1=0, y1=0, x2=1, y2=0)
        + lg("copRoof", (0, "#1e2a5a"), (1, "#0a1230"))
        + lg("beam", (0, "#fff8d0", .6), (1, "#fff8d0", 0), x1=0, y1=1, x2=0, y2=0)
        + lg("flame", (0, "#ffffff"), (.3, "#9aefff"), (1, "#2a6aff", 0), x1=0, y1=0, x2=0, y2=1)
        + rg("smoke", (0, "#e6e8f2", .85), (1, "#e6e8f2", 0))
        + lg("bill", (0, "#b8f8a8"), (1, "#2e9a4a"))
        + lg("bldg", (0, "#2e3450"), (1, "#1a1e30"))
    )
    art = f'''
<rect width="512" height="512" fill="url(#asph)"/>
<!-- city blocks -->
<g fill="url(#bldg)" stroke="#3c4466" stroke-width="3">
  <rect x="-20" y="-20" width="170" height="150" rx="16"/><rect x="362" y="-20" width="170" height="150" rx="16"/>
  <rect x="-20" y="382" width="170" height="150" rx="16"/><rect x="362" y="382" width="170" height="150" rx="16"/>
</g>
<g fill="#ffd58c" opacity=".5"><rect x="24" y="24" width="10" height="10"/><rect x="60" y="64" width="10" height="10"/><rect x="104" y="30" width="10" height="10"/><rect x="400" y="40" width="10" height="10"/><rect x="452" y="86" width="10" height="10"/><rect x="40" y="420" width="10" height="10"/><rect x="430" y="452" width="10" height="10"/><rect x="96" y="470" width="10" height="10"/></g>
<rect x="150" y="0" width="4" height="130" fill="#ff4fd8" opacity=".8"/><rect x="358" y="382" width="4" height="130" fill="#3ff0ff" opacity=".8"/>
<!-- crosswalk -->
<g fill="#ffffff" opacity=".18">{''.join(f'<rect x="{170+i*30}" y="140" width="16" height="44"/>' for i in range(6))}</g>
<g stroke="#ffd27a" stroke-width="6" stroke-dasharray="30 26" opacity=".35"><path d="M256 190 V512"/><path d="M0 256 H140 M372 256 H512"/></g>
<!-- skid marks -->
<g stroke="#000" stroke-width="18" fill="none" opacity=".6" stroke-linecap="round"><path d="M40 500 Q110 400 190 340"/><path d="M100 520 Q170 430 236 374"/></g>
<!-- siren light -->
<circle cx="0" cy="0" r="300" fill="url(#red)"/><circle cx="512" cy="0" r="300" fill="url(#blue)"/>
<circle cx="0" cy="512" r="200" fill="url(#blue)" opacity=".55"/><circle cx="512" cy="512" r="200" fill="url(#red)" opacity=".55"/>
<!-- tire smoke -->
<g filter="url(#b6)"><circle cx="150" cy="380" r="46" fill="url(#smoke)"/><circle cx="110" cy="420" r="58" fill="url(#smoke)"/><circle cx="196" cy="420" r="40" fill="url(#smoke)"/><circle cx="70" cy="470" r="50" fill="url(#smoke)" opacity=".7"/></g>
<!-- police cars at corners -->
<g transform="translate(62 64) rotate(135)" filter="url(#sh2)">{car("url(#cop)", "url(#copRoof)", "url(#glass)", "#0a0c18")}
  <rect x="-34" y="-6" width="34" height="18" rx="4" fill="#ff2a48"/><rect x="0" y="-6" width="34" height="18" rx="4" fill="#2a78ff"/></g>
<g transform="translate(456 84) rotate(-150)" filter="url(#sh2)">{car("url(#cop)", "url(#copRoof)", "url(#glass)", "#0a0c18")}
  <rect x="-34" y="-6" width="34" height="18" rx="4" fill="#2a78ff"/><rect x="0" y="-6" width="34" height="18" rx="4" fill="#ff2a48"/></g>
<g filter="url(#glow)"><circle cx="62" cy="64" r="18" fill="#ff8a9a"/><circle cx="456" cy="84" r="18" fill="#8ab8ff"/></g>
<!-- hero car -->
<g transform="translate(266 270) rotate(38)">
  <path d="M-48 -126 L-150 -520 L60 -520 L-20 -126 Z" fill="url(#beam)"/><path d="M20 -126 L-60 -520 L150 -520 L48 -126 Z" fill="url(#beam)"/>
  <path d="M-26 120 L0 230 L26 120 Z" fill="url(#flame)"/>
  <ellipse cx="0" cy="124" rx="20" ry="12" fill="#cff6ff" filter="url(#glowS)"/>
  <g filter="url(#sh)">{car("url(#body)", "url(#roof)", "url(#glass)")}</g>
  <rect x="-12" y="-128" width="24" height="250" fill="#1a1000" opacity=".22"/>
  <rect x="-50" y="-126" width="24" height="12" rx="5" fill="#fffbe0"/><rect x="26" y="-126" width="24" height="12" rx="5" fill="#fffbe0"/>
  <rect x="-52" y="112" width="26" height="9" rx="4" fill="#ff2a3a"/><rect x="26" y="112" width="26" height="9" rx="4" fill="#ff2a3a"/>
  <path d="M-52 -96 Q-46 0 -58 92" fill="none" stroke="#fff" stroke-width="5" opacity=".7" stroke-linecap="round"/>
</g>
<!-- flying cash -->
<g filter="url(#sh2)" stroke="#0a3a14" stroke-width="3">
  <g transform="translate(410 300) rotate(-24)"><rect x="-38" y="-20" width="76" height="40" rx="5" fill="url(#bill)"/><circle r="11" fill="none" stroke="#0a5a24" stroke-width="3"/><path d="M-30 -12 V12 M30 -12 V12" stroke="#0a5a24"/></g>
  <g transform="translate(452 388) rotate(22)"><rect x="-32" y="-17" width="64" height="34" rx="5" fill="url(#bill)"/><circle r="9" fill="none" stroke="#0a5a24" stroke-width="3"/></g>
  <g transform="translate(372 452) rotate(-6)"><rect x="-28" y="-15" width="56" height="30" rx="5" fill="url(#bill)"/><circle r="8" fill="none" stroke="#0a5a24" stroke-width="3"/></g>
</g>
{sparkle(62, 64, 1.0, "#ffe0e6")}{sparkle(456, 84, 1.0, "#e0ecff")}{sparkle(440, 250, .5, "#e8ffe0")}
'''
    return icon(defs, art)
