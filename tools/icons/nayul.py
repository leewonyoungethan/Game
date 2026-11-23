"""나율이 키우기 — a cheerful baby with a rattle, floating hearts on a pastel sky."""
from .common import icon, lg, rg, rays, bokeh, sparkle, heart_path, star_path

def build():
    defs = (
        rg("bg", (0, "#fffbe0"), (.5, "#ffd6e6"), (1, "#ff8ab8"), cy=.42, r=.82)
        + rg("skin", (0, "#fff4e8"), (.6, "#ffe0c6"), (.88, "#f8c49e"), (1, "#e8a47a"), cx=.42, cy=.38, r=.62)
        + rg("ear", (0, "#ffe0c6"), (1, "#eaa880"))
        + lg("hair", (0, "#a8683a"), (.6, "#7a4420"), (1, "#4a2610"))
        + rg("iris", (0, "#8a5a3a"), (.55, "#4a2a18"), (1, "#1a0c06"), cx=.5, cy=.65)
        + rg("blush", (0, "#ff7a9a", .7), (1, "#ff7a9a", 0))
        + rg("heart", (0, "#ffc2d6"), (.5, "#ff4f80"), (1, "#c40f4a"), cx=.35, cy=.3)
        + lg("mouth", (0, "#c8284a"), (1, "#7a0c22"))
        + lg("tongue", (0, "#ff9ab0"), (1, "#ff6a8a"))
        + lg("bib", (0, "#ffffff"), (1, "#e6f2ff"))
        + lg("onesie", (0, "#9ad8ff"), (1, "#4aa8e8"))
        + rg("rattle", (0, "#fff8c0"), (.5, "#ffd23a"), (1, "#e09000"), cx=.35, cy=.3)
        + lg("handle", (0, "#ff9ac0"), (1, "#e0507a"))
    )
    O = 'stroke="#8a4a2a" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .24, 20, 256, 250)}
{bokeh(9, "#ffffff", 14, 6, 22, (.3, .7))}
<ellipse cx="256" cy="492" rx="170" ry="26" fill="#c03070" opacity=".3" filter="url(#b14)"/>
<!-- body -->
<path d="M120 512 Q124 420 200 404 L312 404 Q388 420 392 512 Z" fill="url(#onesie)" {O}/>
<path d="M190 404 Q256 450 322 404 Q300 446 256 452 Q212 446 190 404 Z" fill="url(#bib)" stroke="#8aa8c8" stroke-width="4"/>
<g filter="url(#sh)">
  <circle cx="92" cy="262" r="42" fill="url(#ear)" {O}/>
  <circle cx="420" cy="262" r="42" fill="url(#ear)" {O}/>
  <ellipse cx="256" cy="256" rx="172" ry="164" fill="url(#skin)" {O}/>
</g>
<circle cx="94" cy="264" r="18" fill="#e8a07a" opacity=".55"/><circle cx="418" cy="264" r="18" fill="#e8a07a" opacity=".55"/>
<!-- hair -->
<path d="M96 222 Q96 100 256 92 Q416 100 416 222 Q396 160 330 146 Q316 176 280 170 Q292 150 280 134 Q256 168 210 160 Q222 144 214 130 Q170 160 152 150 Q120 170 96 222 Z" fill="url(#hair)" stroke="#3a1a08" stroke-width="5" stroke-linejoin="round"/>
<path d="M244 96 Q238 40 290 34 Q336 34 330 76 Q324 54 296 58 Q268 62 276 92" fill="url(#hair)" stroke="#3a1a08" stroke-width="5" stroke-linejoin="round"/>
<path d="M150 134 Q200 104 252 104 M300 108 Q340 114 370 138" stroke="#d8a070" stroke-width="7" fill="none" stroke-linecap="round" opacity=".7"/>
<!-- face light -->
<ellipse cx="200" cy="190" rx="80" ry="36" fill="#fff" opacity=".28" transform="rotate(-18 200 190)"/>
<!-- eyes -->
<g>
  <ellipse cx="184" cy="266" rx="38" ry="46" fill="url(#iris)"/><ellipse cx="328" cy="266" rx="38" ry="46" fill="url(#iris)"/>
  <ellipse cx="184" cy="266" rx="38" ry="46" fill="none" stroke="#1a0c06" stroke-width="4"/><ellipse cx="328" cy="266" rx="38" ry="46" fill="none" stroke="#1a0c06" stroke-width="4"/>
  <circle cx="198" cy="246" r="15" fill="#fff"/><circle cx="342" cy="246" r="15" fill="#fff"/>
  <circle cx="172" cy="286" r="7" fill="#fff" opacity=".9"/><circle cx="316" cy="286" r="7" fill="#fff" opacity=".9"/>
  <path d="M168 300 Q184 310 200 300 M312 300 Q328 310 344 300" stroke="#c89a7a" stroke-width="4" fill="none" opacity=".5"/>
  <path d="M142 236 Q150 220 164 226 M370 236 Q362 220 348 226" stroke="#3a1a08" stroke-width="5" fill="none" stroke-linecap="round"/>
</g>
<path d="M156 206 Q180 194 204 204 M308 204 Q332 194 356 206" stroke="#8a5430" stroke-width="7" fill="none" stroke-linecap="round" opacity=".75"/>
<ellipse cx="126" cy="328" rx="46" ry="28" fill="url(#blush)"/><ellipse cx="386" cy="328" rx="46" ry="28" fill="url(#blush)"/>
<!-- nose & mouth -->
<path d="M246 306 Q256 316 266 306" stroke="#d08a60" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M214 334 Q256 392 298 334 Q256 350 214 334 Z" fill="url(#mouth)" stroke="#6a1020" stroke-width="5" stroke-linejoin="round"/>
<path d="M232 360 Q256 382 280 360 Q256 350 232 360 Z" fill="url(#tongue)"/>
<path d="M224 340 Q256 350 288 340" stroke="#fff" stroke-width="5" fill="none" opacity=".85"/>
<!-- hands + rattle -->
<g transform="translate(402 400) rotate(18)" filter="url(#sh2)">
  <rect x="-9" y="-10" width="18" height="96" rx="9" fill="url(#handle)" stroke="#8a2a4a" stroke-width="4"/>
  <circle cx="0" cy="-48" r="44" fill="url(#rattle)" stroke="#8a5a00" stroke-width="5"/>
  <path d="{star_path(0, -48, 20, .48)}" fill="#ff6a9a" stroke="#8a2a4a" stroke-width="3" stroke-linejoin="round"/>
  <ellipse cx="-16" cy="-66" rx="10" ry="14" fill="#fff" opacity=".85"/>
</g>
<g filter="url(#sh2)"><ellipse cx="394" cy="440" rx="34" ry="28" fill="url(#skin)" {O}/><path d="M374 432 q10 -10 22 -4 M380 448 q10 -8 22 -2" stroke="#c88a60" stroke-width="4" fill="none" stroke-linecap="round"/></g>
<g filter="url(#sh2)"><ellipse cx="128" cy="446" rx="32" ry="26" fill="url(#skin)" {O}/></g>
<!-- hearts -->
<g filter="url(#sh2)" stroke="#9a0c3a" stroke-width="5" stroke-linejoin="round">
  <path d="{heart_path(70, 104, 34)}" fill="url(#heart)"/>
  <path d="{heart_path(448, 128, 26)}" fill="url(#heart)"/>
  <path d="{heart_path(468, 340, 18)}" fill="url(#heart)"/>
</g>
<g fill="#fff" opacity=".85"><ellipse cx="58" cy="94" rx="9" ry="6" transform="rotate(-30 58 94)"/><ellipse cx="440" cy="120" rx="7" ry="5" transform="rotate(-30 440 120)"/></g>
{sparkle(176, 60, .7)}{sparkle(400, 196, .6)}{sparkle(52, 380, .6)}
'''
    return icon(defs, art)
