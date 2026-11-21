"""Generate the clickbait-style thumbnails in thumbnails/ from the base art in thumbnails/base/.

Run: python3 tools/make_thumbs.py
"""
import math, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE, OUT = ROOT / "thumbnails/base", ROOT / "thumbnails"

# text: (line1, line2), pos: 'top' | 'bottom'; circle: (cx, cy, r); arrow: from point -> circle; emoji: (x, y)
GAMES = {
    "rock":        dict(badge="역대급", text=("산 하나를", "통째로 팜ㅋㅋ"), pos="bottom", circle=(470, 160, 62), arrow=(600, 30), emoji=("⛏️", 585, 225)),
    "eggsteal":    dict(badge="충격", text=("닭 몰래", "알 훔치기 성공?"), pos="top", circle=(284, 288, 42), arrow=(390, 205), emoji=("😱", 585, 330)),
    "road":        dict(badge="실화", text=("시속 4000km", "실화냐?"), pos="top", circle=(238, 312, 50), arrow=(110, 205), emoji=("🔥", 590, 330)),
    "rail-dash":   dict(badge="레전드", text=("3분 버티면", "인정해줌"), pos="top", circle=(442, 190, 56), arrow=(590, 268), emoji=("😤", 70, 320)),
    "getaway":     dict(badge="역대급", text=("경찰 9대", "다 따돌림ㅋㅋ"), pos="top", circle=(112, 196, 72), arrow=(300, 300), emoji=("🚨", 590, 250)),
    "piano-tiles": dict(badge="고인물 전용", text=("255곡", "전부 깰 수 있음?"), pos="top", circle=(200, 305, 50), arrow=(70, 200), emoji=("🤯", 585, 320)),
    "nayul":       dict(badge="감동 주의", text=("아기를", "100살까지 키움"), pos="bottom", circle=(320, 92, 52), arrow=(480, 22), emoji=("🥹", 95, 150)),
}

def inner(svg):
    svg = re.sub(r"^\s*<svg[^>]*>", "", svg.strip())
    return re.sub(r"</svg>\s*$", "", svg)

def font_size(s):
    n = len(s)
    return 72 if n <= 6 else 62 if n <= 8 else 54

def text_line(s, x, y, fill):
    fs = font_size(s)
    style = ('font-family="Black Han Sans, Jalnan, Pretendard, Apple SD Gothic Neo, Malgun Gothic, sans-serif" '
             f'font-weight="900" font-size="{fs}" letter-spacing="-1"')
    return (f'<text x="{x}" y="{y}" {style} fill="none" stroke="#000" stroke-width="16" stroke-linejoin="round">{s}</text>'
            f'<text x="{x}" y="{y}" {style} fill="{fill}">{s}</text>')

def arrow(fx, fy, cx, cy, r):
    ang = math.atan2(cy - fy, cx - fx)
    tx, ty = cx - math.cos(ang) * (r + 10), cy - math.sin(ang) * (r + 10)
    L = math.hypot(tx - fx, ty - fy)
    deg = math.degrees(ang)
    shaft = f'M0 -9 L{L-34:.0f} -9 L{L-34:.0f} -26 L{L:.0f} 0 L{L-34:.0f} 26 L{L-34:.0f} 9 L0 9 Z'
    return (f'<g transform="translate({fx} {fy}) rotate({deg:.1f})">'
            f'<path d="{shaft}" fill="#fff" stroke="#fff" stroke-width="10" stroke-linejoin="round"/>'
            f'<path d="{shaft}" fill="#ff1e1e"/></g>')

def build(gid, g):
    art = inner((BASE / f"{gid}.svg").read_text())
    cx, cy, r = g["circle"]
    l1, l2 = g["text"]
    if g["pos"] == "top":
        y1, y2, shade = 72, 146, '<rect width="640" height="175" fill="url(#tshade)"/>'
    else:
        y1, y2, shade = 262, 334, '<rect y="185" width="640" height="175" fill="url(#bshade)"/>'
    bw = 26 + 22 * len(g["badge"])
    ex, ey = g["emoji"][1], g["emoji"][2]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
  <defs>
    <filter id="pop" x="0" y="0" width="1" height="1"><feColorMatrix type="saturate" values="1.55"/>
      <feComponentTransfer><feFuncR type="linear" slope="1.12" intercept="-.03"/><feFuncG type="linear" slope="1.12" intercept="-.03"/><feFuncB type="linear" slope="1.12" intercept="-.03"/></feComponentTransfer></filter>
    <radialGradient id="vig" cx="50%" cy="50%" r="75%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".6"/></radialGradient>
    <linearGradient id="tshade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".55"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>
    <linearGradient id="bshade" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".6"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>
    <radialGradient id="flare"><stop offset="0" stop-color="#fff6a0" stop-opacity=".75"/><stop offset="1" stop-color="#fff6a0" stop-opacity="0"/></radialGradient>
  </defs>
  <g filter="url(#pop)"><g transform="translate(320 180) scale(1.04) translate(-320 -180)">{art}</g></g>
  <circle cx="{cx}" cy="{cy}" r="{r*1.7:.0f}" fill="url(#flare)"/>
  <rect width="640" height="360" fill="url(#vig)"/>
  {shade}
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#fff" stroke-width="16"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#ff1e1e" stroke-width="9"/>
  {arrow(*g["arrow"], cx, cy, r)}
  <text x="{ex}" y="{ey}" font-size="84" text-anchor="middle" dominant-baseline="central">{g["emoji"][0]}</text>
  {text_line(l1, 22, y1, "#ffffff")}
  {text_line(l2, 22, y2, "#ffe14d")}
  <g transform="translate({640 - bw - 14} 14) rotate(4 {bw/2} 20)">
    <rect width="{bw}" height="42" rx="8" fill="#ff1e1e" stroke="#fff" stroke-width="4"/>
    <text x="{bw/2}" y="30" text-anchor="middle" font-family="Black Han Sans, Apple SD Gothic Neo, Malgun Gothic, sans-serif" font-weight="900" font-size="24" fill="#fff">{g["badge"]}</text>
  </g>
  <rect x="3" y="3" width="634" height="354" fill="none" stroke="#ffe14d" stroke-width="6"/>
</svg>
'''

for gid, g in GAMES.items():
    (OUT / f"{gid}.svg").write_text(build(gid, g))
    print("wrote", gid)
