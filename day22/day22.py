from collections import defaultdict

sequence_prices: dict[tuple[int, int, int, int], list[int]] = defaultdict(list)


def secret(start: int, n: int) -> int:
    global sequence_prices
    bought_sequence: set[tuple[int, int, int, int]] = set()
    diffs: list[int] = []
    for _ in range(n):
        before = start
        start ^= start << 6
        start &= (1 << 24) - 1
        start ^= start >> 5
        start &= (1 << 24) - 1
        start ^= start << 11
        start &= (1 << 24) - 1
        diffs.append(start % 10 - before % 10)
        if len(diffs) >= 4:
            sequence = (diffs[-4], diffs[-3], diffs[-2], diffs[-1])
            if sequence in bought_sequence:
                continue
            bought_sequence.add(sequence)
            sequence_prices[sequence].append(start % 10)
    return start


with open("input.txt") as f:
    secret_numbers = [int(line) for line in f]

print(f"Part 1: {sum(map(lambda num: secret(num, 2000), secret_numbers))}")

print(f"Part 2: {max(map(sum, sequence_prices.values()))}")
