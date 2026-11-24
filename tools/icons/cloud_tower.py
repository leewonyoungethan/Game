"""구름 위 블록 탑 — a candy-colored tower of blocks rising through the clouds, the next block sliding in."""
from .common import icon, lg, rg, sparkle

def block(x, y, w, h, hue, depth=16):
    top = f"hsl({hue} 85% 84%)"; side = f"hsl({hue} 60% 46%)"; f1 = f"hsl({hue} 85% 70%)"; f2 = f"hsl({hue} 70% 54%)"
    gid = f"b{hue}"
    wins = "".join(f'<rect x="{wx}" y="{y+12}" width="12" height="13" rx="2" fill="hsl({hue} 90% 93%)" opacity=".6"/>' for wx in range(int(x) + 12, int(x + w) - 18, 24))
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{f1}"/><stop offset="1" stop-color="{f2}"/></linearGradient>'
            f'<path d="M{x} {y} L{x+depth} {y-depth} L{x+w+depth} {y-depth} L{x+w} {y} Z" fill="{top}"/>'
            f'<path d="M{x+w} {y} L{x+w+depth} {y-depth} L{x+w+depth} {y+h-depth} L{x+w} {y+h} Z" fill="{side}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{gid})"/>'
            f'<rect x="{x+5}" y="{y+5}" width="{w-10}" height="5" rx="2.5" fill="#fff" opacity=".45"/>' + wins)

def build():
    defs = lg("sky", (0, "#3a5ad8"), (.5, "#7ab8ff"), (1, "#d8f0ff")) + rg("glow", (0, "#ffffff", .6), (1, "#ffffff", 0))
    blocks = []
    y, w, x = 452, 230, 130
    for i in range(10):
        blocks.append(block(x, y, w, 36, (200 + i * 14) % 360))
        y -= 36
        shrink = [0, 6, 0, 10, 4, 0, 8, 6, 0, 0][i]
        x += shrink / 2 + (3 if i % 2 else -2); w -= shrink
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g fill="#fff" opacity=".9" filter="url(#b2)">
  <ellipse cx="80" cy="150" rx="80" ry="24"/><ellipse cx="120" cy="134" rx="48" ry="24"/>
  <ellipse cx="440" cy="250" rx="90" ry="26"/><ellipse cx="400" cy="236" rx="50" ry="24"/>
</g>
<circle cx="260" cy="90" r="120" fill="url(#glow)"/>
<ellipse cx="256" cy="512" rx="300" ry="70" fill="#5ac85a"/><ellipse cx="256" cy="500" rx="220" ry="40" fill="#7ad86a"/>
<g filter="url(#sh)">{''.join(blocks)}</g>
<!-- sliding block -->
<g opacity=".95" filter="url(#sh2)">{block(330, 52, 180, 36, 340)}</g>
<g stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"><path d="M300 70 h-30 M306 86 h-46"/></g>
<!-- falling cut piece -->
<g transform="translate(70 230) rotate(-22)" filter="url(#sh2)">{block(0, 0, 44, 36, 330, 10)}</g>
<!-- birds -->
<g stroke="#1a2a5a" stroke-width="4" fill="none" stroke-linecap="round" opacity=".7">
  <path d="M60 300 q10 -10 20 0 q10 -10 20 0"/><path d="M410 330 q8 -8 16 0 q8 -8 16 0"/>
</g>
{sparkle(240, 92, 1.0)}{sparkle(470, 150, .55)}{sparkle(60, 420, .5)}
'''
    return icon(defs, art)
