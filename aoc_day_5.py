# TODO Refactor and make it nice (and smarter?) if I have time
with open("aoc5_input.txt") as fd:
    rules, updates = fd.read().split("\n\n")
    updates = [[p for p in u.split(",")] for u in updates.split("\n")]

p1 = 0
p2 = 0

visited = []
i = 0
while len(updates) > i:
    update = updates[i]
    is_valid = True
    visited = []
    for page in update:
        for j, page_visited in enumerate(visited):
            if page + "|" + page_visited in rules:
                if is_valid:
                    removed_faulty = update[:j] + update[j+1:]
                    insert_faulty = removed_faulty + [update[j]]
                    updates.append(insert_faulty)
                is_valid = False
        visited.append(page)
    if is_valid:
        p2 += int(update[(len(update)) // 2])
    i += 1
        

# print("Part 1:", p1)
print("Part 2:", p2)

