"""별빛 기사 — a brave little knight with a glowing sword and a throwing star, castle at night."""
from .common import icon, lg, rg, rays, stars, sparkle, star_path

def build():
    defs = (
        rg("sky", (0, "#5a6ae8"), (.5, "#2a248a"), (1, "#0a0828"), cy=.32, r=.9)
        + lg("castle", (0, "#1e1a5a"), (1, "#100c34"))
        + lg("helm", (0, "#ffffff"), (.35, "#dfe6f4"), (.7, "#9aa8c4"), (1, "#5c6884"), x1=0, y1=0, x2=1, y2=1)
        + lg("helmSide", (0, "#8a98b8"), (1, "#4a5674"))
        + lg("gold", (0, "#fff6b0"), (.45, "#ffcc2a"), (1, "#c07800"))
        + lg("plume", (0, "#ff8a7a"), (.5, "#ff3a4a"), (1, "#a80c24"))
        + lg("cape", (0, "#ff5a5a"), (.6, "#c81a2a"), (1, "#6a0614"))
        + lg("visor", (0, "#0a1230"), (1, "#1a2a5a"))
        + rg("eyeGlow", (0, "#e6f6ff"), (.4, "#7ac8ff", .9), (1, "#7ac8ff", 0))
        + lg("blade", (0, "#ffffff"), (.5, "#e2ecff"), (1, "#8aa4dc"), x1=0, y1=0, x2=1, y2=0)
        + rg("bladeGlow", (0, "#bfe2ff", .85), (1, "#7ab8ff", 0))
        + rg("star", (0, "#fffbe0"), (.45, "#ffd84a"), (1, "#e08a00"), cx=.4, cy=.35)
        + rg("starGlow", (0, "#ffe680", .9), (1, "#ffc634", 0))
        + lg("armor", (0, "#c8d2e6"), (1, "#6a7896"))
    )
    O = 'stroke="#141a3a" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(17, 60, (0, 0, 512, 380))}
{rays("#c8d4ff", .07, 18, 236, 240)}
<g fill="url(#castle)">
  <path d="M0 410 L0 350 L26 350 L26 330 L44 330 L44 350 L66 350 L66 300 L58 300 L82 262 L106 300 L98 300 L98 380 L160 380 L160 512 L0 512 Z"/>
  <path d="M512 410 L512 340 L488 340 L488 320 L470 320 L470 340 L446 340 L446 286 L438 286 L462 246 L486 286 L478 286 L478 300 L420 300 L420 380 L352 380 L352 512 L512 512 Z"/>
</g>
<g fill="#ffd27a" opacity=".85"><rect x="76" y="310" width="10" height="16" rx="5"/><rect x="456" y="296" width="10" height="16" rx="5"/></g>
<rect y="440" width="512" height="72" fill="#0c0a2a"/>
<ellipse cx="236" cy="470" rx="160" ry="22" fill="#000" opacity=".55" filter="url(#b14)"/>
<!-- cape -->
<path d="M118 330 Q80 430 60 500 L210 470 L236 360 Z" fill="url(#cape)" {O}/>
<path d="M354 330 Q392 430 412 500 L262 470 L236 360 Z" fill="url(#cape)" {O}/>
<path d="M90 450 Q110 400 126 360" stroke="#ff9a9a" stroke-width="5" fill="none" opacity=".5" stroke-linecap="round"/>
<!-- body / pauldrons -->
<path d="M140 380 Q236 340 332 380 L336 470 Q236 500 136 470 Z" fill="url(#armor)" {O}/>
<path d="M150 400 Q236 372 322 400" stroke="url(#gold)" stroke-width="10" fill="none"/>
<ellipse cx="128" cy="372" rx="50" ry="36" fill="url(#helm)" {O}/><ellipse cx="344" cy="372" rx="50" ry="36" fill="url(#helm)" {O}/>
<!-- plume -->
<g filter="url(#sh2)">
  <path d="M236 108 Q250 44 326 34 Q300 56 300 80 Q340 64 372 84 Q330 92 314 118 Q346 118 360 140 Q300 136 262 146 Z" fill="url(#plume)" {O}/>
  <path d="M262 104 Q290 70 320 56 M276 124 Q314 100 350 96" stroke="#ffb0a0" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/>
</g>
<!-- helmet -->
<g filter="url(#sh)">
  <path d="M120 250 Q120 120 236 114 Q352 120 352 250 L352 316 Q352 380 236 392 Q120 380 120 316 Z" fill="url(#helm)" {O}/>
</g>
<path d="M300 132 Q352 160 352 250 L352 316 Q350 360 300 380 Q330 330 330 250 Q330 170 300 132 Z" fill="url(#helmSide)" opacity=".55"/>
<path d="M236 116 V226" stroke="url(#gold)" stroke-width="16"/>
<path d="M236 116 V226" stroke="#141a3a" stroke-width="3" opacity=".3"/>
<rect x="146" y="226" width="180" height="46" rx="16" fill="url(#visor)" {O}/>
<path d="M164 262 H308" stroke="#2a3a6a" stroke-width="3"/>
<circle cx="194" cy="248" r="34" fill="url(#eyeGlow)"/><circle cx="278" cy="248" r="34" fill="url(#eyeGlow)"/>
<rect x="176" y="240" width="36" height="14" rx="7" fill="#eaf8ff"/><rect x="260" y="240" width="36" height="14" rx="7" fill="#eaf8ff"/>
<g fill="#141a3a" opacity=".55">{''.join(f'<circle cx="{x}" cy="{y}" r="3.5"/>' for x, y in [(186, 300), (206, 306), (226, 308), (246, 308), (266, 306), (286, 300)])}</g>
<path d="M150 312 Q236 350 322 312" stroke="url(#gold)" stroke-width="10" fill="none" stroke-linecap="round"/>
<path d="M146 170 Q176 130 226 122" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".75"/>
<path d="M142 214 Q140 190 146 172" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".5"/>
<!-- sword -->
<g transform="translate(424 452) rotate(-10)">
  <ellipse cx="0" cy="-190" rx="44" ry="200" fill="url(#bladeGlow)"/>
  <g filter="url(#sh)" {O}>
    <path d="M-17 -40 L-17 -330 L0 -372 L17 -330 L17 -40 Z" fill="url(#blade)"/>
    <rect x="-56" y="-46" width="112" height="24" rx="12" fill="url(#gold)"/>
    <rect x="-11" y="-24" width="22" height="58" rx="6" fill="#6a3a1a"/>
    <circle cx="0" cy="44" r="15" fill="url(#gold)"/>
  </g>
  <path d="M0 -350 V-60" stroke="#fff" stroke-width="5" opacity=".85"/>
  <circle cx="0" cy="-34" r="6" fill="#ff4a5a" stroke="#141a3a" stroke-width="3"/>
</g>
<!-- throwing star -->
<circle cx="88" cy="150" r="78" fill="url(#starGlow)"/>
<g transform="rotate(-14 88 150)" filter="url(#sh2)">
  <path d="{star_path(88, 150, 50, .46)}" fill="url(#star)" stroke="#8a5000" stroke-width="5" stroke-linejoin="round"/>
  <path d="{star_path(88, 150, 22, .46)}" fill="#fff6c0" opacity=".6"/>
</g>
<g stroke="#ffe680" stroke-width="4" stroke-linecap="round" opacity=".6"><path d="M30 196 L56 176 M24 170 L50 160 M40 222 L64 196"/></g>
{sparkle(470, 70, .9)}{sparkle(300, 64, .5, "#fff6c0")}{sparkle(40, 300, .6)}
'''
    return icon(defs, art)
