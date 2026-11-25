"""구름 위 블록 탑 — at sunset, a candy-colored skyscraper of stacked blocks rises out of a sea of clouds;
a smiling block drops onto the top in a golden 'perfect' flash."""
from .common import icon, lg, rg, sparkle

def block(x, y, w, h, hue, d=22, face=False, wins=True, gid=None):
    gid = gid or f"bk{hue}_{int(y)}"
    front = (f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="hsl({hue} 80% 72%)"/>'
             f'<stop offset=".55" stop-color="hsl({hue} 75% 62%)"/><stop offset="1" stop-color="hsl({hue} 70% 50%)"/></linearGradient>')
    out = front
    out += f'<path d="M{x} {y} L{x + d} {y - d * .62} L{x + w + d} {y - d * .62} L{x + w} {y} Z" fill="hsl({hue} 90% 86%)"/>'
    out += f'<path d="M{x + w} {y} L{x + w + d} {y - d * .62} L{x + w + d} {y + h - d * .62} L{x + w} {y + h} Z" fill="hsl({hue} 55% 40%)"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{gid})"/>'
    out += f'<rect x="{x}" y="{y}" width="{w}" height="4" fill="#fff" opacity=".55"/>'
    out += f'<rect x="{x}" y="{y + h - 5}" width="{w}" height="5" fill="#000" opacity=".12"/>'
    if wins and not face:
        n = max(2, int(w // 26))
        gap = w / n
        for i in range(n):
            wx = x + i * gap + gap * .22
            lit = (i * 7 + int(y)) % 3 != 0
            out += f'<rect x="{wx:.1f}" y="{y + h * .28:.1f}" width="{gap * .56:.1f}" height="{h * .44:.1f}" rx="3" fill="{"#fff6c8" if lit else f"hsl({hue} 50% 34%)"}" opacity="{.95 if lit else .55}"/>'
    if face:
        cx = x + w / 2; cy = y + h * .55
        out += (f'<ellipse cx="{cx - 18}" cy="{cy - 4}" rx="6.5" ry="9" fill="#2a1430"/><ellipse cx="{cx + 18}" cy="{cy - 4}" rx="6.5" ry="9" fill="#2a1430"/>'
                f'<circle cx="{cx - 16}" cy="{cy - 8}" r="2.6" fill="#fff"/><circle cx="{cx + 20}" cy="{cy - 8}" r="2.6" fill="#fff"/>'
                f'<ellipse cx="{cx - 34}" cy="{cy + 7}" rx="8" ry="5" fill="#ff6a9a" opacity=".55"/><ellipse cx="{cx + 34}" cy="{cy + 7}" rx="8" ry="5" fill="#ff6a9a" opacity=".55"/>'
                f'<path d="M{cx - 9} {cy + 6} Q{cx} {cy + 17} {cx + 9} {cy + 6}" stroke="#2a1430" stroke-width="4" fill="none" stroke-linecap="round"/>')
    return out

def cloud(cx, cy, s, top="#ffffff", bot="#d8c8f0", op=1):
    gid = f"cl{int(cx)}_{int(cy)}"
    return (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/></linearGradient>'
            f'<g transform="translate({cx} {cy}) scale({s})" fill="url(#{gid})" opacity="{op}">'
            '<ellipse cx="0" cy="10" rx="120" ry="34"/><circle cx="-60" cy="-6" r="42"/><circle cx="-8" cy="-30" r="58"/><circle cx="52" cy="-12" r="46"/><circle cx="96" cy="6" r="30"/></g>')

def build():
    defs = (lg("sky", (0, "#2a2a8a"), (.38, "#7a5ad8"), (.68, "#ff8ab0"), (1, "#ffc890"))
            + rg("sun", (0, "#fffbe0"), (.25, "#ffe9a8", .9), (1, "#ff9ab8", 0))
            + rg("flash", (0, "#ffffff"), (.3, "#fff2a0", .9), (1, "#ffd24a", 0))
            + lg("streak", (0, "#ffffff", 0), (1, "#ffffff", .9)))
    hues = [200, 168, 48, 18, 340, 280]
    tower = ""
    y = 470; x = 168; w = 150
    offs = [0, -4, 6, -2, 8, -6, 3]
    for i, hue in enumerate(hues):
        h = 44
        tower = block(x + offs[i], y - h, w, h, hue) + tower if False else tower + block(x + offs[i], y - h, w, h, hue)
        y -= h
    top_y = y
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g fill="#fff">{''.join(f'<circle cx="{(i * 97) % 512}" cy="{(i * 53) % 190}" r="{1 + (i % 3) * .6}" opacity="{.4 + (i % 4) * .15}"/>' for i in range(44))}</g>
<circle cx="250" cy="300" r="230" fill="url(#sun)"/>
<circle cx="250" cy="300" r="54" fill="#fff6d8" opacity=".9"/>
<!-- far clouds -->
{cloud(70, 270, .7, "#ffd8e8", "#c8a0d8", .8)}{cloud(450, 250, .8, "#ffd8e8", "#c8a0d8", .8)}
<!-- tower -->
<g filter="url(#sh)">{tower}</g>
<!-- landing flash at the top -->
<ellipse cx="{x + w / 2 + 20}" cy="{top_y - 6}" rx="120" ry="30" fill="url(#flash)" opacity=".95"/>
<g stroke="#fff6c0" stroke-width="5" stroke-linecap="round" opacity=".9">
  <path d="M{x - 30} {top_y - 10} l-26 -6 M{x - 24} {top_y - 26} l-22 -16 M{x + w + 50} {top_y - 12} l28 -8 M{x + w + 40} {top_y - 30} l22 -18"/>
</g>
<!-- falling block with face -->
<g transform="translate(0 -22) rotate(-4 256 {top_y - 70})" filter="url(#sh2)">{block(x - 6, top_y - 96, w + 10, 54, 330, face=True, gid="fallb")}</g>
<g stroke="url(#streak)" stroke-width="6" stroke-linecap="round" opacity=".85" transform="rotate(-4 256 {top_y - 70})">
  <path d="M{x + 10} {top_y - 196} V{top_y - 132} M{x + 60} {top_y - 214} V{top_y - 130} M{x + 110} {top_y - 200} V{top_y - 132} M{x + 150} {top_y - 186} V{top_y - 134}"/>
</g>
<!-- falling off-cut piece -->
<g transform="translate(372 {top_y + 40}) rotate(24)" filter="url(#sh2)">{block(0, 0, 40, 46, 18, 14, wins=False, gid="cutb")}</g>
<!-- cloud sea in front -->
{cloud(60, 486, 1.0)}{cloud(256, 500, 1.15)}{cloud(470, 486, 1.0)}
<g fill="#fff" opacity=".9">{cloud(150, 520, .8, "#ffffff", "#e8dcff")}{cloud(380, 525, .85, "#ffffff", "#e8dcff")}</g>
<!-- birds -->
<g stroke="#3a2a6a" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".75">
  <path d="M54 150 q12 -12 24 0 q12 -12 24 0"/><path d="M418 140 q9 -9 18 0 q9 -9 18 0"/><path d="M440 186 q7 -7 14 0 q7 -7 14 0"/>
</g>
{sparkle(x + w + 70, top_y - 40, .9, "#fff6c0")}{sparkle(x - 40, top_y + 30, .6)}{sparkle(440, 380, .5)}{sparkle(70, 360, .45)}
'''
    return icon(defs, art)
