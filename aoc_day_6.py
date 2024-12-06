with open("aoc6_input.txt") as fd:
    lab_map = fd.read().split("\n")

guard = []
guard_positions = ["^", ">", "v", "<"]
guard_orientation = 0

def find_guard(map):
    lab_h = len(map)
    lab_w = len(map[0])
    for i in range(lab_h):
        for j in range(lab_w):
            if map[i][j] in guard_positions:
                guard = [i, j]
                guard_orientation = guard_positions.index(map[i][j])
                map[i] = map[i][:j] + "." + map[i][j+1:]
                return guard, guard_orientation, map

guard, guard_orientation, lab_map_no_guard = find_guard(lab_map.copy())

visited = set()
visited.add((guard[0], guard[1]))

loop = True
while loop:
    next_move = guard.copy()
    if guard_orientation == 0: next_move[0] -= 1
    elif guard_orientation == 1: next_move[1] += 1
    elif guard_orientation == 2: next_move[0] += 1
    elif guard_orientation == 3: next_move[1] -= 1


    if 0 > next_move[0]\
        or  next_move[0] > len(lab_map)-1\
            or 0 > next_move[1]\
                or next_move[1] > len(lab_map[0])-1:
        break
    
    next = lab_map_no_guard[next_move[0]][next_move[1]]

    if next == ".":
        guard = next_move.copy()

        visited.add((guard[0], guard[1]))
    elif next == "#":
        guard_orientation = (guard_orientation + 1) % 4
        
print("Part1:", len(visited))

p2 = 0
for tile in visited:
    i, j = tile
    guard, guard_orientation, new_map = find_guard(lab_map.copy())
    if new_map[i][j] == ".":
        new_map[i] = new_map[i][:j] + "#" + new_map[i][j+1:]

        visited = set()
        visited.add((guard[0], guard[1], guard_orientation))

        loop = True
        while loop:
            next_move = guard.copy()
            if guard_orientation == 0: next_move[0] -= 1
            elif guard_orientation == 1: next_move[1] += 1
            elif guard_orientation == 2: next_move[0] += 1
            elif guard_orientation == 3: next_move[1] -= 1


            if 0 > next_move[0]\
                or  next_move[0] > len(new_map)-1\
                    or 0 > next_move[1]\
                        or next_move[1] > len(new_map[0])-1:
                break
            
            next = new_map[next_move[0]][next_move[1]]

            if next == ".":
                guard = next_move.copy()
                if ((guard[0], guard[1], guard_orientation)) in visited:
                    p2 += 1
                    break
                visited.add((guard[0], guard[1], guard_orientation))
            elif next == "#":
                guard_orientation = (guard_orientation + 1) % 4

print("Part2:", p2)
