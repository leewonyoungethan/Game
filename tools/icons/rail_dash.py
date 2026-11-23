"""Rail Dash — a runner leaping over a barrier on dusk rail tracks, train lights behind."""
import math
from .common import icon, lg, rg, stars, sparkle

def build():
    defs = (
        lg("sky", (0, "#1a1040"), (.38, "#6a2a80"), (.68, "#ff5a7a"), (1, "#ffb060"))
        + rg("sun", (0, "#fffbe0"), (.5, "#ffd27a"), (1, "#ff8a5a", 0))
        + lg("city", (0, "#3a1a55"), (1, "#22103a"))
        + lg("ground", (0, "#3a2448"), (1, "#140a1e"))
        + lg("bed", (0, "#4c3456"), (1, "#1c1022"))
        + lg("rail", (0, "#ffffff"), (1, "#b8b0d0"), x1=0, y1=0, x2=1, y2=0)
        + lg("train", (0, "#8ad0ff"), (.45, "#2f86f0"), (1, "#123a90"))
        + lg("trainSide", (0, "#1e5ab8"), (1, "#0c2a6a"), x1=0, y1=0, x2=1, y2=0)
        + rg("lamp", (0, "#ffffff"), (.2, "#fff4b0", .95), (1, "#fff4b0", 0))
        + lg("beam", (0, "#fff4c0", .45), (1, "#fff4c0", 0))
        + lg("hood", (0, "#86fff0"), (.5, "#2ad6bc"), (1, "#128a7a"))
        + lg("pack", (0, "#ffc07a"), (.5, "#ff8a3a"), (1, "#c8500e"))
        + lg("jeans", (0, "#5a6ab8"), (1, "#22306a"))
        + lg("cap", (0, "#ff8ab4"), (1, "#d8286a"))
        + rg("coin", (0, "#fffbd8"), (.45, "#ffd23a"), (1, "#c07a00"), cx=.38, cy=.32)
        + rg("coinGlow", (0, "#ffd23a", .55), (1, "#ffd23a", 0))
        + lg("trail", (0, "#7affe6", 0), (1, "#7affe6", .65), x1=0, y1=0, x2=1, y2=0)
        + lg("bar", (0, "#ffe25a"), (1, "#f0a800"))
    )
    # tracks: two lines of rails converging on (256, 232)
    VX, VY = 256, 232
    def at(x_bottom, y):              # point on a line from (x_bottom,512) to the vanishing point
        t = (512 - y) / (512 - VY)
        return x_bottom + (VX - x_bottom) * t
    sleepers = []
    for k in range(12):
        y = VY + (512 - VY) * (1 - (0.82 ** k))
        y = 512 - (512 - VY) * (0.78 ** (k + .3))
        x0, x1 = at(80, y), at(432, y)
        w = max(2, 20 * (y - VY) / (512 - VY))
        sleepers.append(f'<path d="M{x0+2:.1f} {y:.1f} H{x1-2:.1f}" stroke="#7a5446" stroke-width="{w:.1f}"/>')
    coins = []
    for i, (x, y, r) in enumerate([(120, 200, 18), (150, 160, 21), (190, 136, 24)]):
        coins.append(f'<circle cx="{x}" cy="{y}" r="{r*2}" fill="url(#coinGlow)"/>'
                     f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r}" fill="url(#coin)" stroke="#7a4600" stroke-width="4"/>'
                     f'<ellipse cx="{x}" cy="{y}" rx="{r*.5:.1f}" ry="{r*.62:.1f}" fill="none" stroke="#c88a00" stroke-width="3"/>'
                     f'<rect x="{x-r*.55:.1f}" y="{y-r*.55:.1f}" width="{r*.22:.1f}" height="{r*.7:.1f}" rx="2" fill="#fff" opacity=".85"/>')
    O = 'stroke="#140a24" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{stars(5, 24, (0, 0, 512, 120))}
<circle cx="350" cy="214" r="120" fill="url(#sun)"/>
<g fill="url(#city)">
  <rect x="0" y="150" width="44" height="90"/><rect x="48" y="118" width="34" height="122"/><rect x="86" y="166" width="54" height="74"/><rect x="144" y="186" width="30" height="54"/>
  <rect x="338" y="176" width="34" height="64"/><rect x="376" y="130" width="42" height="110"/><rect x="422" y="160" width="50" height="80"/><rect x="476" y="108" width="36" height="132"/>
  <path d="M60 118 L65 96 L70 118 Z"/><path d="M490 108 L494 84 L498 108 Z"/>
</g>
<g fill="#ffcc6a" opacity=".55">
  <rect x="56" y="130" width="5" height="6"/><rect x="66" y="148" width="5" height="6"/><rect x="56" y="170" width="5" height="6"/><rect x="96" y="178" width="5" height="6"/>
  <rect x="386" y="144" width="5" height="6"/><rect x="398" y="168" width="5" height="6"/><rect x="430" y="174" width="5" height="6"/><rect x="486" y="122" width="5" height="6"/><rect x="486" y="150" width="5" height="6"/>
</g>
<rect y="232" width="512" height="280" fill="url(#ground)"/>
<path d="M{VX-14} {VY} L{VX+14} {VY} L472 512 L40 512 Z" fill="url(#bed)"/>
<g>{''.join(sleepers)}</g>
<path d="M{VX-8} {VY} L104 512" stroke="url(#rail)" stroke-width="8"/><path d="M{VX+8} {VY} L408 512" stroke="url(#rail)" stroke-width="8"/>
<!-- train -->
<path d="M206 238 L60 512 L452 512 L306 238 Z" fill="url(#beam)" opacity=".5"/>
<g filter="url(#sh2)">
  <path d="M198 138 Q198 108 226 106 L286 106 Q314 108 314 138 L318 252 L194 252 Z" fill="url(#train)" stroke="#0a1a40" stroke-width="5" stroke-linejoin="round"/>
  <rect x="212" y="124" width="88" height="48" rx="10" fill="#0c1428" stroke="#0a1a40" stroke-width="4"/>
  <path d="M220 130 L244 130 L228 166 L216 166 Z" fill="#fff" opacity=".28"/>
  <rect x="196" y="204" width="120" height="8" fill="#fff" opacity=".9"/>
  <rect x="236" y="96" width="40" height="12" rx="4" fill="#ff5a7a" stroke="#0a1a40" stroke-width="3"/>
</g>
<circle cx="222" cy="232" r="38" fill="url(#lamp)"/><circle cx="290" cy="232" r="38" fill="url(#lamp)"/>
<!-- coins -->
{''.join(coins)}
<!-- barrier -->
<g transform="translate(256 438)" filter="url(#sh2)">
  <rect x="-128" y="20" width="14" height="54" fill="#2a1830"/><rect x="114" y="20" width="14" height="54" fill="#2a1830"/>
  <rect x="-142" y="-12" width="284" height="40" rx="8" fill="url(#bar)" stroke="#2a1404" stroke-width="5"/>
  <path d="M-116 -12 L-88 28 M-56 -12 L-28 28 M4 -12 L32 28 M64 -12 L92 28 M118 -12 L134 14" stroke="#2a1404" stroke-width="18"/>
  <rect x="-136" y="-8" width="272" height="5" rx="2" fill="#fff" opacity=".5"/>
</g>
<!-- motion trail -->
<path d="M80 420 Q170 330 262 316" stroke="url(#trail)" stroke-width="56" fill="none" stroke-linecap="round" opacity=".45" filter="url(#b2)"/>
<!-- runner (from behind, mid-leap) -->
<g transform="translate(276 300) rotate(-8)" filter="url(#sh)">
  <path d="M-18 42 Q-52 58 -84 102" stroke="url(#jeans)" stroke-width="32" fill="none" stroke-linecap="round"/>
  <path d="M16 40 Q54 52 64 100" stroke="url(#jeans)" stroke-width="32" fill="none" stroke-linecap="round"/>
  <path d="M-18 42 Q-52 58 -84 102 M16 40 Q54 52 64 100" stroke="#140a24" stroke-width="40" fill="none" stroke-linecap="round" opacity="0"/>
  <g {O}>
    <path d="M-104 96 Q-104 82 -88 84 L-64 100 Q-60 116 -76 116 L-98 114 Q-108 110 -104 96 Z" fill="#ffffff"/>
    <path d="M48 106 Q50 92 64 94 L88 104 Q94 120 78 122 L56 122 Q46 118 48 106 Z" fill="#ffffff"/>
    <path d="M-34 -40 Q-80 -60 -108 -102" stroke="url(#hood)" stroke-width="30" fill="none"/>
    <path d="M34 -36 Q76 -26 108 -60" stroke="url(#hood)" stroke-width="30" fill="none"/>
    <circle cx="-110" cy="-108" r="17" fill="#ffcfa8"/><circle cx="112" cy="-64" r="17" fill="#ffcfa8"/>
    <rect x="-52" y="-84" width="104" height="134" rx="40" fill="url(#hood)"/>
    <rect x="-36" y="-66" width="72" height="84" rx="20" fill="url(#pack)"/>
    <rect x="-24" y="-30" width="48" height="26" rx="8" fill="#ffb070" stroke-width="4"/>
    <path d="M-30 -66 L-40 -84 M30 -66 L40 -84" stroke-width="5"/>
    <circle cx="0" cy="-118" r="42" fill="#3a2416"/>
    <path d="M-44 -122 A44 44 0 0 1 44 -122 L66 -112 L-44 -112 Z" fill="url(#cap)"/>
    <path d="M-30 -140 Q0 -158 30 -140" stroke="#fff" stroke-width="5" fill="none" opacity=".55"/>
  </g>
  <path d="M-46 -60 Q-44 -10 -40 34" stroke="#fff" stroke-width="5" opacity=".35" fill="none" stroke-linecap="round"/>
</g>
{sparkle(430, 300, .7, "#fff6c0")}{sparkle(90, 290, .5)}{sparkle(214, 108, .5, "#fff6c0")}
'''
    return icon(defs, art)
