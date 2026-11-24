"""Generate the game app icons in icons/ (512x512 SVG).

Each icon lives in its own module under tools/icons/ (one per game id, with
'-' written as '_'), and shares helpers from tools/icons/common.py.

Run: python3 tools/make_icons.py            # all icons
     python3 tools/make_icons.py rock f16   # only some
"""
import importlib, pathlib, sys, xml.dom.minidom

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from icons.common import dedupe  # noqa: E402

OUT = ROOT.parent / "icons"
ALL = ["rock", "eggsteal", "road", "rail-dash", "getaway", "piano-tiles",
       "nayul", "starknight", "clearsky", "f16", "planet-merge", "lily-hop", "star-breaker", "treasure-island", "penguin-warehouse", "whack-mole", "memory-forest", "dragon-snake", "quiet-pond", "cloud-tower", "mushroom-defense", "word-detective", "meteor-dodge", "light-up", "slime-pet", "default"]

def main(ids):
    OUT.mkdir(exist_ok=True)
    for gid in ids:
        mod = importlib.import_module("icons." + gid.replace("-", "_"))
        svg = dedupe(mod.build())
        xml.dom.minidom.parseString(svg.encode())      # fail loudly on invalid SVG
        (OUT / f"{gid}.svg").write_text(svg)
        print(f"wrote icons/{gid}.svg ({len(svg) // 1024} KB)")

if __name__ == "__main__":
    main(sys.argv[1:] or ALL)
