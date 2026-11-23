"""여우의 달걀 도둑 — a sly fox clutching a glowing golden egg under the moon."""
from .common import icon, lg, rg, stars, sparkle

def build():
    defs = (
        rg("sky", (0, "#5b3fc8"), (.55, "#2a1670"), (1, "#0d0630"), cx=.72, cy=.2, r=1)
        + rg("moon", (0, "#fffef4"), (.75, "#fff1c0"), (1, "#f0cf78"), cx=.4, cy=.35)
        + rg("moonGlow", (0, "#fff0b8", .55), (.5, "#c8a8ff", .18), (1, "#c8a8ff", 0))
        + lg("fur", (0, "#ffb050"), (.45, "#ff7a1c"), (1, "#c4440a"))
        + lg("furDark", (0, "#d85a14"), (1, "#8a2a04"))
        + lg("cream", (0, "#ffffff"), (1, "#f2dcc2"))
        + lg("earIn", (0, "#4a1a0a"), (1, "#8a3a1a"))
        + rg("iris", (0, "#fffcb0"), (.55, "#ffd23a"), (1, "#d88a00"), cx=.4, cy=.3)
        + rg("egg", (0, "#fffbe8"), (.3, "#ffe680"), (.75, "#f4a800"), (1, "#a86200"), cx=.36, cy=.3, r=.75)
        + rg("eggGlow", (0, "#ffe680", .95), (.45, "#ffc634", .4), (1, "#ffc634", 0))
        + lg("paw", (0, "#5a2a14"), (1, "#24100a"))
        + lg("ground", (0, "#1e1050"), (1, "#0a0420"))
        + lg("rimL", (0, "#cfc0ff", 0), (1, "#cfc0ff", .9), x1=0, y1=1, x2=1, y2=0)
    )
    O = 'stroke="#2a0c02" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"'
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(3, 55, (0, 0, 512, 330))}
<circle cx="398" cy="104" r="150" fill="url(#moonGlow)"/>
<circle cx="398" cy="104" r="58" fill="url(#moon)"/>
<g fill="#e8c878" opacity=".45"><circle cx="380" cy="90" r="11"/><circle cx="414" cy="124" r="7"/><circle cx="418" cy="86" r="5"/><circle cx="388" cy="124" r="4"/></g>
<g fill="#160a40">
  <path d="M0 392 L40 380 L40 352 L60 352 L60 380 L110 372 L120 340 L150 318 L180 340 L190 372 L512 360 L512 512 L0 512 Z"/>
  <rect x="136" y="342" width="28" height="30" fill="#ffc86a" opacity=".85"/>
  <path d="M136 357 H164 M150 342 V372" stroke="#160a40" stroke-width="3"/>
</g>
<g stroke="#160a40" stroke-width="6"><path d="M330 372 V340 M370 372 V336 M410 370 V334 M450 368 V332 M490 366 V330"/><path d="M320 348 H512 M320 360 H512" stroke-width="5"/></g>
<rect y="400" width="512" height="112" fill="url(#ground)"/>
<ellipse cx="236" cy="474" rx="170" ry="24" fill="#000" opacity=".5" filter="url(#b14)"/>

<!-- tail -->
<path d="M70 450 Q10 380 46 300 Q70 360 120 380 Q160 420 140 470 Z" fill="url(#fur)" {O}/>
<path d="M46 300 Q30 330 40 356 Q56 334 64 316 Z" fill="url(#cream)" stroke="#2a0c02" stroke-width="5" stroke-linejoin="round"/>

<g filter="url(#sh)">
  <!-- ears -->
  <path d="M96 236 L104 52 Q112 44 122 52 L214 160 Z" fill="url(#fur)" {O}/>
  <path d="M376 236 L368 52 Q360 44 350 52 L258 160 Z" fill="url(#fur)" {O}/>
  <!-- head -->
  <path d="M54 262 Q60 150 236 140 Q412 150 418 262 L452 288 L410 296 L428 330 L380 330 Q350 400 236 438 Q122 400 92 330 L44 330 L62 296 L20 288 Z" fill="url(#fur)" {O}/>
</g>
<path d="M104 60 L110 118 L132 92 Z" fill="#2a0c02"/><path d="M368 60 L362 118 L340 92 Z" fill="#2a0c02"/>
<path d="M118 200 L120 110 Q160 140 186 168 Z" fill="url(#earIn)"/><path d="M354 200 L352 110 Q312 140 286 168 Z" fill="url(#earIn)"/>
<path d="M124 196 Q136 160 128 130 M140 186 Q150 160 146 140" stroke="#ffe8cc" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/>
<path d="M348 196 Q336 160 344 130 M332 186 Q322 160 326 140" stroke="#ffe8cc" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/>
<!-- forehead light & fur strokes -->
<path d="M120 214 Q160 160 236 156 Q312 160 352 214 Q300 186 236 184 Q172 186 120 214 Z" fill="#fff" opacity=".16"/>
<g stroke="#c4440a" stroke-width="4" stroke-linecap="round" opacity=".55" fill="none"><path d="M226 168 l4 22 M242 166 l-2 22 M210 174 l8 18 M258 172 l-6 18"/></g>
<!-- muzzle / cheeks -->
<path d="M84 300 Q140 268 196 286 Q224 300 236 330 Q248 300 276 286 Q332 268 388 300 Q370 352 330 378 L300 372 L310 392 Q270 420 236 432 Q202 420 162 392 L172 372 L142 378 Q102 352 84 300 Z" fill="url(#cream)" stroke="#2a0c02" stroke-width="6" stroke-linejoin="round"/>
<!-- eyes: sly half-lidded -->
<g stroke="#2a0c02" stroke-width="6" stroke-linejoin="round">
  <path d="M120 252 Q150 226 198 244 Q170 272 130 266 Z" fill="url(#iris)"/>
  <path d="M352 252 Q322 226 274 244 Q302 272 342 266 Z" fill="url(#iris)"/>
</g>
<path d="M162 236 Q156 252 162 266 Q168 252 162 236 Z" fill="#1a0600" stroke="#1a0600" stroke-width="5" stroke-linejoin="round"/>
<path d="M310 236 Q304 252 310 266 Q316 252 310 236 Z" fill="#1a0600" stroke="#1a0600" stroke-width="5" stroke-linejoin="round"/>
<circle cx="148" cy="246" r="5" fill="#fff"/><circle cx="296" cy="246" r="5" fill="#fff"/>
<path d="M112 244 Q154 214 208 238" stroke="#2a0c02" stroke-width="13" fill="none" stroke-linecap="round"/>
<path d="M360 244 Q318 214 264 238" stroke="#2a0c02" stroke-width="13" fill="none" stroke-linecap="round"/>
<path d="M118 216 L196 226" stroke="#2a0c02" stroke-width="9" stroke-linecap="round"/><path d="M354 216 L276 226" stroke="#2a0c02" stroke-width="9" stroke-linecap="round"/>
<!-- nose & mouth -->
<path d="M206 322 Q236 306 266 322 Q262 346 236 352 Q210 346 206 322 Z" fill="#1a0600"/>
<ellipse cx="226" cy="320" rx="11" ry="5" fill="#fff" opacity=".7"/>
<path d="M236 352 V368 M190 366 Q214 392 236 368 Q262 394 300 360" stroke="#2a0c02" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M280 372 L288 396 L298 366 Z" fill="#fff" stroke="#2a0c02" stroke-width="4" stroke-linejoin="round"/>
<g stroke="#f2dcc2" stroke-width="3" stroke-linecap="round" opacity=".85"><path d="M150 346 L92 336 M150 358 L96 366 M322 346 L380 336 M322 358 L376 366"/></g>
<!-- moon rim light on right edge -->


<!-- golden egg + paw -->
<circle cx="380" cy="402" r="118" fill="url(#eggGlow)"/>
<g transform="translate(380 404) rotate(14)" filter="url(#sh)">
  <ellipse rx="62" ry="78" fill="url(#egg)" stroke="#7a3e00" stroke-width="6"/>
  <ellipse cx="-22" cy="-34" rx="15" ry="24" fill="#fff" opacity=".9"/>
  <ellipse cx="22" cy="40" rx="24" ry="12" fill="#fff6c0" opacity=".35"/>
  <path d="M-30 6 Q0 14 30 4" stroke="#fff3b0" stroke-width="4" fill="none" opacity=".6"/>
</g>
<g filter="url(#sh2)">
  <path d="M288 470 Q300 420 330 406 Q356 398 360 420 Q368 448 340 476 Z" fill="url(#paw)" {O}/>
  <path d="M322 412 q8 -14 22 -8 M330 430 q10 -10 22 -2" stroke="#8a5a3a" stroke-width="5" fill="none" stroke-linecap="round"/>
</g>
{sparkle(446, 330, .9, "#fff6c0")}{sparkle(316, 330, .55, "#fff6c0")}{sparkle(452, 470, .5, "#fff6c0")}{sparkle(60, 120, .6)}{sparkle(250, 60, .45)}
'''
    return icon(defs, art)
