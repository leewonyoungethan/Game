"""펭귄 창고 레벨 검증기: BFS로 풀 수 있는지와 최소 밀기 횟수를 계산한다.
Usage: python3 solve.py levels.txt   (levels separated by blank lines, ';' comment lines = names)"""
import sys, collections

def parse(lines):
    walls, goals, boxes, player = set(), set(), set(), None
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch == '#': walls.add((x, y))
            if ch in '.*+': goals.add((x, y))
            if ch in '$*': boxes.add((x, y))
            if ch in '@+': player = (x, y)
    return walls, goals, frozenset(boxes), player

def dead_squares(walls, goals, floor):
    # a non-goal square in a corner is dead
    dead = set()
    for (x, y) in floor:
        if (x, y) in goals: continue
        h = (x - 1, y) in walls or (x + 1, y) in walls
        v = (x, y - 1) in walls or (x, y + 1) in walls
        if h and v: dead.add((x, y))
    return dead

def reachable(start, walls, boxes):
    seen = {start}; q = collections.deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            n = (x+dx, y+dy)
            if n not in seen and n not in walls and n not in boxes: seen.add(n); q.append(n)
    return seen

def solve(lines, limit=400000):
    walls, goals, boxes, player = parse(lines)
    if len(goals) != len(boxes): return ('BAD: goals %d boxes %d' % (len(goals), len(boxes)), None)
    floor = reachable(player, walls, frozenset())
    dead = dead_squares(walls, goals, floor)
    def key(p, b): return (min(reachable(p, walls, b)), b)
    start = key(player, boxes)
    seen = {start}; q = collections.deque([(player, boxes, 0)])
    while q:
        p, b, pushes = q.popleft()
        if b == goals: return ('OK', pushes)
        reach = reachable(p, walls, b)
        for (bx, by) in b:
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                if (bx - dx, by - dy) not in reach: continue
                nb = (bx + dx, by + dy)
                if nb in walls or nb in b or nb in dead: continue
                nbs = (b - {(bx, by)}) | {nb}
                k = key((bx, by), nbs)
                if k in seen: continue
                seen.add(k)
                if len(seen) > limit: return ('LIMIT', None)
                q.append(((bx, by), nbs, pushes + 1))
    return ('UNSOLVABLE', None)

if __name__ == '__main__':
    text = open(sys.argv[1]).read().rstrip('\n')
    blocks = [b for b in text.split('\n\n') if b.strip()]
    for i, blk in enumerate(blocks, 1):
        lines = [l for l in blk.split('\n') if not l.startswith(';')]
        name = next((l[1:].strip() for l in blk.split('\n') if l.startswith(';')), '')
        print(i, name, *solve(lines))
