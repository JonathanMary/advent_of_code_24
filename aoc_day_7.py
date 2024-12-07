with open("aoc7_input.txt") as fd:
    equations = [line.strip().replace(":", "").split(" ") for line in fd.readlines()]

queue = []
# Part 1 is the same except mult * 2 and remove last queue.append()
part2 = 0

for equation in equations:
    result = int(equation[0])
    test_values = equation[1:]
    queue = [int(test_values[0])]
    i_queue = 0
    for i in range(1, len(test_values)):
        mult = 1
        for k in range(i - 1):
            mult *= 3
        for j in range(mult):
            value = int(test_values[i])
            tot = int(queue[i_queue])
            queue.append(tot * value)
            queue.append(tot + value)
            queue.append(int(str(tot)+str(value)))
            i_queue += 1
    # print(queue)
    if result in queue[-(mult * 3):]:
        print(equation, mult)
        part2 += result
print("Part2:", part2)
