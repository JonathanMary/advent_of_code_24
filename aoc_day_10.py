def find_trailheads(start, map):
    # create a function that finds all the trails possible,
    # have the results fit into a set (so the 9 a unique) for part 1
    # keep all possibilities for part 2
    endpoints_p1 = set()
    endpoints_p2 = 0
    queue = [start]
    map_h = len(map)
    map_w = len(map[0])
    while queue:
        (cx, cy) = queue.pop(0)
        if map[cx][cy] == "9":
            endpoints_p1.add((cx, cy))
            endpoints_p2 += 1
            continue
        moves = [
            (cx + 1, cy),
            (cx - 1, cy),
            (cx, cy + 1),
            (cx, cy - 1)
        ]
        for (x, y) in moves:
            if 0 <= x < map_h\
                and 0 <= y < map_w\
                    and int(map[x][y]) == int(map[cx][cy]) + 1:
                queue.append((x, y))
    return len(endpoints_p1), endpoints_p2

with open("aoc10_input.txt") as fd:
    topo_map = [x.strip() for x in fd.readlines()]
    
# trailhead score is the number of 9 heigh positions that can be reached by a trailhead
# parse the topo_map, when 0, run the function
part1 = 0
part2 = 0
for i in range(len(topo_map)):
    for j in range(len(topo_map[i])):
        if topo_map[i][j] == "0":
            p1 , p2 = find_trailheads((i, j), topo_map)
            part1 += p1
            part2 += p2

print("Part1:", part1)
print("Part2:", part2)
