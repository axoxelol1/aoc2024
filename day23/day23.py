from collections import defaultdict
from itertools import combinations

edges: set[tuple[str, str]] = set()
neighbors: dict[str, set[str]] = defaultdict(set)
nodes: set[str] = set()
with open("input.txt") as f:
    for line in f:
        n1, n2 = line.strip().split("-")
        edges.add((n1, n2))
        edges.add((n2, n1))
        neighbors[n1].add(n2)
        neighbors[n2].add(n1)
        nodes.add(n1)
        nodes.add(n2)

triangles = 0
for n1, n2, n3 in combinations(nodes, 3):
    if not (n1[0] == "t" or n2[0] == "t" or n3[0] == "t"):
        continue
    if (n1, n2) in edges and (n2, n3) in edges and (n3, n1) in edges:
        triangles += 1

print(f"Part 1: {triangles}")

cliques: set[frozenset[str]] = set()
for n1 in nodes:
    clique = set([n1])
    for n2 in nodes:
        if all(n2 in neighbors[n] for n in clique):
            clique.add(n2)
    cliques.add(frozenset(clique))

maximum_clique = sorted(list(max(cliques, key=len)))
print(f"Part 2: {",".join(maximum_clique)}")
