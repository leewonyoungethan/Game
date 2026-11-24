"""햇살 농장 — a beaming sun over striped crop rows, a red barn, and a giant carrot popping out of the soil."""
from .common import icon, lg, rg, sparkle, rays

def build():
    defs = (lg("sky", (0, "#5ab8ff"), (1, "#c8f0ff"))
            + rg("sun", (0, "#fffbe0"), (.6, "#ffe06a"), (1, "#ffb84a"))
            + lg("hill", (0, "#8ae060"), (1, "#4aa83a"))
            + lg("soil", (0, "#b07a48"), (1, "#7a4a26"))
            + lg("carrot", (0, "#ffb05a"), (1, "#f0602a"), x1=0, y1=0, x2=1, y2=0)
            + lg("barn", (0, "#ff6a5a"), (1, "#c8302a")))
    rows = "".join(f'<path d="M{-40 + i * 10} {300 + i * 52} Q256 {280 + i * 52} {552 - i * 10} {300 + i * 52} L{552} {326 + i * 52} Q256 {306 + i * 52} {-40} {326 + i * 52} Z" fill="#8a5630" opacity=".55"/>' for i in range(5))
    sprouts = "".join(
        f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 V-22" stroke="#2a8a2a" stroke-width="5" stroke-linecap="round"/><ellipse cx="-10" cy="-20" rx="11" ry="6" fill="#5ac840" transform="rotate(-30 -10 -20)"/><ellipse cx="10" cy="-24" rx="11" ry="6" fill="#6ad850" transform="rotate(30 10 -24)"/></g>'
        for x, y, s in [(70, 318, .9), (150, 312, .9), (300, 312, .9), (380, 316, .9), (450, 322, .9), (40, 374, 1.1), (130, 366, 1.1), (370, 366, 1.1), (470, 374, 1.1), (90, 426, 1.3), (430, 426, 1.3), (60, 486, 1.5), (470, 486, 1.5)])
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g transform="translate(400 96)">{rays("#fff6b0", .35, 14, 0, 0, 160)}<circle r="62" fill="url(#sun)"/>
  <circle cx="-20" cy="-8" r="7" fill="#7a4a10"/><circle cx="20" cy="-8" r="7" fill="#7a4a10"/><path d="M-18 14 Q0 30 18 14" stroke="#7a4a10" stroke-width="6" fill="none" stroke-linecap="round"/>
  <ellipse cx="-34" cy="10" rx="9" ry="5" fill="#ff8a5a" opacity=".6"/><ellipse cx="34" cy="10" rx="9" ry="5" fill="#ff8a5a" opacity=".6"/></g>
<g fill="#fff" opacity=".95"><ellipse cx="110" cy="90" rx="58" ry="22"/><ellipse cx="140" cy="74" rx="36" ry="24"/><ellipse cx="84" cy="80" rx="26" ry="18"/></g>
<path d="M-10 250 Q120 200 260 236 Q380 200 522 240 L522 300 L-10 300 Z" fill="url(#hill)"/>
<!-- barn -->
<g transform="translate(96 252)" filter="url(#sh2)">
  <path d="M-56 0 V-62 L0 -104 L56 -62 V0 Z" fill="url(#barn)" stroke="#6a1010" stroke-width="6" stroke-linejoin="round"/>
  <path d="M-64 -58 L0 -110 L64 -58" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="-22" y="-44" width="44" height="44" fill="#fff" stroke="#6a1010" stroke-width="5"/><path d="M-22 -44 L22 0 M22 -44 L-22 0" stroke="#c8302a" stroke-width="5"/>
  <circle cx="0" cy="-74" r="10" fill="#fff6c0" stroke="#6a1010" stroke-width="4"/>
</g>
<rect y="290" width="512" height="222" fill="url(#soil)"/>
{rows}
{sprouts}
<!-- giant carrot popping out -->
<g transform="translate(256 400) rotate(12)">
  <ellipse cx="0" cy="62" rx="96" ry="22" fill="#5a3418"/>
  <g filter="url(#sh)">
    <path d="M-48 -30 Q-56 60 0 150 Q56 60 48 -30 Q0 -52 -48 -30 Z" fill="url(#carrot)" stroke="#8a2a08" stroke-width="7" stroke-linejoin="round" transform="translate(0 -60)"/>
  </g>
  <g stroke="#c8501a" stroke-width="5" stroke-linecap="round" opacity=".7"><path d="M-36 -46 h20 M18 -22 h20 M-30 10 h16 M14 40 h14"/></g>
  <path d="M-30 -80 Q-36 -40 -26 10" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round" opacity=".45"/>
  <g transform="translate(0 -92)" stroke="#1e7a1e" stroke-width="5" stroke-linejoin="round">
    <path d="M0 0 C-30 -40 -60 -60 -70 -100 C-40 -90 -14 -60 0 0 Z" fill="#4ac83a"/>
    <path d="M0 0 C0 -50 -4 -90 10 -130 C30 -90 16 -40 0 0 Z" fill="#5ad84a"/>
    <path d="M0 0 C30 -40 60 -56 80 -90 C50 -88 20 -60 0 0 Z" fill="#4ac83a"/>
  </g>
  <circle cx="-16" cy="-40" r="8" fill="#2a1408"/><circle cx="18" cy="-40" r="8" fill="#2a1408"/>
  <circle cx="-13" cy="-44" r="3" fill="#fff"/><circle cx="21" cy="-44" r="3" fill="#fff"/>
  <path d="M-10 -18 Q2 -6 14 -18" stroke="#2a1408" stroke-width="5" fill="none" stroke-linecap="round"/>
</g>
<g fill="#7a4a26">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * .7}"/>' for x, y, r in [(160, 452, 12), (350, 450, 10), (190, 474, 8), (330, 478, 9)])}</g>
{sparkle(330, 210, .8)}{sparkle(180, 300, .5)}{sparkle(470, 220, .45)}
'''
    return icon(defs, art)
