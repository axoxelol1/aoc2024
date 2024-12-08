from collections import defaultdict
from itertools import combinations


def in_bounds(p: tuple[int, int], limit: int):
    x, y = p
    return 0 <= x <= limit and 0 <= y <= limit


antennas_map: dict[str, list[tuple[int, int]]] = defaultdict(list)

limit = 0
with open("input.txt") as f:
    for i, row in enumerate(f.readlines()):
        limit = len(row.strip()) - 1
        for j, id in enumerate(row.strip()):
            if id != ".":
                antennas_map[id].append((j, limit - i))

antinodes: set[tuple[int, int]] = set()
for antennas in antennas_map.values():
    for pair in combinations(antennas, 2):
        ((x1, y1), (x2, y2)) = pair
        dx, dy = x2 - x1, y2 - y1
        if in_bounds((x1 - dx, y1 - dy), limit):
            antinodes.add((x1 - dx, y1 - dy))
        if in_bounds((x2 + dx, y2 + dy), limit):
            antinodes.add((x2 + dx, y2 + dy))

print(f"Part 1: {len(antinodes)}")

antinodes = set()
for antennas in antennas_map.values():
    for pair in combinations(antennas, 2):
        ((x1, y1), (x2, y2)) = pair
        dx, dy = x2 - x1, y2 - y1
        x, y = x1, y1
        while in_bounds((x, y), limit):
            antinodes.add((x, y))
            x, y = x + dx, y + dy
        x, y = x2, y2
        while in_bounds((x, y), limit):
            antinodes.add((x, y))
            x, y = x - dx, y - dy

print(f"Part 2: {len(antinodes)}")
