import numpy as np

keys = []
locks = []
with open("input.txt") as f:
    objs = f.read().split("\n\n")
    for obj in objs:
        rows = obj.strip().split("\n")
        key = rows[0][0] == "#"
        ob: list[list[int]] = []
        for row in rows:
            r: list[int] = []
            for c in row.strip():
                if c == "#":
                    r.append(1)
                else:
                    r.append(0)
            ob.append(r)
        arr = np.array(ob)
        if key:
            keys.append(arr)
        else:
            locks.append(arr)

p1 = 0
for key in keys:
    for lock in locks:
        if (key + lock < 2).all():
            p1 += 1
print("Part 1:", p1)
