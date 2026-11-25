"""NOT-GAMBLING · 카지노 시뮬레이터 — a play-money table: a spinning roulette wheel, a fan of cards,
stacks of colorful chips and a pair of dice on green felt under a warm lamp."""
import math
from .common import icon, lg, rg, sparkle

def spade(x, y, s, fill):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{fill}"><path d="M0 -20 C-6 -10 -20 -4 -20 6 C-20 14 -12 18 -4 13 L-8 22 H8 L4 13 C12 18 20 14 20 6 C20 -4 6 -10 0 -20 Z"/></g>')

def heart(x, y, s, fill):
    return f'<g transform="translate({x} {y}) scale({s})" fill="{fill}"><path d="M0 18 C-26 2 -20 -18 -8 -18 C-3 -18 0 -14 0 -10 C0 -14 3 -18 8 -18 C20 -18 26 2 0 18 Z"/></g>'

def card(rot, x, y, suit):
    sym = spade(0, 0, 1.6, "#1a1a2a") if suit == "s" else heart(0, 0, 1.6, "#e8304a")
    corner = spade(-34, -52, .5, "#1a1a2a") if suit == "s" else heart(-34, -52, .5, "#e8304a")
    return (f'<g transform="translate({x} {y}) rotate({rot})" filter="url(#sh2)">'
            f'<rect x="-50" y="-74" width="100" height="148" rx="12" fill="#fffdf6" stroke="#c8c0b0" stroke-width="3"/>'
            f'<rect x="-42" y="-66" width="84" height="132" rx="8" fill="none" stroke="#e8e0d0" stroke-width="2"/>{corner}{sym}</g>')

def chip(x, y, col, n=1):
    out = ""
    for i in range(n):
        yy = y - i * 9
        out += (f'<ellipse cx="{x}" cy="{yy + 4}" rx="34" ry="13" fill="#000" opacity=".25"/>'
                f'<ellipse cx="{x}" cy="{yy}" rx="34" ry="13" fill="{col}" stroke="#fff" stroke-width="3" stroke-dasharray="10 8"/>')
    yy = y - (n - 1) * 9
    out += f'<ellipse cx="{x}" cy="{yy - 1}" rx="20" ry="7" fill="none" stroke="#fff" stroke-width="2.5" opacity=".8"/>'
    return out

def build():
    defs = (rg("felt", (0, "#2aa86a"), (.6, "#0e6a3e"), (1, "#053a20"), cx=.5, cy=.4, r=.8)
            + rg("lamp", (0, "#fff6d0", .45), (1, "#fff6d0", 0))
            + rg("wood", (0, "#c8844a"), (1, "#6a3a1a"))
            + rg("hub", (0, "#fff3b0"), (.6, "#e8b030"), (1, "#a8700a"), cx=.38, cy=.32)
            + rg("ball", (0, "#ffffff"), (1, "#c8c8d0"), cx=.35, cy=.3))
    # roulette wheel
    R, segs = 118, 18
    wedges = ""
    for i in range(segs):
        a0, a1 = i / segs * math.tau, (i + 1) / segs * math.tau
        col = "#1a9a4a" if i == 0 else ("#d8203a" if i % 2 else "#1a1a24")
        wedges += f'<path d="M0 0 L{R * math.cos(a0):.1f} {R * math.sin(a0):.1f} A{R} {R} 0 0 1 {R * math.cos(a1):.1f} {R * math.sin(a1):.1f} Z" fill="{col}" stroke="#e8c070" stroke-width="1.5"/>'
    wheel = (f'<g transform="translate(300 196)" filter="url(#sh)">'
             f'<circle r="{R + 22}" fill="url(#wood)" stroke="#3a1a08" stroke-width="5"/><circle r="{R + 6}" fill="#e8c070"/>'
             f'<g transform="rotate(12)">{wedges}</g>'
             f'<circle r="{R * .55:.0f}" fill="#5a2a10" stroke="#e8c070" stroke-width="4"/>'
             f'<circle r="34" fill="url(#hub)" stroke="#8a5a00" stroke-width="4"/>'
             + "".join(f'<path d="M0 0 L{42 * math.cos(a):.1f} {42 * math.sin(a):.1f}" stroke="#e8b030" stroke-width="7" stroke-linecap="round"/>' for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2))
             + '<circle r="12" fill="url(#hub)"/>'
             f'<circle cx="{R * .82 * math.cos(-.9):.1f}" cy="{R * .82 * math.sin(-.9):.1f}" r="10" fill="url(#ball)" stroke="#888" stroke-width="2"/>'
             '</g>')
    dice = ('<g transform="translate(410 400) rotate(16)" filter="url(#sh2)"><rect x="-30" y="-30" width="60" height="60" rx="12" fill="#fff" stroke="#c8c8d0" stroke-width="3"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#d8203a"/>' for x, y in [(-15, -15), (0, 0), (15, 15)]) + '</g>'
            '<g transform="translate(470 444) rotate(-14)" filter="url(#sh2)"><rect x="-26" y="-26" width="52" height="52" rx="10" fill="#fff" stroke="#c8c8d0" stroke-width="3"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#1a1a24"/>' for x, y in [(-12, -12), (12, -12), (-12, 12), (12, 12)]) + '</g>')
    art = f'''
<rect width="512" height="512" fill="url(#felt)"/>
<ellipse cx="256" cy="120" rx="300" ry="240" fill="url(#lamp)"/>
<path d="M-10 470 Q256 420 522 470" stroke="#e8c070" stroke-width="4" fill="none" opacity=".5"/>
{wheel}
{card(-24, 112, 330, "s")}{card(-4, 176, 316, "h")}
{chip(70, 470, "#3a6ad8", 4)}{chip(160, 476, "#d8203a", 3)}{chip(250, 470, "#1a1a24", 5)}{chip(330, 480, "#e8a020", 2)}
{dice}
{sparkle(360, 120, .8, "#fff6c0")}{sparkle(60, 80, .55)}{sparkle(470, 300, .5)}
'''
    return icon(defs, art)
