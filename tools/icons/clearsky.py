"""맑은 하늘 — a calm air-traffic radar scope under a clear morning sky (memorial tone)."""
import math
from .common import icon, lg, rg

def build():
    cx, cy, R = 256, 270, 176
    ticks = []
    for i in range(72):
        a = math.radians(i * 5)
        r0 = R + 8; r1 = R + (22 if i % 6 == 0 else 14)
        ticks.append(f'<path d="M{cx + r0*math.cos(a):.1f} {cy + r0*math.sin(a):.1f} L{cx + r1*math.cos(a):.1f} {cy + r1*math.sin(a):.1f}" stroke="#2a3a54" stroke-width="{3 if i % 6 == 0 else 1.6}"/>')
    # sweep wedge (trailing fade made of slices)
    sweep = []
    ang0 = -50
    for k in range(24):
        a1 = math.radians(ang0 - k * 3.4); a2 = math.radians(ang0 - (k + 1) * 3.4 - .4)
        op = .85 * (1 - k / 24) ** 1.8
        sweep.append(f'<path d="M{cx} {cy} L{cx + R*math.cos(a1):.1f} {cy + R*math.sin(a1):.1f} A{R} {R} 0 0 0 {cx + R*math.cos(a2):.1f} {cy + R*math.sin(a2):.1f} Z" fill="#9fe0ff" opacity="{op:.3f}"/>')
    la = math.radians(ang0)
    blips = [(-96, -64, "#9fd0f5"), (102, 58, "#9fd0f5"), (-70, 96, "#9fd0f5"), (40, -22, "#63c98f")]
    B = []
    for dx, dy, c in blips:
        B.append(f'<rect x="{cx+dx-6}" y="{cy+dy-6}" width="12" height="12" rx="2" fill="{c}"/>'
                 f'<path d="M{cx+dx} {cy+dy} l{18 if dx < 0 else -16} {-10 if dy < 0 else 10}" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
                 f'<g fill="{c}" opacity=".45">{"".join(f"<rect x=\"{cx+dx-2-(k+1)*8*(1 if dx>0 else -1):.0f}\" y=\"{cy+dy-2:.0f}\" width=\"4\" height=\"4\"/>" for k in range(3))}</g>')
    art = f'''
<rect width="512" height="512" fill="url(#sky)"/>
<g fill="#fff" filter="url(#b6)" opacity=".9"><ellipse cx="90" cy="78" rx="80" ry="18"/><ellipse cx="420" cy="54" rx="64" ry="14"/><ellipse cx="470" cy="112" rx="40" ry="10"/></g>
<ellipse cx="{cx}" cy="{cy+20}" rx="{R+40}" ry="{R+30}" fill="#0a1a2a" opacity=".45" filter="url(#b30)"/>
<g filter="url(#sh)">
  <circle cx="{cx}" cy="{cy}" r="{R+34}" fill="url(#bezel)" stroke="#1a2436" stroke-width="5"/>
</g>
<circle cx="{cx}" cy="{cy}" r="{R+26}" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="3"/>
{''.join(ticks)}
<circle cx="{cx}" cy="{cy}" r="{R+4}" fill="#0a1220" stroke="#0a1220" stroke-width="6"/>
<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#scope)"/>
<g stroke="#9fd0f5" fill="none" opacity=".25" stroke-width="2.5">
  <circle cx="{cx}" cy="{cy}" r="{R*.75:.0f}"/><circle cx="{cx}" cy="{cy}" r="{R*.5:.0f}"/><circle cx="{cx}" cy="{cy}" r="{R*.25:.0f}"/>
  <path d="M{cx} {cy-R} V{cy+R} M{cx-R} {cy} H{cx+R}"/>
  <path d="M{cx-R*.707:.0f} {cy-R*.707:.0f} L{cx+R*.707:.0f} {cy+R*.707:.0f} M{cx-R*.707:.0f} {cy+R*.707:.0f} L{cx+R*.707:.0f} {cy-R*.707:.0f}" opacity=".5"/>
</g>
{''.join(sweep)}
<path d="M{cx} {cy} L{cx + R*math.cos(la):.1f} {cy + R*math.sin(la):.1f}" stroke="#dff4ff" stroke-width="5" stroke-linecap="round" filter="url(#glowS)"/>
{''.join(B)}
<circle cx="{cx+92}" cy="{cy-78}" r="40" fill="url(#amberGlow)"/>
<circle cx="{cx+92}" cy="{cy-78}" r="24" fill="none" stroke="#f0b54a" stroke-width="6"/>
<rect x="{cx+85}" y="{cy-85}" width="14" height="14" rx="2" fill="#f0b54a"/>
<circle cx="{cx}" cy="{cy}" r="9" fill="#e6eef7"/>
<path d="M{cx-R*.8:.0f} {cy-R*.62:.0f} Q{cx-R*.3:.0f} {cy-R*1.02:.0f} {cx+R*.4:.0f} {cy-R*.9:.0f}" stroke="#fff" stroke-width="10" fill="none" opacity=".18" stroke-linecap="round"/>
<g fill="#5a6a84" stroke="#1a2436" stroke-width="2">{''.join(f'<circle cx="{cx + (R+28)*math.cos(math.radians(a)):.1f}" cy="{cy + (R+28)*math.sin(math.radians(a)):.1f}" r="5"/>' for a in (45, 135, 225, 315))}</g>
'''
    defs = (
        lg("sky", (0, "#7cc0f0"), (.6, "#bfe2fa"), (1, "#eaf6ff"))
        + lg("bezel", (0, "#f2f6fb"), (.45, "#c4cedc"), (1, "#6e7c92"), x1=0, y1=0, x2=1, y2=1)
        + rg("scope", (0, "#17405e"), (.7, "#0d2438"), (1, "#06121e"))
        + rg("amberGlow", (0, "#f0b54a", .7), (1, "#f0b54a", 0))
    )
    return icon(defs, art)
