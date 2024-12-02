import timeit

def aoc1():
    with open("aoc1_input.txt") as fd:
        lists = fd.readlines()

    list1, list2, total_distance = dict(), dict(), 0

    for line in lists:
        val = line.split('   ')
        v1, v2 = int(val[0]), int(val[-1])
        if v1 in list2:
            total_distance += v1 * list2[v1]
        if v1 not in list1:
            list1[v1] = 0
        list1[v1] += 1
        if v2 in list1:
            total_distance += v2 * list1[v2]
        if v2 not in list2:
            list2[v2] = 0
        list2[v2] += 1

    return total_distance


execution_time = timeit.timeit(aoc1, number=10000)
print(f"Execution time: {execution_time / 10000: .6f} seconds.")



# This solution is truly one pass but it's 50% slower

# def aoc1():
#     with open("aoc1_input.txt", encoding="utf-8") as fd:
#         file = fd.read()

#         first_half = True
#         v1, v2 = "", ""
#         list1, list2, total_distance = dict(), dict(), 0

#         for char in file:
#             if char.isnumeric():
#                 if first_half:
#                     v1 += char
#                 else:
#                     v2 += char
#                 continue

#             if char == " ":
#                 if not first_half:
#                     continue
#                 first_half = False
#                 v1 = int(v1)
#                 if v1 in list2:
#                     total_distance += v1 * list2[v1]
#                 if v1 not in list1:
#                         list1[v1] = 0
#                 list1[v1] += 1
#                 v1 = ""
#                 continue

#             if char == "\n":
#                 first_half = True
#                 v2 = int(v2)
#                 if v2 in list1:
#                     total_distance += v2 * list1[v2]
#                 if v2 not in list2:
#                     list2[v2] = 0
#                 list2[v2] += 1
#                 v2 = ""

#         return total_distance

# execution_time = timeit.timeit(aoc1, number=10000)
# print(f"Execution time: {execution_time / 10000: .6f} seconds.")
