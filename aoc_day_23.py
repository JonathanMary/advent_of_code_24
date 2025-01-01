with open("aoc23_input.txt", encoding="utf8") as fd:
    raw_input = [x.strip() for x in fd.readlines()]

network = {}
for connection in raw_input:
    comp_a, comp_b = connection.split("-")
    if comp_a not in network:
        network[comp_a] = []
    network[comp_a].append(comp_b)
    if comp_b not in network:
        network[comp_b] = []
    network[comp_b].append(comp_a)

LANs = set()
for comp_a, first_layer in network.items():
    for comp_b in first_layer:
        second_layer = network[comp_b]
        for comp_c in second_layer:
            if comp_c in first_layer:
                if "t" in [comp_a[0], comp_b[0], comp_c[0]]:
                    LANs.add(str(sorted([comp_a, comp_b, comp_c])))
print("Part1", len(LANs))

best = ""
visited = set()
for computer in network:
    q = []
    q.append((computer, computer))

    while q:
        combos_string, to_visit = q.pop(0)
        combos = combos_string.split(",")
        valid = True
        for combo in combos:
            if combo not in network[to_visit] + [to_visit]:
                valid = False
                break

        if valid:
            if len(combos_string) > len(best):
                best = combos_string

            for link in network[to_visit]:
                new_combos = combos.copy()
                if link not in combos:
                    new_combos.append(link)
                    new_combos.sort()
                    combos_string = ",".join(new_combos)
                    if combos_string not in visited:
                        q.append((combos_string, link))
                        visited.add(combos_string)

print("Part2:", best)
