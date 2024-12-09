with open("aoc9_input.txt") as fd:
    disk_map = fd.read().strip()

def find_space(disk, length):
    size = 0
    start = 0
    for i, x in enumerate(disk):
        if x == ".":
            size += 1
            if size == 1:
                start = i
            if size == length:
                return start
        if x != ".":
            size = 0
    return 0

            
# format
formatted_disk_map = []
all_files = {}
all_files_sorted = []
is_file = True
id = 0
for x in disk_map:
    x = int(x)
    if is_file:
        all_files[id] = (x, len(formatted_disk_map))
        all_files_sorted.append(id)
        for i in range(x):
            formatted_disk_map.append(id)
        id += 1
        is_file = False
    else:
        for i in range(x):
            formatted_disk_map.append(".")
        is_file = True


formatted_disk_map2 = formatted_disk_map.copy()
# parse formatted file to build the compact one
# PART 1
for i in range(len(formatted_disk_map)):
    if formatted_disk_map[- 1 - i] != ".":
        empty_block = formatted_disk_map.index(".")
        if empty_block < len(formatted_disk_map) - 1 - i:
            formatted_disk_map[empty_block] = formatted_disk_map[- 1 - i]
            formatted_disk_map[- 1 - i] = "."
        else:
            break

# PART 2
all_files_sorted.reverse()
for id in all_files_sorted:
    start = find_space(formatted_disk_map2, all_files[id][0])
    if start != 0:
        if start + i < all_files[id][1]:
            for i in range(all_files[id][0]):
                formatted_disk_map2[start + i] = id
                formatted_disk_map2[all_files[id][1] + i] = "."

# calculate checksums
part1 = 0
for i, x in enumerate(formatted_disk_map):
    if x != ".":
        part1 += i * x
    else: break
part2 = 0
for i, x in enumerate(formatted_disk_map2):
    if x != ".":
        part2 += i * x

print("Part1", part1)
print("Part2", part2)
