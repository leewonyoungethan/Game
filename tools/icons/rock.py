"""곡괭이 봉우리 — floating voxel mountain with glowing ores and a striking pickaxe."""
import random
from .common import icon, lg, rg, rays, sparkle

S = 46                 # cube edge
OX, OY = 228, 200      # screen position of grid cell (0,0) top-centre at k=0
H = [                  # column heights (i = right-down, j = left-down)
    [1, 2, 2, 1],
    [2, 3, 4, 2],
    [2, 4, 5, 3],
    [1, 2, 3, 2],
]
SNOW = 5

def P(i, j, k):
    return OX + (i - j) * S * .866, OY + (i + j) * S * .5 - k * S

def poly(pts, fill, extra=""):
    return f'<path d="M{" L".join(f"{x:.1f} {y:.1f}" for x, y in pts)} Z" fill="{fill}"{extra}/>'

def face_pt(o, u, v, a, b):
    return o[0] + u[0] * a + v[0] * b, o[1] + u[1] * a + v[1] * b

def cube(i, j, k, top_layer, rnd):
    x, y = P(i, j, k)
    h, w = S * .5, S * .866
    T = [(x, y - h), (x + w, y), (x, y + h), (x - w, y)]
    L = [(x - w, y), (x, y + h), (x, y + h + S), (x - w, y + S)]
    R = [(x, y + h), (x + w, y), (x + w, y + S), (x, y + h + S)]
    snow = k + 1 >= SNOW and top_layer
    out = []
    if top_layer:
        out.append(poly(T, "url(#snowTop)" if snow else "url(#grassTop)"))
        out.append(poly(L, "url(#stoneL)")); out.append(poly(R, "url(#stoneR)"))
        # grass / snow overhang with drips
        cap = "url(#snowSide)" if snow else "url(#grassSide)"
        dl = [(x - w, y), (x, y + h)]
        drip = [(x, y + h + 12), (x - w * .25, y + h * .75 + 7), (x - w * .4, y + h * .6 + 16), (x - w * .6, y + h * .4 + 6), (x - w * .8, y + h * .2 + 12), (x - w, y + 9)]
        out.append(poly(dl + drip, cap))
        dr = [(x, y + h), (x + w, y)]
        drip = [(x + w, y + 10), (x + w * .75, y + h * .25 + 6), (x + w * .55, y + h * .45 + 15), (x + w * .3, y + h * .7 + 7), (x, y + h + 12)]
        out.append(poly(dr + drip, cap, ' opacity=".9"'))
        if not snow:
            for _ in range(3):
                a, b = rnd.uniform(.2, .8), rnd.uniform(.2, .8)
                px, py = face_pt(T[3], (T[0][0] - T[3][0], T[0][1] - T[3][1]), (T[2][0] - T[3][0], T[2][1] - T[3][1]), a, b)
                out.append(f'<path d="M{px:.1f} {py:.1f} l-2 -7 M{px+3:.1f} {py:.1f} l1 -8 M{px+6:.1f} {py:.1f} l3 -6" stroke="#2f8a22" stroke-width="2" stroke-linecap="round"/>')
    else:
        out.append(poly(L, "url(#stoneL)")); out.append(poly(R, "url(#stoneR)"))
    # edge light
    out.append(f'<path d="M{L[0][0]:.1f} {L[0][1]:.1f} L{L[1][0]:.1f} {L[1][1]:.1f} L{R[1][0]:.1f} {R[1][1]:.1f}" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="2"/>')
    out.append(f'<path d="M{L[1][0]:.1f} {L[1][1]:.1f} V{L[2][1]:.1f}" stroke="#000" stroke-opacity=".18" stroke-width="2"/>')
    # stone cracks / ores on side faces
    for face, ou in ((L, "L"), (R, "R")):
        o, u, v = face[0], (face[1][0] - face[0][0], face[1][1] - face[0][1]), (face[3][0] - face[0][0], face[3][1] - face[0][1])
        r = rnd.random()
        if r < .55 and not top_layer or r < .25:
            kind = rnd.choice(["dia", "gold", "gold", "ruby", "dia"])
            for _ in range(rnd.randint(1, 2)):
                a, b = rnd.uniform(.15, .6), rnd.uniform(.25, .62)
                q = [face_pt(o, u, v, a, b), face_pt(o, u, v, a + .24, b), face_pt(o, u, v, a + .24, b + .28), face_pt(o, u, v, a, b + .28)]
                cx, cy = sum(p[0] for p in q) / 4, sum(p[1] for p in q) / 4
                out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="22" fill="url(#{kind}Glow)"/>')
                out.append(poly(q, f"url(#{kind})", ' stroke="#1a1030" stroke-opacity=".6" stroke-width="1.5"'))
                out.append(f'<circle cx="{q[0][0]+2:.1f}" cy="{q[0][1]+3:.1f}" r="1.6" fill="#fff"/>')
        else:
            a, b = rnd.uniform(.25, .6), rnd.uniform(.3, .6)
            p0 = face_pt(o, u, v, a, b); p1 = face_pt(o, u, v, a + .18, b + .1); p2 = face_pt(o, u, v, a + .1, b + .28)
            out.append(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} L{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="#2a2d3c" stroke-opacity=".35" stroke-width="2"/>')
    return "".join(out)

def build():
    rnd = random.Random(11)
    cubes = []
    order = sorted(((i, j) for i in range(4) for j in range(4)), key=lambda t: (t[0] + t[1], t[0]))
    for i, j in order:
        for k in range(H[i][j]):
            cubes.append(cube(i, j, k, k == H[i][j] - 1, rnd))
    # island underside
    bx0, by0 = P(0, 3, 0)[0] - S * .866, P(0, 3, 0)[1] + S
    bx1, by1 = P(3, 0, 0)[0] + S * .866, P(3, 0, 0)[1] + S
    bot = P(3, 3, 0)[1] + S * 1.5
    under = (f'<path d="M{bx0:.0f} {by0:.0f} L{P(3,3,0)[0]:.0f} {bot:.0f} L{bx1:.0f} {by1:.0f} '
             f'L{bx1-26:.0f} {by1+50:.0f} L{OX+36:.0f} {bot+70:.0f} L{OX+4:.0f} {bot+104:.0f} L{OX-28:.0f} {bot+66:.0f} L{bx0+30:.0f} {by0+56:.0f} Z" fill="url(#under)"/>'
             f'<path d="M{OX-10:.0f} {bot+20:.0f} q-6 30 6 70 M{OX+30:.0f} {bot+10:.0f} q10 24 0 50 M{OX-60:.0f} {bot-10:.0f} q-10 24 4 46" stroke="#3a2212" stroke-width="4" fill="none" stroke-linecap="round" opacity=".6"/>')
    defs = (
        lg("sky", (0, "#2a7be8"), (.55, "#7cc8ff"), (1, "#d8f4ff"))
        + rg("sun", (0, "#fffbe8"), (.35, "#fff2b0", .9), (1, "#ffe08a", 0))
        + lg("grassTop", (0, "#c4ff86"), (1, "#5fcc3c"), x1=0, y1=0, x2=1, y2=1)
        + lg("grassSide", (0, "#58c43a"), (1, "#2f8f24"))
        + lg("snowTop", (0, "#ffffff"), (1, "#dbe9ff"), x2=1, y2=1)
        + lg("snowSide", (0, "#f4f8ff"), (1, "#bcd0ee"))
        + lg("stoneL", (0, "#a9adbd"), (1, "#7a7f92"))
        + lg("stoneR", (0, "#7e8396"), (1, "#4d5164"))
        + lg("under", (0, "#8a5530"), (.55, "#5a3418"), (1, "#3a200c"))
        + lg("wood", (0, "#f0b070"), (.45, "#b8702e"), (1, "#6a3810"), x1=0, y1=0, x2=1, y2=0)
        + lg("metal", (0, "#ffffff"), (.3, "#e6ecf6"), (.62, "#94a0b8"), (1, "#4e586e"))
        + lg("metalEdge", (0, "#ffffff"), (1, "#b8c4d8"))
        + rg("dia", (0, "#ffffff"), (.45, "#86f6ff"), (1, "#12a0d8"), cx=.35, cy=.3)
        + rg("gold", (0, "#fffbd0"), (.45, "#ffd640"), (1, "#c88000"), cx=.35, cy=.3)
        + rg("ruby", (0, "#ffe4ec"), (.45, "#ff4f78"), (1, "#a00c38"), cx=.35, cy=.3)
        + rg("diaGlow", (0, "#86f6ff", .55), (1, "#86f6ff", 0))
        + rg("goldGlow", (0, "#ffd640", .55), (1, "#ffd640", 0))
        + rg("rubyGlow", (0, "#ff4f78", .5), (1, "#ff4f78", 0))
        + rg("impact", (0, "#ffffff"), (.2, "#fff6c0", .95), (.5, "#ffb83a", .5), (1, "#ff8a1a", 0))
    )
    peak = P(2, 2, SNOW - 1)
    hit = (peak[0] + 44, peak[1] + 60)          # point on the peak's right face
    import math
    a = math.radians(-35); sc = .58
    tx, ty = -176 * sc, -78 * sc                 # pickaxe left tip in local coords
    rx, ry = tx * math.cos(a) - ty * math.sin(a), tx * math.sin(a) + ty * math.cos(a)
    PX, PY = hit[0] - rx, hit[1] - ry
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
{rays("#ffffff", .08, 22, 96, 80)}
<circle cx="96" cy="80" r="110" fill="url(#sun)"/>
<g fill="#fff" filter="url(#b6)" opacity=".95">
  <ellipse cx="420" cy="118" rx="78" ry="22"/><ellipse cx="452" cy="100" rx="44" ry="24"/>
  <ellipse cx="52" cy="300" rx="80" ry="20"/><ellipse cx="460" cy="380" rx="70" ry="18"/>
</g>
<g fill="#fff" opacity=".6" filter="url(#b2)"><ellipse cx="300" cy="66" rx="40" ry="10"/></g>
<ellipse cx="{OX}" cy="{P(3,3,0)[1]+190:.0f}" rx="130" ry="22" fill="#1a3a80" opacity=".35" filter="url(#b14)"/>
{under}
<g filter="url(#sh)">{''.join(cubes)}</g>

<circle cx="{hit[0]:.0f}" cy="{hit[1]:.0f}" r="62" fill="url(#impact)"/>
<g stroke="#fffbe0" stroke-width="5" stroke-linecap="round">
  <path d="M{hit[0]+14:.0f} {hit[1]-10:.0f} l34 -26"/><path d="M{hit[0]+18:.0f} {hit[1]+2:.0f} l40 4"/><path d="M{hit[0]+10:.0f} {hit[1]+14:.0f} l22 28"/><path d="M{hit[0]:.0f} {hit[1]-18:.0f} l-2 -36"/>
</g>
<g fill="#8b90a2" stroke="#2a2d3c" stroke-width="2">
  <path d="M{hit[0]+60:.0f} {hit[1]-48:.0f} l12 -6 l6 12 l-12 6 Z"/><path d="M{hit[0]+74:.0f} {hit[1]+18:.0f} l9 -3 l3 9 l-9 3 Z"/><path d="M{hit[0]+40:.0f} {hit[1]+56:.0f} l8 -4 l4 8 l-8 4 Z"/>
</g>
<g transform="translate({PX:.0f} {PY:.0f}) rotate(-35) scale(.58)" filter="url(#sh)">
  <path d="M-10 -158 Q30 -150 34 -120" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".55"/>
  <rect x="-16" y="-112" width="32" height="250" rx="15" fill="url(#wood)" stroke="#3a1c06" stroke-width="5"/>
  <path d="M-6 -60 q5 40 0 80 M6 40 q-4 40 0 80" stroke="#7a4214" stroke-width="3" fill="none" opacity=".55"/>
  <rect x="-18" y="80" width="36" height="14" rx="5" fill="#3a2a1a"/><rect x="-18" y="100" width="36" height="14" rx="5" fill="#3a2a1a"/>
  <rect x="-22" y="-124" width="44" height="34" rx="8" fill="#5e6880" stroke="#1e2234" stroke-width="5"/>
  <path d="M-176 -78 Q-90 -168 0 -160 Q90 -168 176 -78 L162 -60 Q90 -126 0 -120 Q-90 -126 -162 -60 Z" fill="url(#metal)" stroke="#1e2234" stroke-width="6" stroke-linejoin="round"/>
  <path d="M-150 -86 Q-80 -150 0 -146 Q80 -150 150 -86" fill="none" stroke="url(#metalEdge)" stroke-width="5" stroke-linecap="round"/>
  <path d="M-176 -78 L-188 -66 L-162 -60 Z M176 -78 L188 -66 L162 -60 Z" fill="#cfd8e8" stroke="#1e2234" stroke-width="5" stroke-linejoin="round"/>
</g>
{sparkle(60, 190, .7)}{sparkle(450, 220, .9, "#fff6c0")}{sparkle(110, 420, .55)}{sparkle(380, 470, .5, "#bff6ff")}
'''
    return icon(defs, art)
