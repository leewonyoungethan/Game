"""행성 합치기 — cute planets piled in a glass jar, two of them merging in a burst of light."""
from .common import icon, lg, rg, stars, sparkle

def face(cx, cy, r, mouth="smile"):
    e, ex, ey = r * .11, r * .3, cy + r * .02
    m = (f'<path d="M{cx - e*.9:.1f} {ey + e*1.6:.1f} Q{cx:.1f} {ey + e*2.6:.1f} {cx + e*.9:.1f} {ey + e*1.6:.1f}" stroke="#1a1030" stroke-width="{max(2, r*.05):.1f}" fill="none" stroke-linecap="round"/>'
         if mouth == "smile" else
         f'<ellipse cx="{cx:.1f}" cy="{ey + e*2:.1f}" rx="{e*.7:.1f}" ry="{e*.9:.1f}" fill="#1a1030"/>')
    return (f'<ellipse cx="{cx-ex:.1f}" cy="{ey:.1f}" rx="{e:.1f}" ry="{e*1.25:.1f}" fill="#1a1030"/><ellipse cx="{cx+ex:.1f}" cy="{ey:.1f}" rx="{e:.1f}" ry="{e*1.25:.1f}" fill="#1a1030"/>'
            f'<circle cx="{cx-ex+e*.35:.1f}" cy="{ey-e*.45:.1f}" r="{e*.38:.1f}" fill="#fff"/><circle cx="{cx+ex+e*.35:.1f}" cy="{ey-e*.45:.1f}" r="{e*.38:.1f}" fill="#fff"/>'
            f'<ellipse cx="{cx-ex-e*.8:.1f}" cy="{ey+e*2.1:.1f}" rx="{e*1.1:.1f}" ry="{e*.6:.1f}" fill="#ff5a8c" opacity=".4"/><ellipse cx="{cx+ex+e*.8:.1f}" cy="{ey+e*2.1:.1f}" rx="{e*1.1:.1f}" ry="{e*.6:.1f}" fill="#ff5a8c" opacity=".4"/>'
            + m)

def planet(pid, cx, cy, r, extra="", mouth="smile"):
    return (f'<g filter="url(#sh2)"><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{pid})" stroke="#0a0820" stroke-opacity=".5" stroke-width="{max(2, r*.05):.1f}"/></g>'
            f'<g clip-path="url(#c{pid})">{extra}<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#term)"/></g>'
            f'<ellipse cx="{cx - r*.38:.1f}" cy="{cy - r*.45:.1f}" rx="{r*.3:.1f}" ry="{r*.17:.1f}" fill="#fff" opacity=".4" transform="rotate(-35 {cx - r*.38:.1f} {cy - r*.45:.1f})"/>'
            + face(cx, cy, r, mouth))

def build():
    P = {  # id: (cx, cy, r)
        "earth": (176, 380, 70), "jup": (330, 372, 82), "moon": (88, 424, 34),
        "mars": (250, 286, 42), "venus": (130, 290, 40), "ast": (420, 268, 24),
        "nep": (390, 224, 36),
    }
    clips = "".join(f'<clipPath id="c{k}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath>' for k, (x, y, r) in P.items())
    defs = (
        rg("sky", (0, "#3a1e8a"), (.55, "#160c48"), (1, "#070418"), cx=.7, cy=.15, r=1)
        + rg("neb", (0, "#ff4fa3", .45), (1, "#ff4fa3", 0))
        + rg("neb2", (0, "#8b5cff", .5), (1, "#8b5cff", 0))
        + rg("earth", (0, "#bfe8ff"), (.5, "#2a7ae0"), (1, "#0c2a7a"), cx=.35, cy=.3)
        + rg("jup", (0, "#fff0d8"), (.55, "#e8a060"), (1, "#8a4418"), cx=.35, cy=.3)
        + rg("moon", (0, "#ffffff"), (.6, "#d4d8e2"), (1, "#7e8698"), cx=.35, cy=.3)
        + rg("mars", (0, "#ffc0a0"), (.55, "#e0582a"), (1, "#7a2208"), cx=.35, cy=.3)
        + rg("venus", (0, "#fff8d8"), (.55, "#f0c060"), (1, "#a06a1a"), cx=.35, cy=.3)
        + rg("ast", (0, "#e8e2d8"), (.6, "#8a8076"), (1, "#4a423a"), cx=.35, cy=.3)
        + rg("nep", (0, "#c0d8ff"), (.55, "#2f5ae0"), (1, "#101e6a"), cx=.35, cy=.3)
        + rg("term", (0, "#000", 0), (.65, "#000", 0), (1, "#05061e", .55), cx=.38, cy=.36, r=.75)
        + lg("glass", (0, "#ffffff", .22), (.1, "#ffffff", .04), (.9, "#ffffff", .02), (1, "#ffffff", .16), x1=0, y1=0, x2=1, y2=0)
        + rg("burst", (0, "#ffffff"), (.2, "#fff6c0", .95), (.5, "#ffb83a", .45), (1, "#ff8a1a", 0))
        + clips
    )
    ex, ey, er = P["earth"]; jx, jy, jr = P["jup"]; mx, my, mr = P["mars"]
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<circle cx="420" cy="80" r="220" fill="url(#neb)"/><circle cx="60" cy="470" r="220" fill="url(#neb2)"/>
{stars(41, 70, (0, 0, 512, 512), .5, 2)}
<!-- jar -->
<path d="M46 110 Q46 92 64 92 L448 92 Q466 92 466 110 L466 452 Q466 486 432 486 L80 486 Q46 486 46 452 Z" fill="#ffffff" fill-opacity=".06" stroke="#d8d0ff" stroke-opacity=".55" stroke-width="6"/>
<path d="M60 168 H452" stroke="#ff5a78" stroke-width="5" stroke-dasharray="16 12" opacity=".8"/>
<!-- planets -->
{planet("moon", *P["moon"], ''.join(f'<circle cx="{88+dx}" cy="{424+dy}" r="{r}" fill="#000" opacity=".14"/>' for dx, dy, r in [(-10, -8, 7), (12, 6, 5), (-4, 14, 4)]))}
{planet("earth", ex, ey, er, f'<ellipse cx="{ex-24}" cy="{ey-14}" rx="27" ry="20" fill="#4fc46a"/><ellipse cx="{ex+26}" cy="{ey+18}" rx="21" ry="29" fill="#4fc46a"/><ellipse cx="{ex+6}" cy="{ey-40}" rx="16" ry="9" fill="#4fc46a"/><path d="M{ex-50} {ey-34} q20 -8 40 0 M{ex-6} {ey+6} q24 -8 48 0" stroke="#fff" stroke-width="7" stroke-linecap="round" fill="none" opacity=".75"/>')}
{planet("jup", jx, jy, jr, ''.join(f'<ellipse cx="{jx}" cy="{jy - jr + (i + .6) * (2*jr/5.4):.0f}" rx="{jr*1.2:.0f}" ry="{jr*.12:.0f}" fill="{c}"/>' for i, c in enumerate(["#a0501e80", "#fff0dc70", "#8c3c1466", "#ffe6c860", "#aa5a2870"])) + f'<ellipse cx="{jx+28}" cy="{jy+26}" rx="18" ry="11" fill="#c0402a"/>')}
{planet("venus", *P["venus"], ''.join(f'<ellipse cx="130" cy="{290 + i*13}" rx="46" ry="6" fill="#fff" opacity=".3"/>' for i in (-2, -1, 0, 1, 2)))}
{planet("nep", *P["nep"], '<ellipse cx="380" cy="234" rx="9" ry="5" fill="#0a1450" opacity=".6"/>')}
<!-- merging pair: asteroid flying into mars -> burst -->
<circle cx="{mx+30}" cy="{my-30}" r="80" fill="url(#burst)"/>
{planet("mars", mx, my, mr, f'<ellipse cx="{mx}" cy="{my-mr*.9:.0f}" rx="{mr*.45:.0f}" ry="{mr*.15:.0f}" fill="#fff" opacity=".85"/><ellipse cx="{mx-12}" cy="{my+8}" rx="14" ry="6" fill="#7a1e08" opacity=".4"/>', "o")}
{planet("ast", *P["ast"], '<circle cx="414" cy="262" r="5" fill="#000" opacity=".2"/><circle cx="428" cy="276" r="4" fill="#000" opacity=".2"/>', "o")}
<g stroke="#fffbe0" stroke-width="5" stroke-linecap="round">
  <path d="M{mx+30} {my-30} l26 -40"/><path d="M{mx+30} {my-30} l46 -6"/><path d="M{mx+30} {my-30} l-6 -46"/><path d="M{mx+30} {my-30} l-36 -24"/>
</g>
<path d="M60 110 Q56 260 64 440" stroke="#fff" stroke-width="10" fill="none" opacity=".35" stroke-linecap="round"/>
<rect x="46" y="92" width="420" height="394" rx="30" fill="url(#glass)"/>
<!-- drop guide + next planet -->
<path d="M256 108 V160" stroke="#fff" stroke-width="3" opacity=".4" stroke-dasharray="6 6"/>
<!-- plus sign merging hint -->
{sparkle(mx+30, my-30, 1.1, "#fffbe0")}{sparkle(440, 140, .6)}{sparkle(90, 140, .5)}{sparkle(470, 460, .45, "#ffe0f0")}
'''
    return icon(defs, art)
