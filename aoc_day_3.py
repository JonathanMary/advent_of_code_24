import re

def instructions(file: str):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(mul_pattern, "".join(file))
    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])
    return res


with open("aoc3_input.txt") as fd:
    file = fd.read()

clean_file = []
split_do = file.split("do()")
for line in split_do:
    clean_file.append(line.split("don't()")[0])

print("Part 1:", instructions(file))
print("Part 2:", instructions(clean_file))
