"""젤리 블록 퍼즐 — a tilted board of glossy jelly cubes; one full row bursts in a flash of light
while a chubby smiling L-shaped jelly piece hovers in, ready to drop."""
from .common import icon, lg, rg, sparkle, star_path

PAL = {"p": ("#ffb0d8", "#ff5aa0", "#c81a6a"), "y": ("#fff0a0", "#ffc83a", "#d88a0a"), "g": ("#c0ffa8", "#5ad86a", "#1a9a4a"),
       "b": ("#bff0ff", "#4ac0ff", "#1a6ad8"), "v": ("#e8d0ff", "#a87aff", "#6a3ad0"), "o": ("#ffd0b0", "#ff8a4a", "#d0501a"), "t": ("#c8fff4", "#3ae0c8", "#0a9a90")}

def cube_defs():
    out = ""
    for k, (hi, mid, lo) in PAL.items():
        out += f'<linearGradient id="j{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{hi}"/><stop offset=".45" stop-color="{mid}"/><stop offset="1" stop-color="{lo}"/></linearGradient>'
    return out

def cube(x, y, s, k, face=False):
    r = s * .28
    out = (f'<rect x="{x}" y="{y + s * .07:.1f}" width="{s}" height="{s}" rx="{r:.1f}" fill="#000" opacity=".22"/>'
           f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{r:.1f}" fill="url(#j{k})"/>'
           f'<rect x="{x + s * .16:.1f}" y="{y + s * .12:.1f}" width="{s * .5:.1f}" height="{s * .16:.1f}" rx="{s * .08:.1f}" fill="#fff" opacity=".7"/>'
           f'<circle cx="{x + s * .78:.1f}" cy="{y + s * .2:.1f}" r="{s * .06:.1f}" fill="#fff" opacity=".6"/>')
    if face:
        cx, cy = x + s / 2, y + s * .56
        out += (f'<ellipse cx="{cx - s * .17:.1f}" cy="{cy - s * .04:.1f}" rx="{s * .07:.1f}" ry="{s * .1:.1f}" fill="#3a0a24"/><ellipse cx="{cx + s * .17:.1f}" cy="{cy - s * .04:.1f}" rx="{s * .07:.1f}" ry="{s * .1:.1f}" fill="#3a0a24"/>'
                f'<circle cx="{cx - s * .15:.1f}" cy="{cy - s * .08:.1f}" r="{s * .03:.1f}" fill="#fff"/><circle cx="{cx + s * .19:.1f}" cy="{cy - s * .08:.1f}" r="{s * .03:.1f}" fill="#fff"/>'
                f'<path d="M{cx - s * .09:.1f} {cy + s * .08:.1f} Q{cx:.1f} {cy + s * .2:.1f} {cx + s * .09:.1f} {cy + s * .08:.1f}" stroke="#3a0a24" stroke-width="{s * .045:.1f}" fill="#ff5a7a" stroke-linecap="round"/>'
                f'<ellipse cx="{cx - s * .3:.1f}" cy="{cy + s * .08:.1f}" rx="{s * .08:.1f}" ry="{s * .05:.1f}" fill="#fff" opacity=".45"/><ellipse cx="{cx + s * .3:.1f}" cy="{cy + s * .08:.1f}" rx="{s * .08:.1f}" ry="{s * .05:.1f}" fill="#fff" opacity=".45"/>')
    return out

def build():
    defs = (rg("bg", (0, "#8a5aff"), (.55, "#4a2aaa"), (1, "#1e0e4a"), cx=.5, cy=.3, r=.85)
            + lg("boardg", (0, "#3a2280"), (1, "#22124e"))
            + lg("beam", (0, "#ffffff", 0), (.5, "#ffffff", .95), (1, "#ffffff", 0), x1=0, y1=0, x2=1, y2=0)
            + rg("burst", (0, "#ffffff"), (.3, "#fff3b0", .8), (1, "#ff8ad8", 0))
            + cube_defs())
    S, G = 46, 6
    layout = ["p.ybg.vo", "pp.bggvo", "yyyyyyyy", ".b.vv.oo", "gbbv.ppo", "gg.vyyp."]
    cells = ""
    for r, row in enumerate(layout):
        for c, k in enumerate(row):
            x, y = c * (S + G), r * (S + G)
            if k == ".":
                cells += f'<rect x="{x}" y="{y}" width="{S}" height="{S}" rx="12" fill="#ffffff" opacity=".07"/>'
            elif r == 2:
                cells += f'<g opacity=".95">{cube(x, y, S, k)}</g><rect x="{x}" y="{y}" width="{S}" height="{S}" rx="12" fill="#fff" opacity=".45"/>'
            else:
                cells += cube(x, y, S, k)
    bw = 8 * (S + G) - G; bh = 6 * (S + G) - G
    P = 70
    outline = "".join(f'<rect x="{x * P - 6}" y="{y * P - 6}" width="{P + 12}" height="{P + 12}" rx="26" fill="#fff"/>' for x, y in [(0, 0), (0, 1), (1, 1)])
    pieces = f'<g opacity=".9">{outline}</g>' + "".join(cube(x * P, y * P, P - 2, "t", face=(x, y) == (0, 1)) for x, y in [(0, 0), (0, 1), (1, 1)])
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
<g fill="#fff">{''.join(f'<path d="{star_path((i * 113) % 512, (i * 71) % 512, 3 + (i % 3) * 2, .4)}" opacity="{.25 + (i % 4) * .12}"/>' for i in range(26))}</g>
<!-- tilted board -->
<g transform="translate(256 300) skewX(-8) rotate(-7) translate({-bw / 2} {-bh / 2 - 40})">
  <rect x="-18" y="-18" width="{bw + 36}" height="{bh + 36}" rx="30" fill="#000" opacity=".3" transform="translate(0 16)"/>
  <rect x="-18" y="-18" width="{bw + 36}" height="{bh + 36}" rx="30" fill="url(#boardg)" stroke="#ffffff" stroke-opacity=".25" stroke-width="4"/>
  {cells}
  <!-- clearing row flash -->
  <rect x="-40" y="{2 * (S + G) - 10}" width="{bw + 80}" height="{S + 20}" fill="url(#beam)" opacity=".9"/>
  <ellipse cx="{bw / 2}" cy="{2 * (S + G) + S / 2}" rx="{bw * .6}" ry="70" fill="url(#burst)" opacity=".8"/>
</g>
<!-- flying jelly bits -->
<g>{''.join(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s * .3}" fill="url(#j{k})" transform="rotate({a} {x + s / 2} {y + s / 2})"/>' for x, y, s, k, a in [(30, 190, 26, "y", 20), (462, 160, 22, "y", -30), (60, 120, 18, "b", 40), (440, 250, 18, "p", 10), (20, 280, 14, "g", -20), (480, 320, 14, "v", 30)])}</g>
<!-- hovering L piece with a face -->
<ellipse cx="380" cy="420" rx="130" ry="110" fill="#3ae0c8" opacity=".35" filter="url(#b30)"/>
<g transform="translate(296 300) rotate(10)" filter="url(#sh)">{pieces}</g>
<g stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"><path d="M310 270 v-40 M360 262 v-30 M410 280 v-36"/></g>
{sparkle(120, 196, 1.0, "#fff6c0")}{sparkle(410, 180, .8)}{sparkle(250, 470, .55)}{sparkle(70, 430, .5, "#ffd0f0")}
'''
    return icon(defs, art)
