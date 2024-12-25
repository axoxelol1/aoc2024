gates: list[tuple[int, str, int, int]] = []
line_to_index: dict[str, int] = dict()
lines: list[bool] = []
received: set[int] = set()


with open("input_fixed.txt") as f:
    ls, gs = f.read().split("\n\n")[:2]

    for line in ls.splitlines():
        name, value = line.split(": ")
        if name.strip() not in line_to_index:
            line_to_index[name.strip()] = len(lines)
            received.add(len(lines))
            lines.append(value.strip() == "1")
    for gate in gs.splitlines():
        cond, dest = gate.split(" -> ")[:2]
        a, op, b = cond.split()
        if a not in line_to_index:
            line_to_index[a] = len(lines)
            lines.append(False)
        if b not in line_to_index:
            line_to_index[b] = len(lines)
            lines.append(False)
        if dest not in line_to_index:
            line_to_index[dest] = len(lines)
            lines.append(False)
        gates.append((line_to_index[a], op, line_to_index[b], line_to_index[dest]))

while len(received) < len(lines):
    for i, op, j, k in gates:
        if i not in received or j not in received:
            continue
        if op == "AND":
            lines[k] = lines[i] and lines[j]
        elif op == "OR":
            lines[k] = lines[i] or lines[j]
        elif op == "XOR":
            lines[k] = lines[i] ^ lines[j]
        received.add(k)

z_wires = sorted(
    filter(lambda x: x[0].startswith("z"), line_to_index.items()), reverse=True
)


x_wires = sorted(
    filter(lambda x: x[0].startswith("x"), line_to_index.items()), reverse=True
)
y_wires = sorted(
    filter(lambda x: x[0].startswith("y"), line_to_index.items()), reverse=True
)

x = 0
print("x:  ", end="")
for i, (_, index) in enumerate(x_wires):
    x += lines[index] << len(x_wires) - i - 1
    print(1 if lines[index] else 0, end="")
print()
y = 0
print("y:  ", end="")
for i, (_, index) in enumerate(y_wires):
    y += lines[index] << len(y_wires) - i - 1
    print(1 if lines[index] else 0, end="")
print()
print("z: ", end="")
z = 0
for i, (_, index) in enumerate(z_wires):
    z += lines[index] << len(z_wires) - i - 1
    print(1 if lines[index] else 0, end="")
print()
print(f"Part 1, z={z}")

index_to_line = {v: k for k, v in line_to_index.items()}

for gate in gates:
    a, op, b, dest = gate
    a = index_to_line[a]
    b = index_to_line[b]
    dest = index_to_line[dest]
    if index_to_line[gate[3]].startswith("z"):
        if gate[1] != "XOR":
            print(
                index_to_line[gate[0]],
                gate[1],
                index_to_line[gate[2]],
                "->",
                index_to_line[gate[3]],
            )

# Part 2 was done using graphviz and some print debugging =)

wrong = ["qsb", "z39", "gvm", "z26", "wmp", "z17", "gjc", "qjj"]
wrong.sort()
print(f"Part 2: {','.join(wrong)}")
