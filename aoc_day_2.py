def check(report: list[int]):
    is_increasing = False
    is_decreasing = False
    if report[0] > report[1]:
        is_decreasing = True
    else:
        is_increasing = True

    for i in range(1, len(report)):
        if abs(report[i-1] - report[i]) > 3\
            or report[i-1] == report[i]\
                or is_increasing and report[i-1] > report[i]\
                    or is_decreasing and report[i-1] < report[i]:
            return i
    return -1

def aoc2():
    with open("input_aoc2.txt") as fd:
        input = fd.readlines()
        p1_safe, p2_safe = 0, 0
        for report in input:
            report_clean = [int(x) for x in report[:-1].split(" ")]
            checked = check(report_clean)
            if checked == -1:
                p1_safe += 1
            else:
                safety1 = check(report_clean[:checked] + report_clean[checked+1:])
                safety2 = check(report_clean[:checked-1] + report_clean[checked:])
                # safety3 solves an edge case where first two values hint at increase when solution is decrease
                # or vice versa, this algorithm will think error is at index 1 or 2, when it's at index 0
                safety3 = check(report_clean[1:])
                if safety1 == -1 or safety2 == -1 or safety3 == -1:
                    p2_safe += 1

    print("Part 1:", p1_safe)
    print("Part 2:", p1_safe + p2_safe)

aoc2()
