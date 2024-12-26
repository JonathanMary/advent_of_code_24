wide, tall = 101, 103


def one_second(robots: dict, w: int, t: int):
    for k, v in robots.items():
        robots[k] = (v[0] + k[0]) % wide, (v[1] + k[1]) % tall


with open("aoc14_input.txt", encoding="utf8") as fd:
    raw_input = [x.strip() for x in fd.readlines()]
robots = {}
for i, robot in enumerate(raw_input):
    nums = [[int(y) for y in x[2:].split(",")] for x in robot.split(" ")]
    p, v = nums[1] + [i], nums[0]
    robots[tuple(p)] = v

for run in range(100):
    one_second(robots, wide, tall)

no, ne, so, se = 0,0,0,0
for robot in robots.values():
    i, j = robot
    if i < (wide // 2):
        if j < (tall // 2):
            no += 1
        elif j > (tall // 2):
            so += 1
    elif i > (wide // 2):
        if j < (tall // 2):
            ne += 1
        elif j > (tall // 2):
            se += 1
print("Part1:", no * ne * so * se)

seconds = 0
while True:
    seconds += 1
    one_second(robots, wide, tall)

    setrobots = set(robots.values())
    print_map = tall * [""]
    count = 0
    le_print = False
    for j in range(tall):
        for i in range(wide):
            if (i,j) in setrobots:
                print_map[j] += "1"
                count += 1
            else:
                print_map[j] += "."
                count = 0
            if count > 7:
                le_print = True
    if le_print:
        print("\n".join(print_map))
        print("\n")
        break
print("Part2:", seconds)
