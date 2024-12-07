from itertools import product
from functools import reduce


def apply_operator(x: int, y: int, op: str):
    if op == "*":
        return x * y
    elif op == "+":
        return x + y
    else:
        return int(str(x) + str(y))


def solve(operators: list[str], equations: list[tuple[int, list[int]]]) -> int:
    calibrations = 0
    for equation in equations:
        result, input = equation
        for ops in product(operators, repeat=len(input) - 1):
            num_with_ops = zip(input[1:], ops)
            if result == reduce(
                lambda x, y: apply_operator(x, y[0], y[1]), num_with_ops, input[0]
            ):
                calibrations += result
                break
    return calibrations


with open("input.txt") as f:
    equations: list[tuple[int, list[int]]] = []
    for line in f:
        res, input = line.split(":")
        input = list(map(int, input.split()))
        equations.append((int(res), input))


print(f"Part 1: {solve(["*","+"], equations)}")
print(f"Part 2: {solve(["*","+", "||"], equations)}")
