"""Shared helpers for the game icons (512x512 SVG app icons)."""
import math, random, re

# ---------------------------------------------------------------- gradients
def _stops(stops):
    out = []
    for st in stops:
        o, c = st[0], st[1]
        a = f' stop-opacity="{st[2]}"' if len(st) > 2 else ""
        out.append(f'<stop offset="{o}" stop-color="{c}"{a}/>')
    return "".join(out)

def lg(id, *stops, x1=0, y1=0, x2=0, y2=1, user=False):
    u = ' gradientUnits="userSpaceOnUse"' if user else ""
    return f'<linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"{u}>{_stops(stops)}</linearGradient>'

def rg(id, *stops, cx=.5, cy=.5, r=.5, fx=None, fy=None, user=False):
    f = f' fx="{fx}" fy="{fy}"' if fx is not None else ""
    u = ' gradientUnits="userSpaceOnUse"' if user else ""
    return f'<radialGradient id="{id}" cx="{cx}" cy="{cy}" r="{r}"{f}{u}>{_stops(stops)}</radialGradient>'

# ---------------------------------------------------------------- shared defs
COMMON = """
<clipPath id="sq"><rect width="512" height="512"/></clipPath>
<filter id="sh" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#000" flood-opacity=".5"/></filter>
<filter id="sh2" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#000" flood-opacity=".4"/></filter>
<filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowS" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="b2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2"/></filter>
<filter id="b6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="b14" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="b30" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="30"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .055 0"/></filter>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".32"/><stop offset=".55" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="vig" cx=".5" cy=".46" r=".78"><stop offset=".62" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".32"/></radialGradient>
<linearGradient id="rim" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".45" stop-color="#fff" stop-opacity=".1"/><stop offset="1" stop-color="#fff" stop-opacity=".25"/></linearGradient>
<radialGradient id="spark"><stop offset="0" stop-color="#fff"/><stop offset=".25" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
"""

def icon(defs, art, gloss=False):
    # Full-bleed square art: the portal rounds the tiles itself (mosaic thumbnails), so no frame/rim here.
    g = '<path d="M0 0 H512 V170 Q256 228 0 170 Z" fill="url(#gloss)"/>' if gloss else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
<defs>{COMMON}{defs}</defs>
<g clip-path="url(#sq)">
{art}
<rect width="512" height="512" filter="url(#grain)"/>
<rect width="512" height="512" fill="url(#vig)"/>
{g}
</g>
</svg>
'''

# ---------------------------------------------------------------- decorations
def sparkle(x, y, s=1.0, color="#fff", glow=True):
    g = f'<circle r="26" fill="url(#spark)" opacity=".75"/>' if glow else ""
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})">{g}'
            f'<path d="M0 -30 Q2.6 -2.6 30 0 Q2.6 2.6 0 30 Q-2.6 2.6 -30 0 Q-2.6 -2.6 0 -30 Z" fill="{color}"/></g>')

def rays(color, op, n=18, cx=256, cy=256, R=760):
    d = []
    for i in range(n):
        a = 2 * math.pi * i / n; b = a + math.pi / n
        d.append(f"M{cx} {cy} L{cx+R*math.cos(a):.0f} {cy+R*math.sin(a):.0f} L{cx+R*math.cos(b):.0f} {cy+R*math.sin(b):.0f} Z")
    return f'<path d="{" ".join(d)}" fill="{color}" opacity="{op}"/>'

def stars(seed, n=30, area=(0, 0, 512, 260), rmin=.7, rmax=2.4, color="#fff"):
    rnd = random.Random(seed)
    return "".join(f'<circle cx="{rnd.uniform(area[0],area[2]):.1f}" cy="{rnd.uniform(area[1],area[3]):.1f}" r="{rnd.uniform(rmin,rmax):.1f}" fill="{color}" opacity="{rnd.uniform(.35,1):.2f}"/>' for _ in range(n))

def bokeh(seed, color, n=10, rmin=6, rmax=26, op=(.08, .3), area=(0, 0, 512, 512)):
    rnd = random.Random(seed); out = []
    for _ in range(n):
        out.append(f'<circle cx="{rnd.uniform(area[0], area[2]):.0f}" cy="{rnd.uniform(area[1], area[3]):.0f}" r="{rnd.uniform(rmin, rmax):.0f}" fill="{color}" opacity="{rnd.uniform(*op):.2f}"/>')
    return "".join(out)

def star_path(cx, cy, r, inner=.45, n=5, rot=-90):
    pts = []
    for i in range(n * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + rr*math.cos(a):.1f} {cy + rr*math.sin(a):.1f}")
    return "M" + " L".join(pts) + " Z"

def heart_path(cx, cy, s):
    return (f"M{cx} {cy+s*.9} C{cx-s*1.3} {cy+s*.05} {cx-s*1.05} {cy-s*.95} {cx} {cy-s*.35} "
            f"C{cx+s*1.05} {cy-s*.95} {cx+s*1.3} {cy+s*.05} {cx} {cy+s*.9} Z")

# ---------------------------------------------------------------- validation
def dedupe(svg):
    def fix(m):
        tag = m.group(0)
        mm = re.match(r"<(\w+)(.*?)(/?)>$", tag, re.S)
        if not mm: return tag
        d = {}
        for k, v in re.findall(r'([\w:-]+)="([^"]*)"', mm.group(2)): d[k] = v
        return "<" + mm.group(1) + "".join(f' {k}="{v}"' for k, v in d.items()) + mm.group(3) + ">"
    return re.sub(r"<\w+\b[^<>]*?/?>", fix, svg)


# ---------------------------------------------------------------- text as outlines
# Icons are shown through <img>, where web fonts never load, so any lettering is converted to
# vector paths. Glyph outlines are cached in glyphs.json (only the characters actually used), so
# building needs the font file only when a new character shows up. Font: Pretendard ExtraBold (OFL),
# looked up at $ICON_FONT or tools/fonts/Pretendard-ExtraBold.otf.
import json as _json, os as _os
_GLYPHS_PATH = _os.path.join(_os.path.dirname(__file__), "glyphs.json")
_glyphs = None

def _load_glyph(ch):
    global _glyphs
    if _glyphs is None:
        _glyphs = _json.load(open(_GLYPHS_PATH)) if _os.path.exists(_GLYPHS_PATH) else {}
    if ch not in _glyphs:
        from fontTools.ttLib import TTFont
        from fontTools.pens.svgPathPen import SVGPathPen
        font_path = _os.environ.get("ICON_FONT") or _os.path.join(_os.path.dirname(__file__), "..", "fonts", "Pretendard-ExtraBold.otf")
        f = TTFont(font_path); gs = f.getGlyphSet(); name = f.getBestCmap()[ord(ch)]
        pen = SVGPathPen(gs); gs[name].draw(pen)
        _glyphs[ch] = {"d": pen.getCommands(), "adv": gs[name].width, "upm": f["head"].unitsPerEm}
        _json.dump(_glyphs, open(_GLYPHS_PATH, "w"), ensure_ascii=False, sort_keys=True, indent=0)
    return _glyphs[ch]

def text_path(text, x, y, size, fill="#000", anchor="middle", extra=""):
    """Outlined text. (x, y) is the baseline point; anchor is start|middle|end."""
    gl = [_load_glyph(c) for c in text]
    k = size / gl[0]["upm"]
    width = sum(g["adv"] for g in gl) * k
    cx = x - (width / 2 if anchor == "middle" else width if anchor == "end" else 0)
    out = []
    for g in gl:
        if g["d"]:
            out.append(f'<path transform="translate({cx:.1f} {y:.1f}) scale({k:.4f} {-k:.4f})" d="{g["d"]}"/>')
        cx += g["adv"] * k
    return f'<g fill="{fill}" {extra}>' + "".join(out) + "</g>"
