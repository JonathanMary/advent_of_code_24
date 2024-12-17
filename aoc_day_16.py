from queue import PriorityQueue

def findstart(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return (i, j)
            

def step(x, y, position):
    # East = y+1, South= x+1, West = y-1, North = x-1
    if position == 0:
        return (x, y + 1)
    elif position == 1:
        return (x + 1, y)
    elif position == 2:
        return (x, y -1)
    else:
        return (x - 1, y)


with open("aoc16_input.txt") as fd:
    map = [x.strip() for x in fd.readlines()]


start = findstart(map)
q = PriorityQueue()
# { (coordinates, position): cost_so_far }
visited = {}

# cost, (coords), position, path_visited
q.put((0, start, 0, [start]))
visited[(start, 0)] = 0

part1 = 999999
routes = []
while not q.empty():
    cost_so_far, (cx, cy), cp, cpath = q.get()

    if map[cx][cy] == "E" and cost_so_far <= part1:
        routes += cpath
        part1 = cost_so_far
    elif map[cx][cy] == "E":
        # We get all best paths then exit
        break

    moves = [
        (cost_so_far + 1000, (cx, cy), (cp + 1) % 4, cpath),
        (cost_so_far + 1000, (cx, cy), (cp - 1) % 4, cpath),
        (cost_so_far + 1, step(cx, cy, cp), cp, cpath + [step(cx, cy, cp)])
    ]
    for move in moves:
        new_cost, (nx, ny), np, npath = move
        if map[nx][ny] != "#":
            if ((nx, ny), np) not in visited or new_cost <= visited[((nx, ny), np)]:
                q.put((new_cost, (nx, ny), np, npath))
                visited[((nx, ny), np)] = new_cost
            
print("PART1:", part1)
print("PART2:", len(set(routes)))
