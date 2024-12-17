def combo(operand, registers):
    if operand == 7:
        raise RuntimeError("Invalid operand.")
    elif operand == 6:
        return registers["C"]
    elif operand == 5:
        return registers["B"]
    elif operand == 4:
        return registers["A"]
    else:
        return operand
    

def instructions(opcode, operand, registers):
    if opcode == 0:
        registers["A"] //= 2 ** combo(operand, registers)
        return "adv", None
    elif opcode == 1:
        registers["B"] ^= operand
        return "bxl", None
    elif opcode == 2:
        registers["B"] = combo(operand, registers) % 8
        return "bst", None
    elif opcode == 3:
        if registers["A"] != 0:
            return "jnz", operand
        else:
            return "", None
    elif opcode == 4:
        registers["B"] ^= registers["C"]
        return "bxc", None
    elif opcode == 5:
        return "out", combo(operand, registers) % 8
    elif opcode == 6:
        registers["B"] = registers["A"] // 2 ** combo(operand, registers)
        return "bdv", None
    elif opcode == 7:
        registers["C"] = registers["A"] // 2 ** combo(operand, registers)
        return "cdv", None


def launch(registers, program):
    res = []
    ptr = 0
    while ptr < len(program):
        opcode, operand = program[ptr], program[ptr+1]
        instruction, value = instructions(opcode, operand, registers)
        ptr += 2
        if instruction == "jnz":
            ptr = value
        elif instruction == "out":
            res.append(value)
    return res


with open("aoc17_input.txt") as fd:
    input = [x.strip().split(' ') for x in fd.readlines()]
registers = {
    "A": int(input[0][-1]),
    "B": 0,
    "C": 0
}

program = [int(x) for x in input[-1][-1].split(",")]

val = launch(registers, program)
print("Part1:", val)

res: int
q = [(1, 0)]
while q:
    (i, A) = q.pop(0)
    for regA in range(A, A+8):
        registers["A"] = regA
        if launch(registers, program) == program[-i:]:
            q += [(i+1, regA*8)]
            if i == len(program):
                res = regA
                q = []
print("Part2:", res)
