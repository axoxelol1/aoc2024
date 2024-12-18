import networkx as nx


# file_name, n = "example.txt", 7
file_name, n = "input.txt", 71
with open(file_name) as f:
    byte_positions = [
        tuple(map(int, line.strip().split(","))) for line in f.readlines()
    ]

graph = nx.grid_2d_graph(n, n)
for i in range(1024):
    if not graph.has_node(byte_positions[i]):
        continue
    graph.remove_node(byte_positions[i])

print(nx.shortest_path_length(graph, (0, 0), (n - 1, n - 1)))

for i in range(1024, len(byte_positions)):
    if not graph.has_node(byte_positions[i]):
        continue
    graph.remove_node(byte_positions[i])
    if not nx.has_path(graph, (0, 0), (n - 1, n - 1)):
        print(byte_positions[i])
        break
