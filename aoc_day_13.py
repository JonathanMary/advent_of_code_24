import re
# from queue import PriorityQueue

# def heuristic(goal, next):
#     return abs(goal[0] - next[0]) + abs(goal[1] - next[1])

def cheaper(machine):
    machine = machine.split("\n")

    for i in range(3):
        if i == 0:
            x1, y1 = [int(x) for x in re.findall(r'\d+', machine[i])]
        if i == 1:
            x2, y2 = [int(x) for x in re.findall(r'\d+', machine[i]) ]
        if i == 2:
            px, py = [int(x) for x in re.findall(r'\d+', machine[i])]
    px += 10000000000000
    py += 10000000000000

    B = (py * x1 - px * y1) / (y2 * x1 - x2 * y1)
    A = (px - B * x2) / x1
    print(A, B)
    return 3 * A + B

# This was not fast enough
# Had to do the math :D
#     # (Heuristic, X, Y, Cost)
#     q = PriorityQueue()
#     visited = dict()
#     q.put((heuristic(prize, [0, 0]), 0, 0, 0))
#     visited[(0, 0)] = 0

#     while not q.empty():
#         ch, cx, cy, cc = q.get(0)
#         if cx == prize[0] and cy == prize[1]:
#             print(cc)
#             return cc
#         moves = [
#             (ch, cx + bA[0], cy + bA[1], cc + 3),
#             (ch, cx + bB[0], cy + bB[1], cc + 1)
#         ]
#         for move in moves:
#             mh, mx, my, mc = move
#             if (mx, my) not in visited or visited[(mx, my)] < mh:
#                 heur = heuristic(prize, [mx, my]) + mc
#                 if heur < mh and mx <= prize[0] and my <= prize[1]:
#                     new_mh = heur + mc
#                     q.put((new_mh, mx, my, mc))
#                     visited[(mx, my)] = mh

#     return 0


with open("aoc13_input.txt") as fd:
    machines = [x for x in fd.read().strip().split("\n\n")]

total = 0
for machine in machines:
    res = cheaper(machine)
    if res == int(res):
        total += res

print("Part2:", total)
