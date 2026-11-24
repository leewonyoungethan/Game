"""두더지 팡팡 — a startled mole popping out of its hole as a big toy hammer swings down."""
from .common import icon, lg, rg, sparkle

def build():
    defs = (
        lg("sky", (0, "#7ad4ff"), (1, "#d8f4ff"))
        + lg("grass", (0, "#7ad85a"), (1, "#2e8a2e"))
        + rg("mole", (0, "#d8a47a"), (.65, "#8a5a3a"), (1, "#4a2a14"), cx=.38, cy=.3)
        + rg("muzzle", (0, "#fff2e0"), (1, "#e0b890"), cx=.45, cy=.3)
        + lg("mound", (0, "#b8803e"), (1, "#5a3414"))
        + lg("head", (0, "#ffa0c0"), (.5, "#ff4f80"), (1, "#b8104a"), x1=0, y1=0, x2=0, y2=1)
        + lg("handle", (0, "#e8b070"), (1, "#8a5420"), x1=0, y1=0, x2=1, y2=0)
        + rg("bang", (0, "#fffbe0"), (.4, "#ffe680", .8), (1, "#ffe680", 0))
    )
    O = 'stroke="#3a1c06" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    fence = "".join(f'<rect x="{x}" y="128" width="40" height="80" rx="12" fill="#fff4dc" stroke="#b8905a" stroke-width="4"/>' for x in range(-10, 520, 56))
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g fill="#fff" opacity=".9" filter="url(#b6)"><ellipse cx="90" cy="70" rx="70" ry="18"/><ellipse cx="420" cy="54" rx="60" ry="16"/></g>
{fence}
<rect x="-10" y="150" width="540" height="12" fill="#fff4dc" stroke="#b8905a" stroke-width="3"/>
<rect y="200" width="512" height="312" fill="url(#grass)"/>
{''.join(f'<path d="M{x} 512 l8 -26 l8 26 Z" fill="#2a7a2a"/>' for x in range(0, 520, 34))}
<!-- hole -->
<ellipse cx="226" cy="392" rx="160" ry="56" fill="#6a4220"/>
<ellipse cx="226" cy="396" rx="132" ry="42" fill="#24130a"/>
<!-- mole -->
<g filter="url(#sh)">
  <path d="M116 400 Q110 240 226 230 Q342 240 336 400 Z" fill="url(#mole)" {O}/>
</g>
<ellipse cx="226" cy="340" rx="66" ry="50" fill="url(#muzzle)"/>
<g fill="#1a0e08"><ellipse cx="186" cy="300" rx="14" ry="16"/><ellipse cx="266" cy="300" rx="14" ry="16"/></g>
<g fill="#fff"><circle cx="191" cy="294" r="6"/><circle cx="271" cy="294" r="6"/></g>
<ellipse cx="226" cy="322" rx="22" ry="15" fill="#ff7a9a" stroke="#8a2a3a" stroke-width="4"/>
<ellipse cx="220" cy="317" rx="7" ry="4" fill="#fff" opacity=".7"/>
<path d="M200 352 Q226 380 252 352" stroke="#3a1c06" stroke-width="6" fill="#c8304a" stroke-linecap="round"/>
<rect x="216" y="352" width="9" height="12" rx="2" fill="#fff"/><rect x="227" y="352" width="9" height="12" rx="2" fill="#fff"/>
<ellipse cx="150" cy="330" rx="20" ry="11" fill="#ff7aa8" opacity=".45"/><ellipse cx="302" cy="330" rx="20" ry="11" fill="#ff7aa8" opacity=".45"/>
<path d="M150 264 Q190 240 226 244" stroke="#fff" stroke-width="10" fill="none" opacity=".3" stroke-linecap="round"/>
<g fill="url(#mole)" {O}><ellipse cx="128" cy="392" rx="34" ry="20" transform="rotate(-20 128 392)"/><ellipse cx="324" cy="392" rx="34" ry="20" transform="rotate(20 324 392)"/></g>
<!-- front mound -->
<path d="M50 400 Q226 470 402 400 Q420 470 226 482 Q32 470 50 400 Z" fill="url(#mound)" stroke="#3a1c06" stroke-width="5"/>
<ellipse cx="150" cy="440" rx="30" ry="8" fill="#fff" opacity=".18"/>
<!-- impact burst + hammer -->
<circle cx="292" cy="226" r="96" fill="url(#bang)"/>
<g stroke="#fff" stroke-width="7" stroke-linecap="round"><path d="M268 180 l-16 -30"/><path d="M300 176 l6 -34"/><path d="M330 196 l28 -20"/><path d="M240 200 l-30 -12"/></g>
<g transform="translate(350 160) rotate(-32)" filter="url(#sh)">
  <rect x="-14" y="-10" width="28" height="210" rx="12" fill="url(#handle)" {O}/>
  <rect x="-96" y="-82" width="192" height="92" rx="30" fill="url(#head)" {O} stroke="#6a0a2a"/>
  <rect x="-80" y="-72" width="160" height="18" rx="9" fill="#fff" opacity=".5"/>
  <rect x="-110" y="-74" width="26" height="76" rx="10" fill="#ffd24a" stroke="#6a0a2a" stroke-width="5"/>
  <rect x="84" y="-74" width="26" height="76" rx="10" fill="#ffd24a" stroke="#6a0a2a" stroke-width="5"/>
</g>
<g fill="#ffe06a" stroke="#8a5a00" stroke-width="3"><path d="M190 214 l8 -18 l8 18 l18 6 l-18 6 l-8 18 l-8 -18 l-18 -6 Z"/></g>
{sparkle(420, 300, .7, "#fff6c0")}{sparkle(70, 260, .55)}
'''
    return icon(defs, art)
