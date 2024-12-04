with open("aoc4_input.txt") as fd:
    lines = fd.read().split("\n")
res1 = 0


for i in range(len(lines) - 3):
    for j in range(len(lines[i]) - 3):
        if(lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] in ["XMAS", "SAMX"]):
            res1 += 1
        if(lines[i][j+3] + lines[i+1][j+2] + lines[i+2][j+1] + lines[i+3][j] in ["XMAS", "SAMX"]):
            res1 += 1
for i in range(len(lines)):
    for j in range(len(lines[i]) - 3):
        if (lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3] in ["XMAS", "SAMX"]):
            res1 += 1
for i in range(len(lines) - 3):
    for j in range(len(lines[i])):
        if(lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] in ["XMAS", "SAMX"]):
            res1 += 1


res2 = 0
for i in range(len(lines) - 2):
    for j in range(len(lines[i]) - 2):
        if(lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] in ["MAS", "SAM"]):
            if(lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j] in ["MAS", "SAM"]):
                res2 += 1


print("Part 1:", res1)
print("Part 2:", res2)
