def is_valid(arr1, arr2):
    for v1, v2 in zip(arr1, arr2):
        if v1 + v2 > 5:
            return 0
    return 1

with open("aoc25_input.txt", encoding="utf8") as fd:
    raw_input = fd.read().strip()
    keys_and_locks = raw_input.split("\n\n")

keys = []
locks = []
for code in keys_and_locks:
    heights = [-1, -1, -1, -1, -1]
    lines = code.split("\n")
    is_key = lines[0][0] == "."
    for line in lines:
        for i, pin in enumerate(line):
            if pin == "#":
                heights[i] += 1
    if is_key:
        keys.append(heights)
    else:
        locks.append(heights)

result = 0
for key in keys:
    for lock in locks:
        result += is_valid(key, lock)

print("result:", result)
