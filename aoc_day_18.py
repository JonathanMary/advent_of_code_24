from queue import PriorityQueue
import re

with open("aoc18_input.txt") as fd:
    input = [x for x in fd.read().strip().split("\n")]

def build_blocks(length) -> set:
    blocks = set()
    for pos in range(length):
        a, b = [int(x) for x in re.findall(r'\d+', input[pos])]
        blocks.add((a, b))
    return blocks

def find_route(blocks, size):
    start, end = (0,0), (size,size)
    visited = set()
    q = PriorityQueue()
    q.put((0, start, set()))
    visited.add(start)

    while not q.empty():
        cs, (cx,cy), cp = q.get()
        cp.add((cx, cy))
        if (cx, cy) == end:
            return cs, cp
        moves = [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]
        for move in moves:
            if move not in blocks\
                and move not in visited\
                    and 0 <= move[0] <= end[0]\
                        and 0 <= move[1] <= end[1]:
                visited.add(move)
                new_cp = cp.copy()
                new_cp.add(move)
                q.put((cs+1, move, new_cp))
    return None, None


MEM_SIZE, BYTES = 70, 1024
part1 = find_route(build_blocks(BYTES), MEM_SIZE)
print("Part1:", part1[0])

blocks = build_blocks(BYTES)
route = find_route(blocks, MEM_SIZE)[1]
while True:
    BYTES += 1
    a, b = [int(x) for x in re.findall(r'\d+', input[BYTES])]
    blocks.add((a, b))
    if (a, b) in route:
        route = find_route(blocks, MEM_SIZE)[1]
        if not route:
            print("Part2", (a, b))
            break
    if BYTES > len(input):
        print("Always safe!")
        break

