with open("input.txt") as f:
    starting_stones = list(map(int, f.read().strip().split()))


cache: dict[tuple[int, int], int] = {}


def blink(stone: int, left: int) -> int:
    global cache
    if (stone, left) in cache:
        return cache[(stone, left)]
    if left == 0:
        res = 1
    elif stone == 0:
        res = blink(1, left - 1)
        cache[(stone, left)] = res
        return res
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        res = blink(int(str(stone)[:mid]), left - 1) + blink(
            int(str(stone)[mid:]), left - 1
        )
    else:
        res = blink(stone * 2024, left - 1)
    cache[(stone, left)] = res
    return res


print(f"Part 1: {sum(map(lambda st: blink(st, 25), starting_stones))}")
print(f"Part 2: {sum(map(lambda st: blink(st, 75), starting_stones))}")
