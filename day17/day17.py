import math


combo: dict[int, int] = {0: 0, 1: 1, 2: 2, 3: 3}

with open("input.txt") as f:
    inp = f.read().splitlines()
    combo[4] = int(inp[0][12:])
    combo[5] = int(inp[1][12:])
    combo[6] = int(inp[2][12:])
    instructions = list(map(int, inp[4].strip()[9:].split(",")))


def run_program(combo: dict[int, int], instructions: list[int]) -> list[int]:
    combo = combo.copy()
    output: list[int] = []
    pc = 0
    while 0 <= pc < len(instructions):
        instr = instructions[pc]
        if instr == 0:
            operand = combo[instructions[pc + 1]]
            combo[4] = int(combo[4] / math.pow(2, operand))
            pc += 2
        elif instr == 1:
            operand = instructions[pc + 1]
            combo[5] = combo[5] ^ operand
            pc += 2
        elif instr == 2:
            operand = combo[instructions[pc + 1]]
            combo[5] = operand % 8
            pc += 2
        elif instr == 3:
            if combo[4] == 0:
                pc += 2
            else:
                operand = instructions[pc + 1]
                pc = operand
        elif instr == 4:
            combo[5] = combo[5] ^ combo[6]
            pc += 2
        elif instr == 5:
            operand = combo[instructions[pc + 1]]
            output.append(operand % 8)
            pc += 2
        elif instr == 6:
            operand = combo[instructions[pc + 1]]
            combo[5] = int(combo[4] / math.pow(2, operand))
            pc += 2
        elif instr == 7:
            operand = combo[instructions[pc + 1]]
            combo[6] = int(combo[4] / math.pow(2, operand))
            pc += 2
    return output


print("Part 1 output:")
print(",".join(map(str, run_program(combo, instructions))))


def loop_output(a: int) -> int:
    return (((a % 8 ^ 5) ^ int(a / math.pow(2, (a % 8) ^ 5))) ^ 6) % 8


def run(a: int) -> list[int]:
    output: list[int] = []
    while a != 0:
        output.append(loop_output(a))
        a = int(a / 8)
    return output


def find(a: int, n: int) -> int:
    global instructions
    for i in range(0, 8):
        test = a + (i << (n * 3))
        res = run(test)
        if res == instructions:
            return test
        if res[n] == instructions[n]:
            waa = find(test, n - 1)
            if waa != -1:
                return waa
    return -1


print(find(8**15, 15))
