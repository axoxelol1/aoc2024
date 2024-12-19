with open("input.txt") as f:
    patterns, designs = f.read().strip().split("\n\n")
    patterns = set(patterns.split(", "))
    designs = designs.split("\n")

possiblep1 = 0
possiblep2 = 0
for design in designs:
    possibilities = [0] * len(design)
    for i in reversed(range(len(design))):
        if design[i:] in patterns:
            possibilities[i] = 1
        for j in range(i + 1, len(design)):
            if possibilities[j] and design[i:j] in patterns:
                possibilities[i] += possibilities[j]
    if possibilities[0]:
        possiblep1 += 1
    possiblep2 += possibilities[0]

print(possiblep1)
print(possiblep2)
