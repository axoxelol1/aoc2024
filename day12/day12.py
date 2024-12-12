from collections import deque, defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()

n = len(input)

type point = tuple[int, int]

adj: list[list[int]] = []
plants: list[str] = []
edge_nodes: set[int] = set()
corner_nodes: set[int] = set()
for i in range(n):
    for j in range(n):
        plants.append(input[i][j])
        if i in [0, n - 1] and j in [0, n - 1]:
            corner_nodes.add(i * n + j)
        elif i in [0, n - 1] or j in [0, n - 1]:
            edge_nodes.add(i * n + j)
        curr_adj: list[int] = []
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= i + di < n and 0 <= j + dj < n:
                curr_adj.append((i + di) * n + (j + dj))
        adj.append(curr_adj)


def part1(
    adj: list[list[int]], plants: list[str]
) -> tuple[int, list[tuple[int, int, list[int]]]]:
    all = set([i for i in range(len(adj))])
    visited: set[int] = set()
    sol = 0
    regions: list[tuple[int, int, list[int]]] = []
    while 0 < len(all.difference(visited)):
        region: list[int] = []
        area = 0
        perimeter = 0
        first = all.difference(visited).pop()
        visited.add(first)
        to_visit = deque([first])
        while 0 < len(to_visit):
            node = to_visit.popleft()
            area += 1
            region.append(node)
            if node in corner_nodes:
                perimeter += 2
            elif node in edge_nodes:
                perimeter += 1
            for neighbor in adj[node]:
                if plants[neighbor] != plants[node]:
                    perimeter += 1
                elif neighbor not in visited:
                    visited.add(neighbor)
                    to_visit.append(neighbor)
        sol += area * perimeter
        regions.append((area, perimeter, region))
    return sol, regions


p1sol, regions = part1(adj, plants)
print(f"Part 1: {p1sol}")


def count_vert(points: set[point]) -> int:
    counted: set[point] = set()
    count = 0
    while points.difference(counted):
        x, y = points.difference(counted).pop()
        curr_y = y
        while (x, curr_y) in points:
            counted.add((x, curr_y))
            curr_y += 1
        curr_y = y
        while (x, curr_y) in points:
            counted.add((x, curr_y))
            curr_y -= 1
        count += 1
    return count


def count_horiz(points: set[point]) -> int:
    counted: set[point] = set()
    count = 0
    while points.difference(counted):
        x, y = points.difference(counted).pop()
        curr_x = x
        while (curr_x, y) in points:
            counted.add((curr_x, y))
            curr_x += 1
        curr_x = x
        while (curr_x, y) in points:
            counted.add((curr_x, y))
            curr_x -= 1
        count += 1
    return count


def count_sides(neighbors: dict[str, set[point]]) -> int:
    count = 0
    for dir in ["up", "down"]:
        count += count_horiz(neighbors[dir])
    for dir in ["right", "left"]:
        count += count_vert(neighbors[dir])

    return count


p2sol = 0
for region in regions:
    area, perimeter, ids = region
    points = set(map(lambda x: (x % n, x // n), ids))
    neighbors: dict[str, set[point]] = defaultdict(set)
    for x, y in points:
        if (x, y - 1) not in points:
            neighbors["up"].add((x, y - 1))
        if (x + 1, y) not in points:
            neighbors["right"].add((x + 1, y))
        if (x, y + 1) not in points:
            neighbors["down"].add((x, y + 1))
        if (x - 1, y) not in points:
            neighbors["left"].add((x - 1, y))
    sides = count_sides(neighbors)
    p2sol += sides * area

print(f"Part 2: {p2sol}")
