"""Generate the game app icons in icons/ (512x512 SVG).

Run: python3 tools/make_icons.py
"""
import math, pathlib, random, re, xml.dom.minidom

OUT = pathlib.Path(__file__).resolve().parent.parent / "icons"

def lg(id, *stops, x2=0, y2=1, x1=0, y1=0):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"{f" stop-opacity=\"{a}\"" if a is not None else ""}/>' for o, c, *rest in stops for a in [rest[0] if rest else None])
    return f'<linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'

def rg(id, *stops, cx=.5, cy=.5, r=.5, fx=None, fy=None):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"{f" stop-opacity=\"{a}\"" if a is not None else ""}/>' for o, c, *rest in stops for a in [rest[0] if rest else None])
    f = f' fx="{fx}" fy="{fy}"' if fx is not None else ""
    return f'<radialGradient id="{id}" cx="{cx}" cy="{cy}" r="{r}"{f}>{s}</radialGradient>'

COMMON = """
  <clipPath id="sq"><rect width="512" height="512" rx="114"/></clipPath>
  <filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="12" stdDeviation="10" flood-color="#000" flood-opacity=".45"/></filter>
  <filter id="sh2" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="5" stdDeviation="4" flood-color="#000" flood-opacity=".35"/></filter>
  <filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="blur4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .07 0"/></filter>
  <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".42"/><stop offset=".6" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <radialGradient id="vig" cx=".5" cy=".45" r=".72"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></radialGradient>
  <linearGradient id="rim" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".75"/><stop offset=".5" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#fff" stop-opacity=".3"/></linearGradient>
  <radialGradient id="spark"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#fff" stop-opacity=".8"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
"""

def sparkle(x, y, s=1.0, color="#fff"):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle r="22" fill="url(#spark)" opacity=".7"/>'
            f'<path d="M0 -26 Q3 -3 26 0 Q3 3 0 26 Q-3 3 -26 0 Q-3 -3 0 -26 Z" fill="{color}"/></g>')

def rays(color, op, n=18, cx=256, cy=256):
    d = []
    for i in range(n):
        a = 2 * math.pi * i / n; b = a + math.pi / n
        d.append(f"M{cx} {cy} L{cx+700*math.cos(a):.0f} {cy+700*math.sin(a):.0f} L{cx+700*math.cos(b):.0f} {cy+700*math.sin(b):.0f} Z")
    return f'<path d="{" ".join(d)}" fill="{color}" opacity="{op}"/>'

def bokeh(seed, color, n=10, rmin=6, rmax=26, op=(.08, .3), area=(0, 0, 512, 512)):
    rnd = random.Random(seed); out = []
    for _ in range(n):
        x = rnd.uniform(area[0], area[2]); y = rnd.uniform(area[1], area[3])
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(rmin, rmax):.0f}" fill="{color}" opacity="{rnd.uniform(*op):.2f}"/>')
    return "".join(out)

def stars(seed, n=30, area=(0, 0, 512, 260)):
    rnd = random.Random(seed)
    return "".join(f'<circle cx="{rnd.uniform(area[0],area[2]):.0f}" cy="{rnd.uniform(area[1],area[3]):.0f}" r="{rnd.uniform(.8,2.6):.1f}" fill="#fff" opacity="{rnd.uniform(.4,1):.2f}"/>' for _ in range(n))

def icon(defs, art):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
<defs>{COMMON}{defs}</defs>
<g clip-path="url(#sq)">
{art}
<rect width="512" height="512" filter="url(#grain)"/>
<rect width="512" height="512" fill="url(#vig)"/>
<path d="M0 0 H512 V190 Q256 250 0 190 Z" fill="url(#gloss)"/>
</g>
<rect x="4" y="4" width="504" height="504" rx="110" fill="none" stroke="url(#rim)" stroke-width="8"/>
</svg>
'''

ICONS = {}

# ---------------------------------------------------------------- 곡괭이 봉우리
ICONS["rock"] = icon(
    rg("bg", (0, "#bff0ff"), (.45, "#4aa8ff"), (1, "#1636a0"), cy=.3, r=.8)
    + lg("grass", (0, "#b8ff7a"), (1, "#3fae2e"))
    + lg("dirtL", (0, "#a8743f"), (1, "#6b4220")) + lg("dirtR", (0, "#8a5a2e"), (1, "#4e2e14"))
    + lg("stoneL", (0, "#a5a9b6"), (1, "#6b7080")) + lg("stoneR", (0, "#7d8292"), (1, "#454a58"))
    + lg("wood", (0, "#e0a060"), (.5, "#b06a2c"), (1, "#7a4218"), x2=1, y2=0)
    + lg("metal", (0, "#ffffff"), (.35, "#d4dce8"), (.7, "#8a96ac"), (1, "#5a6478"))
    + rg("dia", (0, "#ffffff"), (.4, "#8ff8ff"), (1, "#14a8d8"))
    + rg("gold", (0, "#fffbd0"), (.4, "#ffd84a"), (1, "#d08a00"))
    + rg("ruby", (0, "#ffe0e8"), (.4, "#ff5a7a"), (1, "#a8103a")),
    f'''<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .13, 20, 256, 210)}
<g opacity=".9" filter="url(#blur4)"><ellipse cx="90" cy="110" rx="70" ry="24" fill="#fff"/><ellipse cx="130" cy="96" rx="40" ry="22" fill="#fff"/><ellipse cx="430" cy="70" rx="56" ry="18" fill="#fff"/></g>
<ellipse cx="256" cy="452" rx="150" ry="28" fill="#0a1a50" opacity=".55" filter="url(#blur)"/>
<g filter="url(#sh)" stroke="#1a2040" stroke-width="5" stroke-linejoin="round">
  <path d="M256 150 L392 218 L256 286 L120 218 Z" fill="url(#grass)"/>
  <path d="M120 218 L256 286 L256 318 L120 250 Z" fill="url(#dirtL)"/>
  <path d="M392 218 L256 286 L256 318 L392 250 Z" fill="url(#dirtR)"/>
  <path d="M120 250 L256 318 L256 440 L120 372 Z" fill="url(#stoneL)"/>
  <path d="M392 250 L256 318 L256 440 L392 372 Z" fill="url(#stoneR)"/>
</g>
<path d="M256 162 L372 220 L256 278 L140 220 Z" fill="#fff" opacity=".18"/>
<g stroke="#2a8a1e" stroke-width="4" stroke-linecap="round" opacity=".6"><path d="M180 222 l8 -10"/><path d="M230 250 l6 -10"/><path d="M300 200 l8 -10"/><path d="M330 236 l6 -10"/></g>
<path d="M120 250 L140 262 L150 254 L170 272 L186 264 L204 282 L226 276 L256 300 L256 286 L120 218 Z" fill="url(#grass)" stroke="#1a2040" stroke-width="4" stroke-linejoin="round"/>
<path d="M392 250 L372 262 L360 254 L340 272 L324 266 L304 282 L284 278 L256 300 L256 286 L392 218 Z" fill="#3fae2e" stroke="#1a2040" stroke-width="4" stroke-linejoin="round"/>
<g stroke="#1a2040" stroke-width="4" stroke-linejoin="round">
  <path d="M160 320 l22 -12 l14 22 l-22 12 Z" fill="url(#dia)" filter="url(#glow)"/>
  <path d="M310 340 l26 -12 l12 24 l-26 12 Z" fill="url(#gold)" filter="url(#glow)"/>
  <path d="M200 380 l18 -9 l10 18 l-18 9 Z" fill="url(#ruby)" filter="url(#glow)"/>
  <path d="M350 290 l14 -7 l8 14 l-14 7 Z" fill="url(#dia)"/>
</g>
<g transform="translate(392 176) rotate(40) scale(.82)" filter="url(#sh)">
  <rect x="-15" y="-10" width="30" height="250" rx="13" fill="url(#wood)" stroke="#3a1e08" stroke-width="5"/>
  <path d="M-8 30 q4 40 0 80 M6 120 q-4 40 0 80" stroke="#6a3a14" stroke-width="3" fill="none" opacity=".6"/>
  <rect x="-19" y="-6" width="38" height="26" rx="6" fill="#5a6478" stroke="#1a2040" stroke-width="5"/>
  <path d="M-160 22 Q-80 -80 0 -76 Q80 -80 160 22 L146 40 Q80 -36 0 -34 Q-80 -36 -146 40 Z" fill="url(#metal)" stroke="#1a2040" stroke-width="6" stroke-linejoin="round"/>
  <path d="M-130 8 Q-70 -60 0 -62 Q70 -60 130 8" fill="none" stroke="#fff" stroke-width="5" opacity=".85" stroke-linecap="round"/>
</g>
<g fill="#8a8f9e" stroke="#1a2040" stroke-width="3"><path d="M418 268 l14 -6 l6 12 l-14 6 Z"/><path d="M440 236 l9 -4 l4 9 l-9 4 Z"/><path d="M400 300 l8 -4 l4 8 l-8 4 Z"/></g>
{sparkle(176, 316, .8)}{sparkle(340, 330, .9, "#fff6c0")}{sparkle(100, 200, .7)}{sparkle(436, 170, 1.0)}
''')

# ---------------------------------------------------------------- 여우의 달걀 도둑
ICONS["eggsteal"] = icon(
    rg("bg", (0, "#6a4cd8"), (.55, "#2a1870"), (1, "#0c0628"), cy=.35, r=.85)
    + rg("moon", (0, "#fffbe8"), (.7, "#ffeeb0"), (1, "#f0c860"))
    + rg("moonglow", (0, "#ffe9a0", .55), (1, "#ffe9a0", 0))
    + lg("fur", (0, "#ffb85a"), (.5, "#ff7a1a"), (1, "#c8400a"))
    + lg("furDark", (0, "#e0601a"), (1, "#9a2e06"))
    + lg("muzzle", (0, "#ffffff"), (1, "#f3dcc4"))
    + rg("eye", (0, "#fffbb0"), (.6, "#ffd23a"), (1, "#e08a00"))
    + rg("egg", (0, "#fffbe0"), (.35, "#ffe066"), (.8, "#f0a800"), (1, "#b86e00"), cx=.4, cy=.35, r=.7)
    + rg("eggglow", (0, "#ffe680", .95), (.5, "#ffc634", .45), (1, "#ffc634", 0))
    + lg("earIn", (0, "#3a1408"), (1, "#7a2e14")),
    f'''<rect width="512" height="512" fill="url(#bg)"/>
{stars(3, 40)}
<circle cx="404" cy="100" r="110" fill="url(#moonglow)"/>
<circle cx="404" cy="100" r="50" fill="url(#moon)"/>
<g fill="#e8c870" opacity=".5"><circle cx="390" cy="88" r="9"/><circle cx="418" cy="116" r="6"/><circle cx="420" cy="84" r="4"/></g>
<path d="M0 420 Q130 380 256 410 T512 400 L512 512 L0 512 Z" fill="#120a30"/>
<ellipse cx="240" cy="470" rx="170" ry="26" fill="#000" opacity=".5" filter="url(#blur)"/>
<g filter="url(#sh)" stroke="#2a0e04" stroke-width="6" stroke-linejoin="round">
  <path d="M100 236 L118 70 L210 166 Z" fill="url(#fur)"/><path d="M380 236 L362 70 L270 166 Z" fill="url(#fur)"/>
  <path d="M60 250 Q60 130 240 128 Q420 130 420 250 Q420 340 340 392 L240 440 L140 392 Q60 340 60 250 Z" fill="url(#fur)"/>
</g>
<path d="M126 200 L132 104 L190 168 Z" fill="url(#earIn)"/><path d="M354 200 L348 104 L290 168 Z" fill="url(#earIn)"/>
<path d="M90 230 Q120 150 240 146 Q360 150 390 230 Q340 180 240 178 Q140 180 90 230 Z" fill="#fff" opacity=".18"/>
<path d="M60 268 L30 300 L78 300 L54 330 L104 322 Z" fill="url(#furDark)" stroke="#2a0e04" stroke-width="5" stroke-linejoin="round"/>
<path d="M420 268 L450 300 L402 300 L426 330 L376 322 Z" fill="url(#furDark)" stroke="#2a0e04" stroke-width="5" stroke-linejoin="round"/>
<path d="M110 300 Q170 270 240 318 Q310 270 370 300 Q340 390 240 440 Q140 390 110 300 Z" fill="url(#muzzle)" stroke="#2a0e04" stroke-width="6" stroke-linejoin="round"/>
<g stroke="#2a0e04" stroke-width="6" stroke-linejoin="round">
  <path d="M120 250 Q150 212 204 240 Q160 270 120 250 Z" fill="url(#eye)"/>
  <path d="M360 250 Q330 212 276 240 Q320 270 360 250 Z" fill="url(#eye)"/>
</g>
<path d="M164 232 q-4 12 0 26 q4 -14 0 -26 Z" fill="#1a0800" stroke="#1a0800" stroke-width="6" stroke-linejoin="round"/>
<path d="M316 232 q-4 12 0 26 q4 -14 0 -26 Z" fill="#1a0800" stroke="#1a0800" stroke-width="6" stroke-linejoin="round"/>
<circle cx="150" cy="238" r="5" fill="#fff"/><circle cx="302" cy="238" r="5" fill="#fff"/>
<path d="M104 222 L210 232" stroke="#2a0e04" stroke-width="12" stroke-linecap="round"/>
<path d="M376 222 L270 232" stroke="#2a0e04" stroke-width="12" stroke-linecap="round"/>
<ellipse cx="240" cy="330" rx="30" ry="20" fill="#1a0800"/><ellipse cx="232" cy="322" rx="10" ry="5" fill="#fff" opacity=".6"/>
<path d="M196 372 Q240 400 290 364" fill="none" stroke="#2a0e04" stroke-width="7" stroke-linecap="round"/>
<path d="M276 372 l8 16 l8 -18" fill="#fff" stroke="#2a0e04" stroke-width="4" stroke-linejoin="round"/>
<circle cx="372" cy="388" r="100" fill="url(#eggglow)"/>
<g transform="translate(372 388) rotate(16)" filter="url(#sh)">
  <ellipse rx="56" ry="70" fill="url(#egg)" stroke="#7a4400" stroke-width="5"/>
  <ellipse cx="-20" cy="-30" rx="14" ry="22" fill="#fff" opacity=".85"/>
  <ellipse cx="22" cy="34" rx="20" ry="10" fill="#fff6c0" opacity=".35"/>
</g>
{sparkle(430, 320, .9, "#fff6c0")}{sparkle(318, 452, .6, "#fff6c0")}{sparkle(70, 120, .6)}
''')

# ---------------------------------------------------------------- Wander Road
ICONS["road"] = icon(
    lg("sky", (0, "#1d1450"), (.35, "#6a2a8a"), (.6, "#ff5a6a"), (.78, "#ffb04a"), (1, "#ffe08a"))
    + rg("sun", (0, "#fffbe0"), (.5, "#ffd86a"), (1, "#ff8a3a"))
    + rg("sunglow", (0, "#ffd080", .8), (1, "#ff7a50", 0))
    + lg("m1", (0, "#8a4aa8"), (1, "#4a2a70")) + lg("m2", (0, "#5a2a7a"), (1, "#2a1450"))
    + lg("ground", (0, "#3a2a5a"), (1, "#120a24"))
    + lg("road", (0, "#3a3450"), (1, "#16141f"))
    + lg("car", (0, "#ff6a6a"), (.45, "#e8202e"), (1, "#8a0a14"))
    + lg("glass", (0, "#bfe6ff"), (.5, "#4a7aa8"), (1, "#1a2a4a"))
    + rg("tail", (0, "#ffe0e0"), (.4, "#ff2a3a"), (1, "#ff2a3a", 0)),
    f'''<rect width="512" height="512" fill="url(#sky)"/>
{stars(11, 25, (0, 0, 512, 120))}
<circle cx="256" cy="250" r="170" fill="url(#sunglow)"/>
<circle cx="256" cy="250" r="96" fill="url(#sun)"/>
<g fill="url(#sky)"><rect x="150" y="250" width="212" height="8"/><rect x="150" y="270" width="212" height="10"/><rect x="150" y="294" width="212" height="12"/></g>
<path d="M0 300 L70 236 L140 280 L210 214 L256 250 L310 206 L380 270 L450 226 L512 268 L512 330 L0 330 Z" fill="url(#m1)"/>
<path d="M0 320 L100 270 L190 310 L280 262 L370 306 L460 276 L512 300 L512 340 L0 340 Z" fill="url(#m2)"/>
<rect y="318" width="512" height="194" fill="url(#ground)"/>
<path d="M232 318 L280 318 L512 512 L0 512 Z" fill="url(#road)"/>
<path d="M232 318 L0 512" stroke="#ffcf60" stroke-width="6"/><path d="M280 318 L512 512" stroke="#ffcf60" stroke-width="6"/>
<g fill="#fff">
  <path d="M254 326 L258 326 L259 340 L253 340 Z"/><path d="M252 352 L260 352 L262 376 L250 376 Z"/><path d="M249 396 L263 396 L266 436 L246 436 Z"/><path d="M244 466 L268 466 L272 512 L240 512 Z"/>
</g>
<g stroke="#fff" stroke-linecap="round" opacity=".55"><path d="M40 380 L110 350" stroke-width="5"/><path d="M20 430 L120 390" stroke-width="7"/><path d="M472 380 L402 350" stroke-width="5"/><path d="M492 430 L392 390" stroke-width="7"/></g>
<ellipse cx="256" cy="476" rx="128" ry="18" fill="#000" opacity=".7" filter="url(#blur4)"/>
<g filter="url(#sh)">
  <path d="M140 470 L140 410 Q140 386 162 376 L190 330 Q200 314 222 314 L290 314 Q312 314 322 330 L350 376 Q372 386 372 410 L372 470 Z" fill="url(#car)" stroke="#2a0408" stroke-width="6" stroke-linejoin="round"/>
  <path d="M196 372 L214 334 Q218 326 228 326 L284 326 Q294 326 298 334 L316 372 Z" fill="url(#glass)" stroke="#2a0408" stroke-width="5" stroke-linejoin="round"/>
  <path d="M220 334 L240 334 L222 368 L204 368 Z" fill="#fff" opacity=".35"/>
  <path d="M150 398 Q256 384 362 398" fill="none" stroke="#fff" stroke-width="4" opacity=".45"/>
  <rect x="152" y="404" width="62" height="22" rx="8" fill="#ff2a3a" stroke="#2a0408" stroke-width="4"/>
  <rect x="298" y="404" width="62" height="22" rx="8" fill="#ff2a3a" stroke="#2a0408" stroke-width="4"/>
  <rect x="216" y="434" width="80" height="22" rx="4" fill="#f2f2f2" stroke="#2a0408" stroke-width="4"/>
  <rect x="140" y="456" width="44" height="30" rx="6" fill="#16141f"/><rect x="328" y="456" width="44" height="30" rx="6" fill="#16141f"/>
</g>
<circle cx="183" cy="415" r="44" fill="url(#tail)"/><circle cx="329" cy="415" r="44" fill="url(#tail)"/>
{sparkle(120, 170, .6)}{sparkle(420, 150, .5)}
''')

# ---------------------------------------------------------------- Rail Dash
ICONS["rail-dash"] = icon(
    lg("sky", (0, "#1a1040"), (.45, "#8a2a7a"), (.75, "#ff6a6a"), (1, "#ffb060"))
    + lg("bed", (0, "#4a3050"), (1, "#1a1020"))
    + lg("train", (0, "#7ac4ff"), (.5, "#2a7ae8"), (1, "#123a8a"))
    + rg("lamp", (0, "#fffbe0"), (.3, "#fff0a0", .9), (1, "#fff0a0", 0))
    + lg("hood", (0, "#7affe6"), (1, "#18b89a")) + lg("pack", (0, "#ffb070"), (1, "#e0601a"))
    + lg("pants", (0, "#4a5a9a"), (1, "#1e2a5a"))
    + rg("coin", (0, "#fffbd0"), (.5, "#ffd23a"), (1, "#c88400"), cx=.4, cy=.35)
    + lg("trail", (0, "#7affe6", 0), (1, "#7affe6", .7), x2=1, y2=0),
    f'''<rect width="512" height="512" fill="url(#sky)"/>
{stars(5, 18, (0, 0, 512, 110))}
<g fill="#2a1240" opacity=".9"><rect x="0" y="150" width="40" height="90"/><rect x="44" y="120" width="34" height="120"/><rect x="82" y="168" width="50" height="72"/><rect x="380" y="130" width="40" height="110"/><rect x="424" y="160" width="50" height="80"/><rect x="478" y="110" width="34" height="130"/></g>
<g fill="#ffcc66" opacity=".6"><rect x="54" y="134" width="5" height="5"/><rect x="64" y="150" width="5" height="5"/><rect x="390" y="144" width="5" height="5"/><rect x="400" y="170" width="5" height="5"/><rect x="488" y="124" width="5" height="5"/></g>
<rect y="236" width="512" height="276" fill="#241430"/>
<path d="M226 236 L286 236 L470 512 L42 512 Z" fill="url(#bed)"/>
<g stroke="#7a5a4a" stroke-linecap="butt"><path d="M60 494 L452 494" stroke-width="18"/><path d="M118 410 L394 410" stroke-width="12"/><path d="M164 346 L348 346" stroke-width="9"/><path d="M196 300 L316 300" stroke-width="7"/><path d="M216 268 L296 268" stroke-width="5"/></g>
<g stroke="#e8e0f8" stroke-width="7"><path d="M238 236 L120 512"/><path d="M274 236 L392 512"/></g>
<g filter="url(#sh)">
  <path d="M176 140 Q176 104 212 104 L300 104 Q336 104 336 140 L336 300 L176 300 Z" fill="url(#train)" stroke="#0a1a40" stroke-width="6"/>
  <rect x="196" y="126" width="120" height="64" rx="12" fill="#0e1830" stroke="#0a1a40" stroke-width="5"/>
  <path d="M206 132 L236 132 L214 184 L200 184 Z" fill="#fff" opacity=".25"/>
  <rect x="176" y="226" width="160" height="10" fill="#fff" opacity=".9"/>
</g>
<circle cx="206" cy="264" r="44" fill="url(#lamp)"/><circle cx="306" cy="264" r="44" fill="url(#lamp)"/>
<circle cx="206" cy="264" r="12" fill="#fffbe0"/><circle cx="306" cy="264" r="12" fill="#fffbe0"/>
<g transform="translate(256 432)" filter="url(#sh2)">
  <rect x="-120" y="-18" width="240" height="40" rx="6" fill="#ffd23a" stroke="#2a1404" stroke-width="5"/>
  <path d="M-96 -18 L-66 22 M-36 -18 L-6 22 M24 -18 L54 22 M84 -18 L110 16" stroke="#2a1404" stroke-width="16"/>
  <rect x="-108" y="22" width="12" height="40" fill="#2a1404"/><rect x="96" y="22" width="12" height="40" fill="#2a1404"/>
</g>
<path d="M120 380 Q190 330 250 330" stroke="url(#trail)" stroke-width="40" fill="none" stroke-linecap="round" opacity=".5"/>
<g transform="translate(268 330) rotate(-12)" filter="url(#sh)" stroke="#120a20" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
  <path d="M-20 26 Q-60 40 -84 76" stroke="url(#pants)" stroke-width="28" fill="none"/>
  <path d="M18 24 Q60 30 70 70" stroke="url(#pants)" stroke-width="28" fill="none"/>
  <ellipse cx="-88" cy="84" rx="20" ry="12" fill="#fff"/><ellipse cx="76" cy="78" rx="20" ry="12" fill="#fff"/>
  <path d="M-30 -36 Q-70 -60 -96 -96" stroke="url(#hood)" stroke-width="24" fill="none"/>
  <path d="M30 -30 Q70 -20 96 -50" stroke="url(#hood)" stroke-width="24" fill="none"/>
  <rect x="-46" y="-74" width="92" height="110" rx="34" fill="url(#hood)"/>
  <rect x="-30" y="-58" width="60" height="66" rx="16" fill="url(#pack)"/>
  <circle cx="0" cy="-108" r="38" fill="#3a2416"/>
  <path d="M-40 -112 A40 40 0 0 1 40 -112 L60 -104 L-40 -104 Z" fill="#ff4f8a"/>
</g>
<g filter="url(#sh2)"><circle cx="92" cy="250" r="28" fill="url(#coin)" stroke="#7a4a00" stroke-width="5"/><circle cx="430" cy="300" r="24" fill="url(#coin)" stroke="#7a4a00" stroke-width="5"/><circle cx="410" cy="216" r="18" fill="url(#coin)" stroke="#7a4a00" stroke-width="4"/></g>
<g fill="#fff" opacity=".8"><rect x="86" y="236" width="6" height="18" rx="3"/><rect x="424" y="288" width="5" height="16" rx="2.5"/></g>
{sparkle(118, 222, .5)}{sparkle(452, 274, .5)}
''')

# ---------------------------------------------------------------- 도둑차 대탈주
ICONS["getaway"] = icon(
    lg("asph", (0, "#1e2234"), (1, "#0a0c16"))
    + rg("red", (0, "#ff2a44", .95), (.5, "#ff2a44", .35), (1, "#ff2a44", 0))
    + rg("blue", (0, "#2a7aff", .95), (.5, "#2a7aff", .35), (1, "#2a7aff", 0))
    + lg("body", (0, "#fff07a"), (.4, "#ffc61a"), (1, "#c87a00"), x2=1, y2=0)
    + lg("roof", (0, "#ffe25a"), (1, "#e09a00"), x2=1, y2=0)
    + lg("glass", (0, "#9ad0ff"), (.5, "#24406e"), (1, "#0a1428"))
    + lg("beamv", (0, "#fff8d0", .55), (1, "#fff8d0", 0), y1=1, y2=0)
    + lg("flame", (0, "#ffffff"), (.3, "#8ae8ff"), (1, "#2a6aff", 0))
    + lg("bill", (0, "#9af0a0"), (1, "#2e9a4a")),
    f'''<rect width="512" height="512" fill="url(#asph)"/>
<g fill="#2a3050"><rect x="-10" y="-10" width="170" height="150" rx="10"/><rect x="360" y="-10" width="170" height="150" rx="10"/><rect x="-10" y="380" width="150" height="150" rx="10"/><rect x="372" y="380" width="150" height="150" rx="10"/></g>
<g fill="#ffd58c" opacity=".55"><rect x="20" y="20" width="10" height="10"/><rect x="60" y="60" width="10" height="10"/><rect x="110" y="30" width="10" height="10"/><rect x="400" y="40" width="10" height="10"/><rect x="450" y="90" width="10" height="10"/><rect x="40" y="420" width="10" height="10"/><rect x="420" y="440" width="10" height="10"/></g>
<rect x="160" y="0" width="4" height="512" fill="#ff4fd8" opacity=".7"/><rect x="348" y="0" width="4" height="512" fill="#3ff0ff" opacity=".7"/>
<g stroke="#fff" stroke-width="8" stroke-dasharray="36 28" opacity=".35"><path d="M256 0 V512"/><path d="M0 256 H512"/></g>
<g stroke="#000" stroke-width="16" fill="none" opacity=".55" stroke-linecap="round"><path d="M60 470 Q140 380 200 330"/><path d="M110 500 Q180 410 236 360"/></g>
<circle cx="40" cy="60" r="260" fill="url(#red)"/><circle cx="472" cy="60" r="260" fill="url(#blue)"/><circle cx="40" cy="470" r="170" fill="url(#blue)" opacity=".6"/><circle cx="472" cy="470" r="170" fill="url(#red)" opacity=".6"/>
<g transform="translate(250 270) rotate(45)"><path d="M-62 -186 L-150 -520 L40 -520 L-30 -186 Z" fill="url(#beamv)"/><path d="M30 -186 L-40 -520 L150 -520 L62 -186 Z" fill="url(#beamv)"/></g>
<g stroke="#fff" stroke-linecap="round" opacity=".35"><path d="M60 330 L150 240" stroke-width="6"/><path d="M110 430 L190 350" stroke-width="8"/><path d="M200 470 L260 410" stroke-width="5"/></g>
<g transform="translate(250 270) rotate(45)">
  <ellipse cx="6" cy="14" rx="92" ry="178" fill="#000" opacity=".6" filter="url(#blur4)"/>
  <path d="M-30 168 L0 260 L30 168 Z" fill="url(#flame)"/>
  <g filter="url(#sh)" stroke="#3a2400" stroke-width="6" stroke-linejoin="round">
    <path d="M-80 -150 Q-84 -186 -40 -192 L40 -192 Q84 -186 80 -150 L90 140 Q92 176 50 180 L-50 180 Q-92 176 -90 140 Z" fill="url(#body)"/>
    <path d="M-58 -96 Q0 -116 58 -96 L54 -40 L-54 -40 Z" fill="url(#glass)"/>
    <path d="M-54 -40 L54 -40 L56 70 L-56 70 Z" fill="url(#roof)"/>
    <path d="M-56 70 L56 70 L50 116 Q0 126 -50 116 Z" fill="url(#glass)"/>
  </g>
  <path d="M-40 -100 L-14 -104 L-30 -50 L-50 -50 Z" fill="#fff" opacity=".4"/>
  <rect x="-10" y="-190" width="20" height="370" fill="#2a1a00" opacity=".22"/>
  <rect x="-68" y="-186" width="30" height="16" rx="6" fill="#fffbe0"/><rect x="38" y="-186" width="30" height="16" rx="6" fill="#fffbe0"/>
  <rect x="-70" y="166" width="30" height="12" rx="4" fill="#ff2a3a"/><rect x="40" y="166" width="30" height="12" rx="4" fill="#ff2a3a"/>
  <path d="M-80 -150 Q-70 0 -84 140" fill="none" stroke="#fff" stroke-width="5" opacity=".6"/>
</g>
<g filter="url(#sh2)" stroke="#0a3a14" stroke-width="3">
  <g transform="translate(410 300) rotate(-24)"><rect x="-34" y="-18" width="68" height="36" rx="4" fill="url(#bill)"/><circle r="10" fill="none" stroke="#0a5a24"/></g>
  <g transform="translate(450 380) rotate(18)"><rect x="-30" y="-16" width="60" height="32" rx="4" fill="url(#bill)"/><circle r="9" fill="none" stroke="#0a5a24"/></g>
  <g transform="translate(380 440) rotate(-8)"><rect x="-26" y="-14" width="52" height="28" rx="4" fill="url(#bill)"/><circle r="8" fill="none" stroke="#0a5a24"/></g>
</g>
<g filter="url(#sh2)" stroke="#0a0c16" stroke-width="5" stroke-linejoin="round">
  <g transform="translate(70 76)"><path d="M-30 18 L-24 -14 Q0 -32 24 -14 L30 18 Z" fill="#ff2a44"/><rect x="-38" y="16" width="76" height="16" rx="5" fill="#d0d6e6"/></g>
  <g transform="translate(442 76)"><path d="M-30 18 L-24 -14 Q0 -32 24 -14 L30 18 Z" fill="#2a7aff"/><rect x="-38" y="16" width="76" height="16" rx="5" fill="#d0d6e6"/></g>
</g>
<g filter="url(#glow)" opacity=".9"><ellipse cx="70" cy="70" rx="16" ry="12" fill="#ffb0bc"/><ellipse cx="442" cy="70" rx="16" ry="12" fill="#b0ccff"/></g>
{sparkle(64, 70, .9, "#ffe0e6")}{sparkle(448, 70, .9, "#e0ecff")}
''')

# ---------------------------------------------------------------- 건반 소나기
ICONS["piano-tiles"] = icon(
    rg("bg", (0, "#ff5ac8"), (.5, "#8a2aff"), (1, "#2a0a7a"), cx=.3, cy=.2, r=1)
    + lg("board", (0, "#ffffff"), (1, "#dcd6f4"))
    + lg("tile", (0, "#4a4e62"), (.15, "#22242e"), (1, "#05060a"))
    + lg("hit", (0, "#c0f4ff"), (.5, "#3ab8ff"), (1, "#2a5aff"))
    + rg("ring", (0, "#7af0ff", 0), (.7, "#7af0ff", 0), (.85, "#bff8ff", .9), (1, "#7af0ff", 0))
    + lg("note", (0, "#fff4a0"), (.5, "#ffc234"), (1, "#e07a00")),
    f'''<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .08, 22, 140, 100)}
{bokeh(21, "#ffffff", 14, 8, 34)}
<g transform="translate(256 270) rotate(-14) translate(-256 -270)" filter="url(#sh)">
  <rect x="104" y="40" width="304" height="460" rx="30" fill="url(#board)" stroke="#2a1458" stroke-width="7"/>
  <g stroke="#cfc8ea" stroke-width="5"><path d="M180 48 V492"/><path d="M256 48 V492"/><path d="M332 48 V492"/></g>
  <rect x="108" y="64" width="70" height="150" rx="12" fill="url(#tile)"/>
  <rect x="258" y="20" width="72" height="140" rx="12" fill="url(#tile)"/>
  <rect x="334" y="196" width="70" height="152" rx="12" fill="url(#tile)"/>
  <g fill="#fff" opacity=".22"><rect x="114" y="70" width="12" height="130" rx="6"/><rect x="264" y="26" width="12" height="120" rx="6"/><rect x="340" y="202" width="12" height="130" rx="6"/></g>
  <rect x="182" y="300" width="72" height="156" rx="12" fill="url(#hit)" filter="url(#glow)"/>
</g>
<circle cx="230" cy="380" r="110" fill="url(#ring)"/>
<circle cx="230" cy="380" r="64" fill="none" stroke="#e8fcff" stroke-width="10" filter="url(#glow)"/>
<g fill="#bff8ff">{"".join(f'<circle cx="{230+92*math.cos(a):.0f}" cy="{380+92*math.sin(a):.0f}" r="{5+3*(i%2)}"/>' for i, a in enumerate([k*math.pi/5 for k in range(10)]))}</g>
<g transform="translate(372 300) rotate(12)" filter="url(#sh)" stroke="#6a3400" stroke-width="6" stroke-linejoin="round">
  <ellipse cx="-4" cy="110" rx="46" ry="34" fill="url(#note)" transform="rotate(-22 -4 110)"/>
  <ellipse cx="96" cy="84" rx="46" ry="34" fill="url(#note)" transform="rotate(-22 96 84)"/>
  <path d="M32 100 V-40 L132 -66 V74 L120 74 V-30 L44 -10 V100 Z" fill="url(#note)"/>
</g>
<g fill="#fff" opacity=".7"><ellipse cx="-14" cy="0" rx="10" ry="6" transform="translate(372 300) rotate(-10) translate(-6 100)"/></g>
{sparkle(446, 150, .9, "#fff6c0")}{sparkle(84, 300, .7)}{sparkle(130, 460, .6, "#bff8ff")}
''')

# ---------------------------------------------------------------- 나율이 키우기
ICONS["nayul"] = icon(
    rg("bg", (0, "#fff8d0"), (.5, "#ffc4d8"), (1, "#ff7aa8"), cy=.4, r=.8)
    + rg("skin", (0, "#fff0e0"), (.7, "#ffd8b8"), (1, "#f0b48a"), cx=.45, cy=.4, r=.6)
    + lg("hair", (0, "#9a5a30"), (1, "#4a2410"))
    + rg("eye", (0, "#6a4a3a"), (.6, "#2a1a10"), (1, "#100804"), cx=.5, cy=.6)
    + rg("blush", (0, "#ff7a9a", .8), (1, "#ff7a9a", 0))
    + rg("heart", (0, "#ffb0c8"), (.5, "#ff4f7b"), (1, "#c8104a"), cx=.35, cy=.3)
    + lg("bottle", (0, "#e8f8ff"), (1, "#8ad0f8"))
    + lg("milk", (0, "#ffffff"), (1, "#f0ece4"))
    + lg("cap", (0, "#ffc070"), (1, "#f07a1a")),
    f'''<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .22, 20, 256, 230)}
{bokeh(9, "#ffffff", 12, 6, 22, (.25, .6))}
<ellipse cx="256" cy="476" rx="150" ry="20" fill="#b03060" opacity=".35" filter="url(#blur)"/>
<g filter="url(#sh)">
  <circle cx="98" cy="290" r="42" fill="url(#skin)" stroke="#8a4a2a" stroke-width="5"/>
  <circle cx="414" cy="290" r="42" fill="url(#skin)" stroke="#8a4a2a" stroke-width="5"/>
  <circle cx="256" cy="290" r="170" fill="url(#skin)" stroke="#8a4a2a" stroke-width="6"/>
</g>
<circle cx="98" cy="290" r="18" fill="#f0a888" opacity=".6"/><circle cx="414" cy="290" r="18" fill="#f0a888" opacity=".6"/>
<path d="M92 250 Q100 116 256 112 Q412 116 420 250 Q390 170 310 166 Q280 196 236 168 Q150 172 92 250 Z" fill="url(#hair)" stroke="#2a1006" stroke-width="5" stroke-linejoin="round"/>
<path d="M244 116 Q262 50 316 70 Q290 76 284 112" fill="url(#hair)" stroke="#2a1006" stroke-width="5" stroke-linejoin="round"/>
<path d="M150 170 Q200 136 260 138" fill="none" stroke="#c8885a" stroke-width="8" stroke-linecap="round" opacity=".7"/>
<g>
  <ellipse cx="190" cy="296" rx="34" ry="42" fill="url(#eye)"/><ellipse cx="322" cy="296" rx="34" ry="42" fill="url(#eye)"/>
  <circle cx="202" cy="280" r="13" fill="#fff"/><circle cx="334" cy="280" r="13" fill="#fff"/>
  <circle cx="180" cy="310" r="6" fill="#fff" opacity=".85"/><circle cx="312" cy="310" r="6" fill="#fff" opacity=".85"/>
  <path d="M150 262 Q160 246 172 254 M362 262 Q352 246 340 254" stroke="#2a1006" stroke-width="5" fill="none" stroke-linecap="round"/>
</g>
<ellipse cx="140" cy="354" rx="42" ry="26" fill="url(#blush)"/><ellipse cx="372" cy="354" rx="42" ry="26" fill="url(#blush)"/>
<path d="M226 364 Q256 400 286 364 Q256 378 226 364 Z" fill="#ff5a7a" stroke="#8a2a2a" stroke-width="5" stroke-linejoin="round"/>
<ellipse cx="256" cy="380" rx="12" ry="6" fill="#ffb0c0"/>
<path d="M150 200 Q190 180 230 190" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".35"/>
<g filter="url(#sh2)" stroke="#8a1038" stroke-width="5" stroke-linejoin="round">
  <path d="M82 104 c-22 -30 -66 -2 -36 34 l36 32 l36 -32 c30 -36 -14 -64 -36 -34 Z" fill="url(#heart)"/>
  <path d="M436 132 c-16 -22 -50 -2 -28 26 l28 24 l28 -24 c22 -28 -12 -48 -28 -26 Z" fill="url(#heart)"/>
  <path d="M456 420 c-10 -14 -32 0 -18 16 l18 16 l18 -16 c14 -16 -8 -30 -18 -16 Z" fill="url(#heart)"/>
</g>
<g fill="#fff" opacity=".8"><ellipse cx="66" cy="102" rx="9" ry="6"/><ellipse cx="424" cy="130" rx="7" ry="5"/></g>
<g transform="translate(78 430) rotate(-18)" filter="url(#sh)" stroke="#2a5a8a" stroke-width="5" stroke-linejoin="round">
  <path d="M-12 -98 Q0 -122 12 -98 L14 -80 L-14 -80 Z" fill="url(#cap)"/>
  <rect x="-26" y="-82" width="52" height="18" rx="6" fill="url(#cap)"/>
  <rect x="-34" y="-64" width="68" height="104" rx="24" fill="url(#bottle)"/>
  <rect x="-28" y="-20" width="56" height="54" rx="18" fill="url(#milk)" stroke="none"/>
  <path d="M-34 -30 H-14 M-34 -6 H-18 M-34 18 H-14" stroke-width="4"/>
  <rect x="-24" y="-56" width="10" height="80" rx="5" fill="#fff" opacity=".7" stroke="none"/>
</g>
{sparkle(400, 210, .8)}{sparkle(120, 190, .6)}{sparkle(380, 440, .6)}
''')

# ---------------------------------------------------------------- 별빛 기사
ICONS["starknight"] = icon(
    rg("bg", (0, "#4a5ad8"), (.5, "#22207a"), (1, "#0a0828"), cy=.35, r=.85)
    + lg("helm", (0, "#ffffff"), (.45, "#d4dcec"), (1, "#7d8aa8"))
    + lg("helmDark", (0, "#a8b4cc"), (1, "#5a6680"))
    + lg("plume", (0, "#fff07a"), (.5, "#ffc21a"), (1, "#d87a00"))
    + lg("cape", (0, "#ff5a4a"), (1, "#9a1a20"))
    + lg("blade", (0, "#ffffff"), (.5, "#e6eeff"), (1, "#9ab0e0"), x2=1, y2=0)
    + rg("bladeGlow", (0, "#bfe0ff", .9), (1, "#7ab8ff", 0))
    + rg("star", (0, "#fffbe0"), (.5, "#ffd84a"), (1, "#e89a00"), cx=.4, cy=.35)
    + rg("starGlow", (0, "#ffe680", .9), (1, "#ffc634", 0))
    + rg("visor", (0, "#6ab8ff"), (1, "#0a1430")),
    f'''<rect width="512" height="512" fill="url(#bg)"/>
{stars(17, 46, (0, 0, 512, 512))}
{rays("#bfd0ff", .08, 18, 256, 230)}
<path d="M0 430 L60 410 L60 380 L90 380 L90 410 L150 400 L150 360 L170 340 L190 360 L190 400 L330 400 L330 350 L350 330 L370 350 L370 405 L430 410 L430 385 L460 385 L460 415 L512 420 L512 512 L0 512 Z" fill="#14123a"/>
<ellipse cx="256" cy="470" rx="150" ry="22" fill="#000" opacity=".5" filter="url(#blur)"/>
<g filter="url(#sh)">
  <path d="M150 300 Q120 400 96 470 L230 440 L250 330 Z" fill="url(#cape)" stroke="#3a0608" stroke-width="6" stroke-linejoin="round"/>
  <path d="M362 300 Q392 400 416 470 L282 440 L262 330 Z" fill="url(#cape)" stroke="#3a0608" stroke-width="6" stroke-linejoin="round"/>
</g>
<g filter="url(#sh)" stroke="#1a2040" stroke-width="6" stroke-linejoin="round">
  <path d="M256 92 Q300 40 366 58 Q330 70 318 100 Q356 92 380 116 Q330 118 300 140 Z" fill="url(#plume)"/>
  <path d="M146 250 Q146 120 256 116 Q366 120 366 250 L366 330 Q366 380 256 392 Q146 380 146 330 Z" fill="url(#helm)"/>
  <path d="M170 236 L342 236 Q348 236 348 244 L348 262 Q348 270 340 270 L172 270 Q164 270 164 262 L164 244 Q164 236 170 236 Z" fill="url(#visor)"/>
  <path d="M256 122 L256 236" stroke="#8a96b0" stroke-width="10"/>
  <path d="M190 300 L322 300 M196 330 L316 330" stroke="#8a96b0" stroke-width="7" fill="none"/>
  <path d="M146 330 Q146 380 256 392 Q366 380 366 330 Q300 360 256 360 Q212 360 146 330 Z" fill="url(#helmDark)"/>
</g>
<path d="M176 160 Q210 128 256 126" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" opacity=".7"/>
<g fill="#ffe680"><rect x="206" y="246" width="26" height="12" rx="4"/><rect x="282" y="246" width="26" height="12" rx="4"/></g>
<g filter="url(#glow)" opacity=".85"><rect x="206" y="246" width="26" height="12" rx="4" fill="#bfe6ff"/><rect x="282" y="246" width="26" height="12" rx="4" fill="#bfe6ff"/></g>
<g transform="translate(442 410) rotate(-12)">
  <ellipse cx="0" cy="-150" rx="40" ry="170" fill="url(#bladeGlow)"/>
  <g filter="url(#sh)" stroke="#1a2040" stroke-width="6" stroke-linejoin="round">
    <path d="M-16 -20 L-16 -270 L0 -306 L16 -270 L16 -20 Z" fill="url(#blade)"/>
    <rect x="-52" y="-24" width="104" height="22" rx="10" fill="url(#plume)"/>
    <rect x="-11" y="-4" width="22" height="56" rx="6" fill="#7a4a24"/>
    <circle cx="0" cy="62" r="14" fill="url(#plume)"/>
  </g>
  <path d="M0 -280 L0 -40" stroke="#fff" stroke-width="5" opacity=".8"/>
</g>
<circle cx="110" cy="150" r="70" fill="url(#starGlow)"/>
<g transform="translate(110 150) rotate(-14)" filter="url(#sh2)">
  <path d="M0 -44 L13 -14 L44 -12 L20 8 L28 40 L0 22 L-28 40 L-20 8 L-44 -12 L-13 -14 Z" fill="url(#star)" stroke="#8a5200" stroke-width="5" stroke-linejoin="round"/>
</g>
{sparkle(430, 90, .9)}{sparkle(70, 300, .6)}{sparkle(300, 70, .5, "#fff6c0")}
''')

# ---------------------------------------------------------------- default
ICONS["default"] = icon(
    rg("bg", (0, "#7aa8ff"), (1, "#2a1aa8"), cy=.3, r=.9)
    + lg("pad", (0, "#ffffff"), (1, "#d0d6f0")),
    f'''<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .1)}
<g filter="url(#sh)" stroke="#1a1050" stroke-width="7" stroke-linejoin="round">
  <path d="M110 210 Q110 160 170 160 L342 160 Q402 160 402 210 L430 340 Q440 396 384 396 Q350 396 330 352 L182 352 Q162 396 128 396 Q72 396 82 340 Z" fill="url(#pad)"/>
  <path d="M170 224 V296 M134 260 H206" stroke-width="22" stroke-linecap="round"/>
  <circle cx="334" cy="236" r="20" fill="#ff4f7b"/><circle cx="374" cy="280" r="20" fill="#ffc634"/>
</g>
{sparkle(420, 120, .8)}
''')

def dedupe(svg):
    def fix(m):
        tag = m.group(0)
        mm = re.match(r"<(\w+)(.*?)(/?)>$", tag, re.S)
        if not mm: return tag
        d = {}
        for k, v in re.findall(r'([\w:-]+)="([^"]*)"', mm.group(2)): d[k] = v
        return "<" + mm.group(1) + "".join(f' {k}="{v}"' for k, v in d.items()) + mm.group(3) + ">"
    return re.sub(r"<\w+\b[^<>]*?/?>", fix, svg)

OUT.mkdir(exist_ok=True)
for name, svg in ICONS.items():
    svg = dedupe(svg)
    xml.dom.minidom.parseString(svg.encode())
    (OUT / f"{name}.svg").write_text(svg)
    print("wrote", name, len(svg))
