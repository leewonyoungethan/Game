"""고요한 낚시터 — a straw-hatted cat fishing at golden hour as a big fish leaps from the lake."""
from .common import icon, lg, rg, sparkle

def build():
    defs = (
        lg("sky", (0, "#6a5ac8"), (.45, "#ff8a7a"), (1, "#ffd08a"))
        + rg("sun", (0, "#fffbe0"), (.6, "#ffe08a"), (1, "#ffb05a", 0))
        + lg("lake", (0, "#5ab0d8"), (1, "#1a5a8a"))
        + lg("mount", (0, "#8a6ab8"), (1, "#5a4a8a"))
        + rg("cat", (0, "#ffd6a0"), (.6, "#ffa856"), (1, "#d8762a"), cx=.38, cy=.3)
        + lg("hat", (0, "#fff0a0"), (1, "#e0b040"))
        + lg("fish", (0, "#ffb070"), (.5, "#ff7a3a"), (1, "#fff0e0"), x1=0, y1=0, x2=0, y2=1)
        + lg("dock", (0, "#b8784a"), (1, "#6a3e1e"))
    )
    O = 'stroke="#4a2410" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<circle cx="340" cy="250" r="140" fill="url(#sun)"/>
<circle cx="340" cy="250" r="60" fill="#fff3c0"/>
<path d="M-10 276 L80 210 L150 250 L240 186 L330 262 L420 214 L522 268 L522 290 L-10 290 Z" fill="url(#mount)"/>
<rect y="284" width="512" height="228" fill="url(#lake)"/>
<g fill="#fff3c0" opacity=".55">{''.join(f'<rect x="{300 - i*3}" y="{300 + i*16}" width="{80 - i*8}" height="4" rx="2"/>' for i in range(8))}</g>
<g stroke="#fff" stroke-opacity=".25" stroke-width="3" fill="none">{''.join(f'<path d="M-10 {y} q30 -6 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0"/>' for y in (330, 380, 430, 480))}</g>
<!-- leaping fish -->
<g fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"><ellipse cx="400" cy="380" rx="60" ry="14"/><ellipse cx="400" cy="380" rx="90" ry="22" opacity=".5"/></g>
<g transform="translate(392 300) rotate(-38)" filter="url(#sh)">
  <path d="M60 0 L104 -30 L98 0 L104 30 Z" fill="#ff7a3a" stroke="#7a2a0a" stroke-width="5" stroke-linejoin="round"/>
  <ellipse cx="0" cy="0" rx="70" ry="34" fill="url(#fish)" stroke="#7a2a0a" stroke-width="5"/>
  <path d="M-10 -32 Q14 -60 34 -28 Z" fill="#ff7a3a" stroke="#7a2a0a" stroke-width="4" stroke-linejoin="round"/>
  <circle cx="-40" cy="-6" r="9" fill="#fff"/><circle cx="-42" cy="-6" r="5" fill="#1a0a04"/>
  <path d="M-14 -20 Q10 -24 30 -16" stroke="#fff" stroke-width="5" fill="none" opacity=".5" stroke-linecap="round"/>
</g>
<g fill="#e8fbff">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(352, 360, 6), (430, 350, 5), (380, 336, 4), (446, 372, 4), (330, 376, 3)])}</g>
<!-- line + bobber -->
<path d="M262 150 Q330 230 360 362" stroke="#fff" stroke-width="3" fill="none" opacity=".9"/>
<!-- dock -->
<rect x="-20" y="410" width="290" height="40" fill="url(#dock)" stroke="#4a2410" stroke-width="5"/>
<path d="M30 410 V450 M90 410 V450 M150 410 V450 M210 410 V450" stroke="#4a2410" stroke-width="4" opacity=".6"/>
<rect x="40" y="448" width="18" height="70" fill="#5a3418"/><rect x="200" y="448" width="18" height="70" fill="#5a3418"/>
<!-- cat -->
<g transform="translate(150 330)">
  <path d="M-40 70 Q-100 60 -96 0" stroke="#ffa856" stroke-width="20" fill="none" stroke-linecap="round"/>
  <path d="M-40 70 Q-100 60 -96 0" stroke="#4a2410" stroke-width="28" fill="none" stroke-linecap="round" opacity="0"/>
  <g filter="url(#sh)"><ellipse cx="0" cy="40" rx="58" ry="62" fill="url(#cat)" {O}/></g>
  <ellipse cx="10" cy="52" rx="30" ry="38" fill="#fff4e8"/>
  <path d="M62 -40 L120 -184" stroke="#7a4a1a" stroke-width="10" stroke-linecap="round"/>
  <path d="M120 -184 L118 -186" stroke="#c8a86a" stroke-width="6"/>
  <ellipse cx="54" cy="24" rx="20" ry="15" fill="url(#cat)" {O}/>
  <g filter="url(#sh2)">
    <path d="M-44 -60 L-36 -118 L-6 -78 Z M44 -60 L36 -118 L6 -78 Z" fill="url(#cat)" {O}/>
    <circle cx="0" cy="-40" r="56" fill="url(#cat)" {O}/>
  </g>
  <path d="M-34 -74 L-30 -104 L-14 -82 Z M34 -74 L30 -104 L14 -82 Z" fill="#ff9aa8"/>
  <path d="M-28 -40 Q-18 -32 -8 -40 M8 -40 Q18 -32 28 -40" stroke="#4a2410" stroke-width="6" fill="none" stroke-linecap="round"/>
  <ellipse cx="0" cy="-22" rx="7" ry="5" fill="#ff7a9a"/>
  <path d="M-12 -12 Q0 -4 12 -12" stroke="#4a2410" stroke-width="4" fill="none" stroke-linecap="round"/>
  <ellipse cx="-36" cy="-22" rx="11" ry="6" fill="#ff7a9a" opacity=".5"/><ellipse cx="36" cy="-22" rx="11" ry="6" fill="#ff7a9a" opacity=".5"/>
  <g stroke="#4a2410" stroke-width="3" stroke-linecap="round" opacity=".7"><path d="M-44 -24 H-72 M-44 -16 L-70 -8 M44 -24 H72 M44 -16 L70 -8"/></g>
  <ellipse cx="0" cy="-84" rx="78" ry="18" fill="url(#hat)" stroke="#8a6a1a" stroke-width="5"/>
  <path d="M-42 -88 Q-40 -132 0 -132 Q40 -132 42 -88 Z" fill="url(#hat)" stroke="#8a6a1a" stroke-width="5"/>
  <path d="M-42 -96 Q0 -88 42 -96 L42 -86 Q0 -78 -42 -86 Z" fill="#e8403a"/>
</g>
{sparkle(340, 250, 1.0, "#fffbe0")}{sparkle(470, 120, .55)}{sparkle(80, 120, .5)}
'''
    return icon(defs, art)
