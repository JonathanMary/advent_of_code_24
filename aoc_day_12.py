def explore_plot(start, map, visited):
    plot = map[start[0]][start[1]]
    lenx = len(map)
    leny = len(map[0])

    visited_now = {} # keeps track of current visited tiles

    sides = {}

    queue = [start]
    perimeter = 0

    while queue:
        cx, cy = queue.pop(0)
        visited[(cx, cy)] = True # keeps track of plots so we don't visit the same twice
        visited_now[(cx, cy)] = True


        moves = [
            (cx - 1, cy),
            (cx + 1, cy),
            (cx, cy - 1),
            (cx, cy + 1)
        ]
        for move in moves:
            mx, my = move
            if (0 <= mx < lenx) and (0 <= my < leny) and (map[mx][my] == plot):
                if move not in visited_now:
                    queue.append((mx, my))
                    visited_now[(mx, my)] = True
            else:
                # if we're in the plot and a nearby tile is not, there's a fence
                perimeter += 1
                
                if cx - mx == 1:
                    # side[0] => fence up or down current tile
                    # side[1] => where are we on the map
                    side = ["southx" + str(mx), my]
                elif cx - mx == -1:
                    side = ["northx" + str(mx), my]
                elif cy - my == 1:
                    side = ["southy" + str(my), mx]
                elif cy - my == -1:
                    side = ["northy" + str(my), mx]

                if side[0] not in sides:
                    sides[side[0]] = []
                sides[side[0]].append(side[1])


    sides_count = 0
    for fences in sides.values():
        fences.sort()
        sides_count += 1
        for i in range(len(fences) - 1):
            if fences[i] + 1 != fences[i + 1]:
                sides_count += 1
    area = len(visited_now.keys())
    return (area * sides_count, area * perimeter)


with open("aoc12_input.txt") as fd:
    map = [x.strip() for x in fd.readlines()]

visited = {}
part1 = 0
part2 = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if (i, j) not in visited:
            p2, p1 = explore_plot((i, j), map, visited)
            part1 += p1
            part2 += p2

print("Part1:", part1)
print("Part2:", part2)


