def find_antinodes(a, b, map_h, map_w):
    ah, aw = a[0], a[1]
    bh, bw = b[0], b[1]

    antinode_n1 = []
    n1h: int
    n1w: int
    resonance = 1
    while True:
        if ah > bh:
            diff_h = resonance * (ah - bh)
            n1h = ah + diff_h
        else:
            diff_h = resonance * (bh - ah)
            n1h = ah - diff_h
        if aw > bw:
            diff_w = resonance * (aw - bw)
            n1w = aw + diff_w
        else:
            diff_w = resonance * (bw - aw)
            n1w = aw - diff_w
        if (n1h >= 0) and (n1h < map_h) and (n1w >= 0) and (n1w < map_w):
            antinode_n1.append((n1h, n1w))
            resonance += 1
        else: break

    antinode_n2 = []
    n2h: int
    n2w: int
    resonance = 1
    while True:
        if ah > bh:
            diff_h = resonance * (ah - bh)
            n2h = bh - diff_h
        else:
            diff_h = resonance * (bh - ah)
            n2h = bh + diff_h
        if aw > bw:
            diff_w = resonance * (aw - bw)
            n2w = bw - diff_w
        else:
            diff_w = resonance * (bw - aw)
            n2w = bw + diff_w
        if (n2h >= 0) and (n2h < map_h) and (n2w >= 0) and (n2w < map_w):
            antinode_n2.append((n2h, n2w))
            resonance += 1
        else: break

    return antinode_n1 + antinode_n2


with open("aoc8_input.txt") as fd:
    map = [line.strip() for line in fd.readlines()]
antinodes = set()
map_h = len(map)
map_w = len(map[0])

antennas = {}

for i in range(map_h):
    for j in range(map_w):
        current = map[i][j]
        if current != ".":
            antinodes.add((i, j))
            if current not in antennas:
                antennas[current] = [(i, j)]
            else:
                for antenna in antennas[current]:
                    for resonant_harmonic in find_antinodes((i, j), antenna, map_h, map_w):
                        antinodes.add(resonant_harmonic)
                antennas[current].append((i, j))

print("Part2:", len(antinodes))


