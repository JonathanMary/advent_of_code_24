from queue import PriorityQueue

def racetrack_details(track):
    """Find start, end, and walls locations"""
    s, e, w = (0,0), (0,0), set()

    for i, row in enumerate(track):
        for j, tile in enumerate(row):
            if tile == "#":
                w.add((i,j))
            elif tile == "S":
                s = (i,j)
            elif tile == "E":
                e = (i,j)
    return s, e, w


def get_path(st, wa, he, wi):
    """Finds all paths from a starting point and return coordinates + distance from start"""
    q = PriorityQueue()
    visited = {}

    q.put((0, st))
    visited.update({ st: 0 })

    while not q.empty():
        c_steps, c_coord = q.get()
        (cx, cy) = c_coord
        moves = [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]
        for move in moves:
            (nx, ny) = move
            if 0 <= nx <= he\
                and 0 <= ny <= wi\
                    and move not in visited\
                        and move not in wa:
                visited.update({ move: c_steps + 1 })
                q.put((c_steps + 1, move))
    return visited

def check_walls(st, en, wa, he, wi, max_moves):
    """Could be better here, kinda hack and slow"""

    q = PriorityQueue()
    visited = set()
    q.put((0, st, []))
    visited.add(st)

    while not q.empty():
        c_steps, c_coord, c_path = q.get()
        if c_steps > max_moves:
            break
        if c_coord == en:
            return True
        (cx, cy) = c_coord

        moves = [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]
        for move in moves:
            (nx, ny) = move
            if 0 <= nx < he\
                and 0 <= ny < wi\
                    and move not in visited\
                        and not (c_steps == max_moves and move not in wa):
                visited.add(move)
                q.put((c_steps + 1, move, c_path + [move]))
    return False


with open("aoc20_input.txt", encoding="utf8") as fd:
    racetrack = [x.strip() for x in fd.readlines()]

height = len(racetrack)
width = len(racetrack[0])
start, end, walls = racetrack_details(racetrack)

moves_from_start = get_path(start, walls, height, width)
moves_from_end = get_path(end, walls, height, width)

no_shortcut = moves_from_start[end]

all_time_saved = {}
for wall in walls:
    (x, y) = wall
    shorts = [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]
    distances_to_start = []
    distances_to_end = []
    for short in shorts:
        mfs = moves_from_start.get(short)
        mfe = moves_from_end.get(short)
        if mfs is not None:
            distances_to_start.append(mfs)
        if mfe is not None:
            distances_to_end.append(mfe)
    if distances_to_start and distances_to_end:
        time_saved = no_shortcut - (min(distances_to_start) + min(distances_to_end) + 2)
        if time_saved not in all_time_saved:
            all_time_saved[time_saved] = 0
        all_time_saved[time_saved] += 1

part1 = 0
for k, v in all_time_saved.items():
    if k >= 50:
        part1 += v
print("Part1", part1)

visited = set()
part2 = 0
for mvt, dist in moves_from_start.items():
    (x, y) = mvt
    for i in range(-20, 20):
        for j in range(-20, 20):
            abs_dist = abs(i) + abs(j)
            if abs_dist <= 20:
                mfe = moves_from_end.get((x+i, y+j))
                if mfe is not None:
                    if ((x+i, y+j), mvt) not in visited\
                        and (mvt, (x+i, y+j)) not in visited:
                        visited.add(((x+i, y+j), mvt))
                        if no_shortcut - (mfe + abs_dist + dist) >= 50:
                            is_valid = check_walls(mvt, (x+i, y+j), walls, height, width, abs_dist)
                            if is_valid:
                                part2 += 1

print("Part2", part2)
