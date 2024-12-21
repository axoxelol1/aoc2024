from __future__ import annotations
from functools import cache
from itertools import pairwise
import rustworkx as rx

numpad_graph: rx.PyDiGraph[str, str] = rx.PyDiGraph()
numpad_nodes: dict[str, int] = {}

for num_button in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]:
    id = numpad_graph.add_node(num_button)
    numpad_nodes[num_button] = id

for k1, k2 in [
    ("0", "2"),
    ("A", "3"),
    ("1", "4"),
    ("2", "5"),
    ("3", "6"),
    ("4", "7"),
    ("5", "8"),
    ("6", "9"),
]:
    _ = numpad_graph.add_edge(numpad_nodes[k1], numpad_nodes[k2], "^")
    _ = numpad_graph.add_edge(numpad_nodes[k2], numpad_nodes[k1], "v")

for k1, k2 in [
    ("0", "A"),
    ("1", "2"),
    ("2", "3"),
    ("4", "5"),
    ("5", "6"),
    ("7", "8"),
    ("8", "9"),
]:
    _ = numpad_graph.add_edge(numpad_nodes[k1], numpad_nodes[k2], ">")
    _ = numpad_graph.add_edge(numpad_nodes[k2], numpad_nodes[k1], "<")

dir_nodes: dict[str, int] = {}
dir_graph: rx.PyDiGraph[str, str] = rx.PyDiGraph()
for dir_button in ["v", "<", "^", ">", "A"]:
    id = dir_graph.add_node(dir_button)
    dir_nodes[dir_button] = id

for k1, k2 in [("v", "^"), (">", "A")]:
    _ = dir_graph.add_edge(dir_nodes[k1], dir_nodes[k2], "^")
    _ = dir_graph.add_edge(dir_nodes[k2], dir_nodes[k1], "v")

for k1, k2 in [("<", "v"), ("v", ">"), ("^", "A")]:
    _ = dir_graph.add_edge(dir_nodes[k1], dir_nodes[k2], ">")
    _ = dir_graph.add_edge(dir_nodes[k2], dir_nodes[k1], "<")

numpad_paths = rx.all_pairs_all_simple_paths(numpad_graph)
dir_paths = rx.all_pairs_all_simple_paths(dir_graph)


with open("input.txt") as f:
    codes = list(map(lambda x: x.strip(), f.read().split("\n")[:-1]))


@cache
def shortest(start: str, end: str, depth: int, max_depth: int) -> int:
    if depth == 0:
        sums: list[int] = []
        for path in numpad_paths[numpad_nodes[start]][numpad_nodes[end]]:
            parent_buttons: list[str] = []
            parent_buttons.append("A")
            for a, b in pairwise(path):
                parent_buttons.append(numpad_graph.get_edge_data(a, b))
            parent_buttons.append("A")
            sum = 0
            for a, b in pairwise(parent_buttons):
                sum += shortest(a, b, depth + 1, max_depth)
            sums.append(sum)
        return min(sums)
    if depth == max_depth:
        return 1
    sums = []
    if start == end:
        return 1
    for path in dir_paths[dir_nodes[start]][dir_nodes[end]]:
        parent_buttons = []
        parent_buttons.append("A")
        for a, b in pairwise(path):
            parent_buttons.append(dir_graph.get_edge_data(a, b))
        parent_buttons.append("A")
        sum = 0
        for a, b in pairwise(parent_buttons):
            sum += shortest(a, b, depth + 1, max_depth)
        sums.append(sum)
    return min(sums)


p1sol = 0
for code in codes:
    m1 = shortest("A", code[0], 0, 3)
    m2 = shortest(code[0], code[1], 0, 3)
    m3 = shortest(code[1], code[2], 0, 3)
    m4 = shortest(code[2], code[3], 0, 3)
    p1sol += (m1 + m2 + m3 + m4) * int(code[:3])

print(p1sol)

p2sol = 0
for code in codes:
    m1 = shortest("A", code[0], 0, 26)
    m2 = shortest(code[0], code[1], 0, 26)
    m3 = shortest(code[1], code[2], 0, 26)
    m4 = shortest(code[2], code[3], 0, 26)
    p2sol += (m1 + m2 + m3 + m4) * int(code[:3])

print(p2sol)
