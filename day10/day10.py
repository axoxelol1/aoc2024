from collections import deque

with open("input.txt") as f:
    input = [[int(c) for c in line] for line in f.read().splitlines()]

n = len(input)

nodes = []
trailheads: list[int] = []
adj: list[list[int]] = []
vals: list[int] = []
for i in range(n):
    for j in range(n):
        vals.append(input[i][j])
        if input[i][j] == 0:
            trailheads.append(i * n + j)
        neighbours: list[int] = []
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (
                0 <= i + di < n
                and 0 <= j + dj < n
                and input[i][j] + 1 == input[i + di][j + dj]
            ):
                neighbours.append((i + di) * n + (j + dj))
        adj.append(neighbours)


def part1(trailheads: list[int], adj: list[list[int]], vals: list[int]) -> int:
    total = 0
    for head in trailheads:
        to_visit: deque[int] = deque([head])
        reachable_ends: set[int] = set()
        while to_visit:
            curr = to_visit.popleft()
            if vals[curr] == 9:
                reachable_ends.add(curr)
            for neighbour in adj[curr]:
                to_visit.append(neighbour)
        total += len(reachable_ends)
    return total


def part2(trailheads: list[int], adj: list[list[int]], vals: list[int]) -> int:
    total = 0
    for head in trailheads:
        to_visit: deque[int] = deque([head])
        while to_visit:
            curr = to_visit.popleft()
            if vals[curr] == 9:
                total += 1
            for neighbour in adj[curr]:
                to_visit.append(neighbour)
    return total


print(f"Part 1: {part1(trailheads, adj, vals)}")
print(f"Part 2: {part2(trailheads, adj, vals)}")
