# After 6 blinks, "125 17" contains 4 occurences of 2.
# The single and 2 digits quickly become a huge number.
# By having it in a dict instead of array, we cut calculations by a lot

def get_answer(stones_count):
    res = 0
    for v in stones_count:
        res += v
    return res

with open("aoc11_input.txt") as fd:
    stones = {int(x): 1 for x in fd.read().strip().split()}

part1 = 0

blinks = 75
for i in range(blinks):
    if i == 25:
        part1 = get_answer(stones.values())

    temp_stones = {}
    for stone, count in stones.items():
        len_stone = len(str(stone))
        if stone == 0:
            temp_stones = temp_stones | { 1: temp_stones.get(1, 0) + count}
        elif not (len_stone & 1):
            first_stone = int(str(stone)[:len_stone // 2])
            temp_stones = temp_stones | { first_stone: temp_stones.get(first_stone, 0) + count}
            second_stone = int(str(stone)[len_stone // 2:])
            temp_stones = temp_stones | { second_stone: temp_stones.get(second_stone, 0) + count}

        else:
            mult_stone = stone * 2024
            temp_stones = temp_stones | { mult_stone: temp_stones.get(mult_stone, 0) + count}

    stones = temp_stones

print("Part1:", part1)
print("Part2:", get_answer(stones.values()))


# This got me to part 1, memo not enough for part 2.

# memo = {
#     "0": ["1"],
#     }

# def change(stone):
# # if stone = 0 -> stone = 1
#     length = len(stone)
# # if stone has even number of digits -> stone replace by 2 stones, no extra digit ex 1000 -> 10 | 0
#     if not (length & 1):
#         memo[stone] = [str(int(stone[:length // 2])), str(int(stone[length // 2:]))]
# # else stone number * 2024
#     else:
#         memo[stone] = [str(int(stone) * 2024)]

# blinks = 10
# stones = ["9"]
# for i in range(blinks):
#     new_stones = []
#     for stone in stones:
#         if stone not in memo:
#             change(stone)
#         new_stones += memo[stone]

#     stones = new_stones
#     print(i, len(stones))
#     print(stones)

# print("Part1:", len(stones))
# print("Part1 unique stones:", len(set(stones))) <= le hint

# print("Part2:", part2)
