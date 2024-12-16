with open("input.txt") as f:
    equations: list[tuple[int, list[int]]] = []
    for line in f:
        res, input = line.split(":")
        input = list(map(int, input.split()))
        equations.append((int(res), input))


def solvable(res: int, input: list[int]) -> bool:
    if len(input) == 2:
        x, y = input[0], input[1]
        return x + y == res or x * y == res or int(str(x) + str(y)) == res

    x = input[-1]
    if res % x == 0 and solvable(res // x, input[:-1]):
        return True
    if x < res and solvable(res - x, input[:-1]):
        return True
    if (
        str(res).endswith(str(x))
        and len(str(x)) < len(str(res))
        and solvable(int(str(res)[: -len(str(x))]), input[:-1])
    ):
        return True
    return False


print(sum(map(lambda x: x[0] if solvable(x[0], x[1]) else 0, equations)))
