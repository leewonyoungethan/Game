"""Wander Road — a sports coupe cruising toward a golden-hour sun on an endless road."""
from .common import icon, lg, rg, stars, sparkle

def build():
    defs = (
        lg("sky", (0, "#241a5c"), (.32, "#6a3a9a"), (.56, "#ff6a7a"), (.74, "#ffb15a"), (1, "#ffe3a0"))
        + rg("sun", (0, "#fffdf0"), (.45, "#ffe58a"), (1, "#ff9a4a"), cx=.5, cy=.4)
        + rg("sunGlow", (0, "#ffd890", .85), (.5, "#ff8a6a", .25), (1, "#ff8a6a", 0))
        + lg("m1", (0, "#9a5ab8"), (1, "#5a3488"))
        + lg("m2", (0, "#6a3a8e"), (1, "#3a2066"))
        + lg("m3", (0, "#3e2a6a"), (1, "#1e1440"))
        + lg("land", (0, "#2a1d4e"), (1, "#0e0a22"))
        + lg("road", (0, "#4a4060"), (.4, "#2a2638"), (1, "#121018"))
        + lg("roadShine", (0, "#ffb070", 0), (.5, "#ffb070", .22), (1, "#ffb070", 0), x1=0, y1=0, x2=1, y2=0)
        + lg("body", (0, "#ff7a7a"), (.35, "#e8202e"), (.75, "#a00c18"), (1, "#5a040a"))
        + lg("bodySide", (0, "#c8141e"), (1, "#5a040a"), x1=0, y1=0, x2=1, y2=0)
        + lg("glass", (0, "#2a1e3e"), (.5, "#121022"), (1, "#05040a"))
        + lg("glassRefl", (0, "#ffb870", .75), (1, "#ff6a7a", 0), x1=0, y1=0, x2=1, y2=1)
        + lg("tail", (0, "#ff8a8a"), (.5, "#ff1a2e"), (1, "#a8000e"))
        + rg("tailGlow", (0, "#ff3a4a", .7), (1, "#ff3a4a", 0))
        + lg("tyre", (0, "#2a2830"), (1, "#08070c"))
        + lg("refl", (0, "#ff2a3a", .55), (1, "#ff2a3a", 0))
        + lg("cloud", (0, "#ffd2b0"), (1, "#ff8a9a"))
    )
    O = 'stroke="#1c0206" stroke-width="5" stroke-linejoin="round"'
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(11, 26, (0, 0, 512, 110))}
<g filter="url(#b2)" opacity=".85">
  <path d="M30 150 Q70 128 120 140 Q150 120 190 138 L190 150 Z" fill="url(#cloud)"/>
  <path d="M330 120 Q370 100 410 116 Q440 100 480 118 L480 130 L330 132 Z" fill="url(#cloud)"/>
</g>
<circle cx="256" cy="262" r="190" fill="url(#sunGlow)"/>
<circle cx="256" cy="262" r="100" fill="url(#sun)"/>
<g fill="url(#sky)"><rect x="140" y="262" width="232" height="7"/><rect x="140" y="282" width="232" height="9"/><rect x="140" y="304" width="232" height="11"/></g>
<path d="M0 312 L60 250 L110 280 L170 214 L230 272 L256 258 L300 220 L360 268 L420 226 L512 290 L512 340 L0 340 Z" fill="url(#m1)"/>
<path d="M170 214 L188 236 L176 240 L196 262 L160 246 Z M300 220 L316 240 L304 242 L322 264 L292 248 Z" fill="#fff" opacity=".22"/>
<path d="M0 330 L90 284 L160 316 L240 278 L330 312 L420 280 L512 316 L512 350 L0 350 Z" fill="url(#m2)"/>
<path d="M0 346 L120 322 L200 340 L290 318 L380 342 L512 324 L512 360 L0 360 Z" fill="url(#m3)"/>
<rect y="342" width="512" height="170" fill="url(#land)"/>
<!-- roadside trees -->
<g fill="#0c0820">
  <path d="M28 420 l22 -78 l22 78 Z"/><path d="M70 404 l16 -56 l16 56 Z"/><path d="M104 384 l10 -36 l10 36 Z"/><path d="M134 372 l7 -24 l7 24 Z"/>
  <path d="M484 420 l-22 -78 l-22 78 Z"/><path d="M442 404 l-16 -56 l-16 56 Z"/><path d="M408 384 l-10 -36 l-10 36 Z"/><path d="M378 372 l-7 -24 l-7 24 Z"/>
</g>
<!-- road -->
<path d="M240 342 L272 342 L520 512 L-8 512 Z" fill="url(#road)"/>
<path d="M240 342 L272 342 L520 512 L-8 512 Z" fill="url(#roadShine)"/>
<path d="M240 342 L-8 512" stroke="#ffe0a0" stroke-width="5"/><path d="M272 342 L520 512" stroke="#ffe0a0" stroke-width="5"/>
<g fill="#fff8e0">
  <path d="M254.5 348 L257.5 348 L258 360 L254 360 Z"/><path d="M253 372 L259 372 L260 392 L252 392 Z"/><path d="M251 410 L261 410 L263 442 L249 442 Z"/><path d="M247 466 L265 466 L268 512 L244 512 Z"/>
</g>
<!-- speed lines -->
<g stroke="#ffe8c8" stroke-linecap="round" opacity=".55">
  <path d="M30 396 L120 366" stroke-width="4"/><path d="M8 444 L120 404" stroke-width="6"/><path d="M482 396 L392 366" stroke-width="4"/><path d="M504 444 L392 404" stroke-width="6"/>
</g>
<!-- car (rear view) -->
<g transform="translate(256 470) scale(.84) translate(-256 -486)">
<ellipse cx="256" cy="486" rx="150" ry="20" fill="#000" opacity=".75" filter="url(#b6)"/>
<path d="M150 490 L362 490 L392 512 L120 512 Z" fill="url(#refl)" opacity=".7"/>
<g filter="url(#sh)">
  <rect x="120" y="440" width="58" height="52" rx="14" fill="url(#tyre)"/><rect x="334" y="440" width="58" height="52" rx="14" fill="url(#tyre)"/>
  <path d="M112 470 L112 420 Q112 392 140 380 L176 322 Q186 306 210 304 L302 304 Q326 306 336 322 L372 380 Q400 392 400 420 L400 470 Q400 482 386 482 L126 482 Q112 482 112 470 Z" fill="url(#body)" {O}/>
  <path d="M172 378 L198 330 Q204 320 216 320 L296 320 Q308 320 314 330 L340 378 Z" fill="url(#glass)" {O}/>
  <path d="M206 334 L238 334 L214 372 L190 372 Z" fill="url(#glassRefl)"/>
  <path d="M128 400 Q256 382 384 400" fill="none" stroke="#ffb0b0" stroke-width="4" opacity=".55"/>
  <path d="M150 380 Q256 368 362 380" fill="none" stroke="#ff9a9a" stroke-width="3" opacity=".4"/>
  <path d="M188 304 L196 290 L316 290 L324 304 Z" fill="#14060a" {O}/>
  <rect x="126" y="404" width="260" height="22" rx="10" fill="#2a0408"/>
  <rect x="130" y="408" width="252" height="14" rx="7" fill="url(#tail)"/>
  <rect x="132" y="409" width="248" height="4" rx="2" fill="#ffd0d0" opacity=".8"/>
  <rect x="208" y="436" width="96" height="26" rx="6" fill="#f2f2f6" {O}/>
  <text x="256" y="455" text-anchor="middle" font-family="Arial, sans-serif" font-weight="900" font-size="15" fill="#1c0206">WANDER</text>
  <path d="M120 470 L392 470 L384 482 L128 482 Z" fill="#14060a"/>
  <g fill="#3a3640" stroke="#0a0a0e" stroke-width="3"><ellipse cx="166" cy="476" rx="14" ry="7"/><ellipse cx="346" cy="476" rx="14" ry="7"/></g>
</g>
<circle cx="150" cy="416" r="58" fill="url(#tailGlow)"/><circle cx="362" cy="416" r="58" fill="url(#tailGlow)"/>
</g>
{sparkle(96, 214, .55)}{sparkle(430, 190, .5)}
'''
    return icon(defs, art)
