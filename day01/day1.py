from collections import Counter

l1: list[int] = []
l2: list[int] = []

l2counter: Counter[int] = Counter()

with open("input.txt") as f:
    for line in f:
        n1, n2 = line.split()[:2]
        l1.append(int(n1))
        l2.append(int(n2))
        l2counter[int(n2)] += 1

l1.sort()
l2.sort()

zipped = zip(l1, l2)
mapped = map(lambda n: abs(n[0] - n[1]), zipped)
print(f"Part 1: {sum(mapped)}")

sol = 0
for n1 in l1:
    sol += n1 * l2counter[n1]

print(f"Part 2: {sol}")
