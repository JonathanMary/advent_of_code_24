def calc(num):
    num = ((num * 64) ^ num) & ((1 << 24) - 1)
    num = ((num // 32) ^ num) & ((1 << 24) - 1)
    return ((num * 2048) ^ num) & ((1 << 24) - 1)


with open("aoc22_input.txt", encoding="utf8") as fd:
    raw_input = [int(x.strip()) for x in fd.readlines()]

values = {}

for secret in raw_input:
    visited = set()
    q = []
    prev = secret % 10
    # build queue
    for i in range(4):
        secret = calc(secret)
        digit = secret % 10
        q.append(digit - prev)
        prev = digit
    changes = str(q)
    values[changes] = digit
    visited.add(changes)

    for i in range(1996):
        secret = calc(secret)
        digit = secret % 10
        q.append(digit - prev)
        q.pop(0)
        prev = digit
        changes = str(q)
        if changes not in visited:
            if changes not in values:
                values[changes] = 0
            values[changes] += digit
                
            visited.add(changes)

print(max(values.values()))

# secret_numbers.append(secret)

# print(secret_numbers)
# print(sum(secret_numbers))
