"""개구리 연잎 점프 — on a sunny pond, a chubby green frog leaps joyfully between spinning lily pads,
a dotted arc behind it, a lotus blooming and droplets flying."""
from .common import icon, lg, rg, sparkle

def pad(cx, cy, r, rot=0, flower=False, tilt=.42):
    return (f'<g transform="translate({cx} {cy}) scale(1 {tilt}) rotate({rot})">'
            f'<ellipse cx="0" cy="8" rx="{r * 1.02:.1f}" ry="{r * 1.02:.1f}" fill="#0e4a5a" opacity=".22"/>'
            f'<path d="M0 0 L{r * .98:.1f} {-r * .2:.1f} A{r} {r} 0 1 0 {r * .98:.1f} {r * .2:.1f} Z" fill="url(#pad)" stroke="#1e7a3a" stroke-width="5"/>'
            f'<g stroke="#2e9a4a" stroke-width="3" opacity=".7">{"".join(f"<path d=\"M0 0 L{r * .9 * __import__("math").cos(a):.1f} {r * .9 * __import__("math").sin(a):.1f}\"/>" for a in [1.0, 1.9, 2.8, 3.7, 4.6, 5.5])}</g>'
            f'<ellipse cx="{-r * .35:.1f}" cy="{-r * .4:.1f}" rx="{r * .3:.1f}" ry="{r * .14:.1f}" fill="#fff" opacity=".35"/></g>')

def lotus(x, y, s):
    petals = "".join(f'<path d="M0 0 C-14 -20 -10 -46 0 -56 C10 -46 14 -20 0 0 Z" fill="url(#petal)" stroke="#c8407a" stroke-width="3" transform="rotate({a})"/>' for a in (-60, -30, 30, 60, 0))
    return f'<g transform="translate({x} {y}) scale({s})">{petals}<circle cy="-8" r="9" fill="#ffd24a"/></g>'

def build():
    defs = (lg("water", (0, "#5ad8f0"), (.55, "#2aa8d8"), (1, "#1a6aa8"))
            + rg("sunsp", (0, "#ffffff", .9), (1, "#ffffff", 0))
            + rg("pad", (0, "#a8f070"), (.7, "#5ac83a"), (1, "#2a9a30"), cx=.4, cy=.35)
            + rg("frog", (0, "#d8ff8a"), (.45, "#7ae04a"), (1, "#2aa83a"), cx=.38, cy=.3)
            + rg("belly", (0, "#ffffe8"), (1, "#f0f0a8"))
            + lg("petal", (0, "#ffe0f0"), (1, "#ff7ab0"))
            + rg("eye", (0, "#ffffff"), (1, "#e8f0e0")))
    O = 'stroke="#1a5a22" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"'
    ripples = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * .32}" fill="none" stroke="#fff" stroke-width="4" opacity="{o}"/>' for x, y, r, o in [(150, 420, 60, .55), (150, 420, 92, .3), (420, 250, 40, .45), (90, 230, 34, .4)])
    caustics = "".join(f'<path d="M{x} {y} q20 -10 40 0 t40 0" stroke="#bff4ff" stroke-width="4" fill="none" opacity=".35" stroke-linecap="round"/>' for x, y in [(20, 120), (300, 90), (380, 340), (40, 330), (250, 470), (420, 460), (180, 170)])
    art = f'''
<rect width="512" height="512" fill="url(#water)"/>
{caustics}
<ellipse cx="400" cy="70" rx="200" ry="110" fill="url(#sunsp)" opacity=".55"/>
<!-- reeds -->
<g stroke-linecap="round">
  <path d="M470 512 Q462 380 480 300" stroke="#3a8a3a" stroke-width="10" fill="none"/><path d="M492 512 Q500 400 490 330" stroke="#2a7a2a" stroke-width="8" fill="none"/>
  <rect x="472" y="286" width="16" height="50" rx="8" fill="#8a5a2a"/>
  <path d="M30 512 Q40 410 20 350" stroke="#3a8a3a" stroke-width="10" fill="none"/><rect x="10" y="334" width="16" height="48" rx="8" fill="#8a5a2a" transform="rotate(-10 18 358)"/>
</g>
{ripples}
{pad(150, 420, 100, 20)}{pad(430, 250, 62, -120)}{pad(70, 300, 52, 60)}{pad(360, 470, 70, 200)}
{lotus(118, 410, .9)}{lotus(378, 462, .7)}
<!-- jump arc -->
<path d="M160 400 Q210 170 400 230" stroke="#fff" stroke-width="7" stroke-dasharray="2 18" stroke-linecap="round" fill="none" opacity=".9"/>
<!-- droplets from take-off -->
<g fill="#e8fcff">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r * .7}" ry="{r}" transform="rotate({a} {x} {y})"/>' for x, y, r, a in [(176, 360, 8, -20), (150, 350, 6, -40), (198, 372, 6, 10), (130, 372, 5, -60)])}</g>
<!-- frog mid-leap -->
<g transform="translate(278 210) rotate(-14)">
  <g filter="url(#sh)">
    <!-- back legs stretched -->
    <path d="M-54 40 Q-120 70 -150 120 Q-130 128 -112 112 Q-90 80 -44 66 Z" fill="url(#frog)" {O}/>
    <path d="M-150 120 q-14 6 -20 -4 M-150 120 q-6 14 -18 12 M-150 120 q4 14 -6 22" stroke="#1a5a22" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path d="M-20 70 Q-60 110 -80 160 Q-60 164 -50 150 Q-34 112 4 86 Z" fill="url(#frog)" {O}/>
    <!-- body -->
    <ellipse cx="0" cy="20" rx="96" ry="78" fill="url(#frog)" {O}/>
    <ellipse cx="18" cy="48" rx="58" ry="40" fill="url(#belly)"/>
    <!-- front arms reaching -->
    <path d="M70 30 Q118 20 140 -6" stroke="url(#frog)" stroke-width="22" fill="none" stroke-linecap="round"/>
    <path d="M70 30 Q118 20 140 -6" stroke="#1a5a22" stroke-width="30" fill="none" stroke-linecap="round" opacity="0"/>
    <g fill="#7ae04a" stroke="#1a5a22" stroke-width="5"><circle cx="146" cy="-12" r="9"/><circle cx="134" cy="-20" r="8"/><circle cx="154" cy="0" r="8"/></g>
    <!-- eyes -->
    <circle cx="-30" cy="-46" r="34" fill="url(#frog)" {O}/><circle cx="40" cy="-50" r="34" fill="url(#frog)" {O}/>
  </g>
  <circle cx="-30" cy="-46" r="22" fill="url(#eye)"/><circle cx="40" cy="-50" r="22" fill="url(#eye)"/>
  <circle cx="-24" cy="-44" r="12" fill="#1a1a1a"/><circle cx="46" cy="-48" r="12" fill="#1a1a1a"/>
  <circle cx="-20" cy="-50" r="5" fill="#fff"/><circle cx="50" cy="-54" r="5" fill="#fff"/>
  <path d="M-26 6 Q14 46 60 4" stroke="#1a5a22" stroke-width="8" fill="#e84a6a" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M-8 22 Q14 36 38 22" fill="#ff8aa8"/>
  <ellipse cx="-56" cy="0" rx="14" ry="8" fill="#ff8aa8" opacity=".6"/><ellipse cx="84" cy="-8" rx="14" ry="8" fill="#ff8aa8" opacity=".6"/>
  <g fill="#3aa83a" opacity=".5"><circle cx="-60" cy="40" r="7"/><circle cx="-40" cy="60" r="5"/><circle cx="-70" cy="16" r="4"/></g>
  <path d="M-60 -10 Q-70 -40 -50 -60" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" opacity=".4"/>
</g>
<!-- dragonfly -->
<g transform="translate(96 120) rotate(16)">
  <ellipse cx="0" cy="0" rx="34" ry="5" fill="#2a6ad8"/><circle cx="36" cy="0" r="8" fill="#2a6ad8"/>
  <g fill="#e8fbff" opacity=".8" stroke="#8ad0ff" stroke-width="2"><ellipse cx="8" cy="-16" rx="8" ry="20" transform="rotate(-30 8 -16)"/><ellipse cx="8" cy="16" rx="8" ry="20" transform="rotate(30 8 16)"/><ellipse cx="-6" cy="-14" rx="6" ry="16" transform="rotate(-50 -6 -14)"/><ellipse cx="-6" cy="14" rx="6" ry="16" transform="rotate(50 -6 14)"/></g>
</g>
{sparkle(420, 330, .7)}{sparkle(60, 90, .6)}{sparkle(250, 60, .5)}
'''
    return icon(defs, art)
