"""낱말 탐정 — a magnifying glass over a paper grid of Hangul, one word circled in a marker capsule, with a detective hat."""
from .common import icon, lg, rg, sparkle, text_path

GRID = ["고래다바", "양호랑이", "사나무강", "탐정소리"]

def build():
    defs = (lg("bg", (0, "#2a3470"), (1, "#141a3a"))
            + lg("paper", (0, "#fff8e6"), (1, "#efdcb0"))
            + rg("lens", (0, "#ffffff", .55), (.7, "#bfe8ff", .25), (1, "#7ac0ff", .35), cx=.35, cy=.3)
            + lg("rimG", (0, "#ffe08a"), (.5, "#d89a2a"), (1, "#8a5a10"))
            + lg("handle", (0, "#8a4a2a"), (1, "#4a2010"))
            + lg("hat", (0, "#8a6a4a"), (1, "#4a3420"))
            + rg("spot", (0, "#ffe9a0", .5), (1, "#ffe9a0", 0)))
    cells = []
    x0, y0, s = 92, 120, 82
    for r, row in enumerate(GRID):
        for c, ch in enumerate(row):
            cells.append(text_path(ch, x0 + c * s + s / 2, y0 + r * s + s / 2 + 18, 52, "#3a2a1a"))
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
<circle cx="256" cy="240" r="260" fill="url(#spot)"/>
<g transform="rotate(-6 256 260)">
  <g filter="url(#sh)"><rect x="70" y="98" width="372" height="372" rx="26" fill="url(#paper)"/></g>
  <g stroke="#c8a870" stroke-width="2" opacity=".35">{''.join(f'<path d="M{x0} {y0 + i * s} H{x0 + 4 * s}"/>' for i in range(1, 4))}</g>
  <!-- found word capsules -->
  <rect x="{x0 + 6}" y="{y0 + s + 8}" width="{s * 4 - 12}" height="{s - 16}" rx="{(s - 16) / 2}" fill="#ffb44a" opacity=".6" transform="translate(0 0)"/>
  <line x1="{x0 + s / 2}" y1="{y0 + s / 2}" x2="{x0 + s / 2}" y2="{y0 + s * 2.5}" stroke="#4ac8ff" stroke-width="{s - 18}" stroke-linecap="round" opacity=".5"/>
  {''.join(cells)}
</g>
<!-- magnifying glass -->
<g transform="translate(318 330)">
  <path d="M60 60 L150 150" stroke="#2a0a00" stroke-width="44" stroke-linecap="round" opacity=".35" transform="translate(6 8)"/>
  <path d="M60 60 L150 150" stroke="url(#handle)" stroke-width="38" stroke-linecap="round"/>
  <path d="M70 66 L140 136" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".25"/>
  <g filter="url(#sh)"><circle r="96" fill="none" stroke="url(#rimG)" stroke-width="22"/></g>
  <circle r="85" fill="#fff8e6" opacity=".93"/><circle r="85" fill="url(#lens)"/>
  {text_path("탐", 0, 34, 100, "#e8402a")}
  <path d="M-58 -40 A70 70 0 0 1 -10 -72" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".8"/>
</g>
<!-- detective hat -->
<g transform="translate(118 92) rotate(-14)" filter="url(#sh)">
  <ellipse cx="0" cy="22" rx="96" ry="24" fill="url(#hat)" stroke="#2a1a0a" stroke-width="5"/>
  <path d="M-62 22 Q-66 -46 0 -54 Q66 -46 62 22 Z" fill="url(#hat)" stroke="#2a1a0a" stroke-width="5" stroke-linejoin="round"/>
  <path d="M-63 2 Q0 16 63 2 L62 18 Q0 32 -62 18 Z" fill="#c8402a"/>
  <path d="M-40 -30 Q-20 -46 10 -46" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".3"/>
</g>
{sparkle(440, 70, 1.0)}{sparkle(470, 250, .55)}{sparkle(56, 440, .5)}
'''
    return icon(defs, art)
