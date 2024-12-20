from __future__ import annotations
import rustworkx as rx
from rustworkx.generators import directed_grid_graph
from collections import Counter

# file_name, dim = "example.txt", 15
file_name, dim = "input.txt", 141

G: rx.PyDiGraph[int, None] = directed_grid_graph(
    dim, dim, bidirectional=True, multigraph=False
)
start = 0
end = 0

path_nodes: set[int] = set()
with open(file_name, "r") as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == "#":
                G.remove_node(y * dim + x)
            else:
                path_nodes.add(y * dim + x)
            if c == "S":
                start = y * dim + x
            elif c == "E":
                end = y * dim + x

start_to_n = rx.dijkstra_shortest_path_lengths(G, start, lambda _: 1)
end_to_n = rx.dijkstra_shortest_path_lengths(G, end, lambda _: 1)

path = rx.dijkstra_shortest_paths(G, start, end)[end]


p1cheats: int = 0
for i in range(len(path)):
    x, y = path[i] % dim, path[i] // dim
    for dx, dy in [
        (0, 2),
        (2, 0),
        (0, -2),
        (-2, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]:
        if x + dx < 0 or x + dx >= dim or y + dy < 0 or y + dy >= dim:
            continue
        endid = (y + dy) * dim + x + dx
        if endid not in path_nodes:
            continue
        cheat_length = int(
            (start_to_n[path[i]] if path[i] != start else 0)
            + (end_to_n[endid] if endid != end else 0)
            + 2
        )
        if len(path) - cheat_length >= 100:
            p1cheats += 1

print(f"Part 1: {p1cheats}")

p2cheats: int = 0
for i in range(len(path)):
    x, y = path[i] % dim, path[i] // dim
    cheat_ends: set[tuple[int, int]] = set()
    for d in range(2, 21):
        for dx in range(-d, d + 1):
            for dy_sign in [-1, 1]:
                dy = (d - abs(dx)) * dy_sign
                if x + dx < 0 or x + dx >= dim or y + dy < 0 or y + dy >= dim:
                    continue
                if (y + dy) * dim + x + dx not in path_nodes:
                    continue
                cheat_ends.add((((y + dy) * dim + x + dx), d))
    for endid, d in cheat_ends:
        cheat_length = int(
            (start_to_n[path[i]] if path[i] != start else 0)
            + (end_to_n[endid] if endid != end else 0)
            + d
        )
        if len(path) - cheat_length >= 100:
            p2cheats += 1

print(f"Part 2: {p2cheats}")
