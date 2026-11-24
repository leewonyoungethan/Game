"""등불 던전 — a hooded little adventurer raising a glowing lantern in a stone dungeon, glowing eyes lurking in the dark."""
from .common import icon, lg, rg, sparkle

def build():
    defs = (rg("dark", (0, "#5a3e22"), (.45, "#2a1c10"), (1, "#0a0604"), cx=.5, cy=.48, r=.62)
            + rg("light", (0, "#fff2c0", .85), (.35, "#ffb84a", .45), (1, "#ff8a2a", 0))
            + rg("flame", (0, "#ffffff"), (.4, "#fff0a0"), (1, "#ffa83a"))
            + lg("cloak", (0, "#4a6ac8"), (1, "#1e3478"))
            + lg("brass", (0, "#ffd88a"), (1, "#a8701a"))
            + rg("skin", (0, "#ffe4c8"), (1, "#f0b890")))
    bricks = []
    for r in range(13):
        y = r * 40; off = (r % 2) * 40
        for c in range(-1, 8):
            x = c * 80 + off
            bricks.append(f'<rect x="{x + 3}" y="{y + 3}" width="74" height="34" rx="5"/>')
    art = f'''
<rect width="512" height="512" fill="#1a120a"/>
<g fill="#3a2a1a" opacity=".9">{''.join(bricks)}</g>
<rect width="512" height="512" fill="url(#dark)" opacity=".85" style="mix-blend-mode:multiply"/>
<circle cx="300" cy="230" r="300" fill="url(#light)"/>
<!-- lurking eyes -->
<g fill="#ff4a3a" filter="url(#glowS)"><ellipse cx="62" cy="120" rx="9" ry="5"/><ellipse cx="94" cy="120" rx="9" ry="5"/><ellipse cx="446" cy="430" rx="8" ry="4.5"/><ellipse cx="474" cy="430" rx="8" ry="4.5"/></g>
<g fill="#ffe06a" filter="url(#glowS)" opacity=".8"><ellipse cx="458" cy="96" rx="6" ry="6"/><ellipse cx="482" cy="96" rx="6" ry="6"/></g>
<!-- floor -->
<ellipse cx="236" cy="466" rx="170" ry="26" fill="#000" opacity=".45"/>
<!-- adventurer -->
<g transform="translate(220 300)">
  <g filter="url(#sh)">
    <path d="M-92 166 Q-104 20 -10 -40 Q60 -60 96 40 Q112 120 100 166 Z" fill="url(#cloak)" stroke="#0e1a40" stroke-width="7" stroke-linejoin="round"/>
    <circle cx="0" cy="-70" r="66" fill="url(#skin)" stroke="#3a2010" stroke-width="7"/>
    <path d="M-80 -40 Q-92 -150 0 -158 Q92 -150 80 -40 Q64 -110 0 -116 Q-64 -110 -80 -40 Z" fill="url(#cloak)" stroke="#0e1a40" stroke-width="7" stroke-linejoin="round"/>
  </g>
  <path d="M-96 76 Q0 96 104 70" stroke="#6a3e1a" stroke-width="16" fill="none" stroke-linecap="round"/>
  <rect x="-14" y="72" width="28" height="22" rx="5" fill="url(#brass)" stroke="#5a3a08" stroke-width="4"/>
  <g transform="translate(-84 110) rotate(-30)"><rect x="-6" y="-10" width="12" height="96" rx="4" fill="#d8e0f0" stroke="#3a4050" stroke-width="4"/><rect x="-22" y="-18" width="44" height="12" rx="5" fill="url(#brass)" stroke="#5a3a08" stroke-width="4"/><rect x="-6" y="-46" width="12" height="30" rx="4" fill="#6a3e1a" stroke="#2a1608" stroke-width="4"/></g>
  <ellipse cx="-22" cy="-66" rx="9" ry="13" fill="#1a0e08"/><ellipse cx="28" cy="-66" rx="9" ry="13" fill="#1a0e08"/>
  <circle cx="-19" cy="-71" r="3.5" fill="#fff"/><circle cx="31" cy="-71" r="3.5" fill="#fff"/>
  <ellipse cx="-44" cy="-42" rx="13" ry="7" fill="#ff8a8a" opacity=".5"/><ellipse cx="50" cy="-42" rx="13" ry="7" fill="#ff8a8a" opacity=".5"/>
  <path d="M-6 -36 Q4 -28 14 -36" stroke="#3a2010" stroke-width="5" fill="none" stroke-linecap="round"/>
  <!-- arm up holding lantern -->
  <path d="M60 20 Q110 -10 120 -70" stroke="#1e3478" stroke-width="30" fill="none" stroke-linecap="round"/>
  <circle cx="120" cy="-74" r="16" fill="url(#skin)" stroke="#3a2010" stroke-width="5"/>
</g>
<!-- lantern -->
<g transform="translate(340 170)">
  <path d="M0 -70 Q0 -96 -18 -96 M0 -70 Q0 -96 18 -96" stroke="#6a4a1a" stroke-width="6" fill="none"/>
  <circle cx="0" cy="-10" r="150" fill="url(#light)"/>
  <g filter="url(#sh2)">
    <path d="M-40 -60 L40 -60 L30 -74 L-30 -74 Z" fill="url(#brass)" stroke="#5a3a08" stroke-width="5" stroke-linejoin="round"/>
    <rect x="-38" y="-60" width="76" height="92" rx="12" fill="#fff4c8" fill-opacity=".35" stroke="url(#brass)" stroke-width="9"/>
    <rect x="-44" y="30" width="88" height="16" rx="6" fill="url(#brass)" stroke="#5a3a08" stroke-width="5"/>
  </g>
  <path d="M0 18 C-24 0 -12 -26 0 -46 C12 -26 24 0 0 18 Z" fill="url(#flame)" filter="url(#glow)"/>
  <path d="M0 10 C-10 0 -6 -14 0 -24 C6 -14 10 0 0 10 Z" fill="#fff"/>
  <path d="M-38 -14 H38 M0 -60 V32" stroke="#a8701a" stroke-width="4" opacity=".7"/>
</g>
{sparkle(400, 90, .7, "#fff6c0")}{sparkle(250, 120, .45, "#fff6c0")}
'''
    return icon(defs, art)
