"""Fallback icon for games without their own — a glossy gamepad."""
from .common import icon, lg, rg, rays, sparkle

def build():
    defs = (
        rg("bg", (0, "#8aa8ff"), (.55, "#4a3ae0"), (1, "#1e1080"), cy=.3, r=.95)
        + lg("pad", (0, "#ffffff"), (.6, "#e2e6f6"), (1, "#a8b0d0"))
        + lg("dpad", (0, "#3a3a5a"), (1, "#16162a"))
        + rg("btnA", (0, "#ffb0c4"), (1, "#e0285a"), cx=.35, cy=.3)
        + rg("btnB", (0, "#fff0a0"), (1, "#e8a000"), cx=.35, cy=.3)
    )
    O = 'stroke="#1a1050" stroke-width="7" stroke-linejoin="round"'
    art = f'''
<rect width="512" height="512" fill="url(#bg)"/>
{rays("#ffffff", .09, 20, 256, 256)}
<ellipse cx="256" cy="404" rx="170" ry="24" fill="#0a0640" opacity=".5" filter="url(#b14)"/>
<g filter="url(#sh)">
  <path d="M96 214 Q96 160 160 160 L352 160 Q416 160 416 214 L446 350 Q458 410 400 410 Q362 410 340 362 L172 362 Q150 410 112 410 Q54 410 66 350 Z" fill="url(#pad)" {O}/>
</g>
<path d="M120 190 Q150 176 200 176" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".9"/>
<path d="M160 226 V306 M120 266 H200" stroke="url(#dpad)" stroke-width="30" stroke-linecap="round"/>
<circle cx="340" cy="238" r="22" fill="url(#btnA)" stroke="#1a1050" stroke-width="5"/>
<circle cx="384" cy="282" r="22" fill="url(#btnB)" stroke="#1a1050" stroke-width="5"/>
<circle cx="332" cy="230" r="6" fill="#fff" opacity=".8"/><circle cx="376" cy="274" r="6" fill="#fff" opacity=".8"/>
<rect x="232" y="246" width="48" height="14" rx="7" fill="#9aa2c4"/>
{sparkle(430, 110, .9)}{sparkle(84, 120, .55)}
'''
    return icon(defs, art)
