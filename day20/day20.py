from __future__ import annotations
import rustworkx as rx
from rustworkx.generators import directed_grid_graph
from collections import Counter
from itertools import permutations
from tqdm import tqdm

# file_name, dim = "example.txt", 15
file_name, dim = "input.txt", 141

G: rx.PyDiGraph[int, None] = directed_grid_graph(
    dim, dim, bidirectional=True, multigraph=False
)
start = 0
end = 0

path_nodes: set[int] = set()
walls: set[int] = set()
with open(file_name, "r") as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == "#":
                walls.add(y * dim + x)
                G.remove_node(y * dim + x)
            else:
                path_nodes.add(y * dim + x)
            if c == "S":
                start = y * dim + x
            elif c == "E":
                end = y * dim + x

all_shortest = rx.all_pairs_dijkstra_path_lengths(G, lambda _: 1)
path = rx.dijkstra_shortest_paths(G, start, end)[end]

cheats: Counter[int] = Counter()
for wall in walls:
    path_neighbours: list[int] = []
    x, y = wall % dim, wall // dim
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < dim and 0 <= ny < dim and ny * dim + nx not in walls:
            path_neighbours.append(ny * dim + nx)
    if len(path_neighbours) < 2:
        continue
    for pair in permutations(path_neighbours, 2):
        cheat_length = int(
            (all_shortest[start][pair[0]] if start != pair[0] else 0)
            + (all_shortest[pair[1]][end] if end != pair[1] else 0)
            + 2
        )
        no_cheat = int(all_shortest[start][end])
        cheats[no_cheat - cheat_length] += 1

print(f"Part 1: {sum([v for k, v in sorted(cheats.items()) if k >= 100])}")

p2cheats: Counter[int] = Counter()

for i in tqdm(range(len(path))):
    for j in range(i + 1, len(path)):
        pair = (path[i], path[j])
        bird_path = abs(pair[0] // dim - pair[1] // dim) + abs(
            pair[0] % dim - pair[1] % dim
        )
        if bird_path <= 20:
            cheat_length = int(
                (all_shortest[start][pair[0]] if start != pair[0] else 0)
                + (all_shortest[pair[1]][end] if end != pair[1] else 0)
                + bird_path
            )
            no_cheat = int(all_shortest[start][end])
            p2cheats[no_cheat - cheat_length] += 1

print(f"Part 2: {sum([v for k, v in sorted(p2cheats.items()) if k >= 100])}")
