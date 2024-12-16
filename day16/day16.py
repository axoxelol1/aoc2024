from heapq import heappop, heappush
from collections import defaultdict

type node = tuple[int, str]
edges: dict[node, list[tuple[node, int]]] = defaultdict(list)


def get_dir(fr: int, to: int, n: int) -> str:
    diff = to - fr
    if diff == 1:
        return "R"
    if diff == -1:
        return "L"
    if diff == n:
        return "D"
    if diff == -n:
        return "U"
    raise ValueError(f"Invalid diff: {diff}")


n = 0
start = 0
end = 0
with open("input.txt") as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        n = len(line.strip())
        for x, c in enumerate(line.strip()):
            if c == "#":
                continue
            if c == "S":
                start = y * n + x
            if c == "E":
                end = y * n + x
            neighbors: list[int] = []
            for dir in ["U", "R", "D", "L"]:
                for dir2 in ["U", "R", "D", "L"]:
                    if dir == dir2:
                        continue
                    edges[(y * n + x, dir)].append(((y * n + x, dir2), 1000))
            for dx, dy, dir in [(0, 1, "D"), (1, 0, "R"), (-1, 0, "L"), (0, -1, "U")]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and lines[ny][nx] in [".", "S", "E"]:
                    edges[(y * n + x, dir)].append(((ny * n + nx, dir), 1))


dist: dict[node, int] = {}
queue = [
    (0, (start, "R")),
]

dist[(start, "R")] = 0
dist[(start, "L")] = 1000
dist[(start, "U")] = 1000
dist[(start, "D")] = 1000
parents: dict[node, set[node]] = defaultdict(set)
while queue:
    d, u = heappop(queue)
    if d > dist[u]:
        continue
    for v, cost in edges[u]:
        alt = d + cost
        if alt <= dist.get(v, float("inf")):
            dist[v] = alt
            parents[v].add(u)
            heappush(queue, (alt, v))


for dir in ["U", "R", "D", "L"]:
    if (end, dir) in dist:
        print(f"Distance to end from start with direction {dir}: {dist[(end, dir)]}")

best_ids: set[int] = set()

to_visit = [(end, "U")]
while to_visit:
    u, dir = to_visit.pop()
    best_ids.add(u)
    if len(parents[(u, dir)]) == 0:
        continue
    parent_costs: list[int] = []
    for v in parents[(u, dir)]:
        parent_edges = edges[v]
        edge_cost = 0
        for edge in parent_edges:
            if edge[0] == (u, dir):
                edge_cost = edge[1]
                break
        parent_costs.append(edge_cost + dist[v])
    min_cost = min(parent_costs)
    for i, v in enumerate(parents[(u, dir)]):
        if parent_costs[i] == min_cost:
            to_visit.append(v)

print(f"Part 2: {len(best_ids)}")
