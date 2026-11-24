"""Register a game that lives in games/<id>/ : adds it to games.json, the README table and the icon list.

Usage:
  python3 tools/add_game.py <id> "<title with emoji>" "<genre1,genre2>" "<description>" [author]
"""
import json, pathlib, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent

def main(gid, title, genres, desc, author="Claude"):
    gj = ROOT / "games.json"
    games = json.loads(gj.read_text())
    games = [g for g in games if g["id"] != gid]
    games.append({"id": gid, "title": title, "genres": [g.strip() for g in genres.split(",") if g.strip()], "author": author,
                  "description": desc, "icon": f"icons/{gid}.svg",
                  "added": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M")})
    gj.write_text(json.dumps(games, ensure_ascii=False, indent=2) + "\n")

    readme = ROOT / "README.md"
    lines = readme.read_text().splitlines()
    url = f"https://leewonyoungethan.github.io/Game/games/{gid}/"
    row = f"| [{title}]({url}) (`games/{gid}/`) | {author} | {desc.split('.')[0]} |"
    lines = [l for l in lines if f"(`games/{gid}/`)" not in l]
    last = max(i for i, l in enumerate(lines) if l.startswith("| [") and "github.io" in l or l.startswith("| [") and "claude.ai" in l)
    lines.insert(last + 1, row)
    readme.write_text("\n".join(lines) + "\n")

    mk = ROOT / "tools" / "make_icons.py"
    s = mk.read_text()
    if f'"{gid}"' not in s:
        s = s.replace(', "default"]', f', "{gid}", "default"]')
        mk.write_text(s)
    print("registered", gid)

if __name__ == "__main__":
    main(*sys.argv[1:])
