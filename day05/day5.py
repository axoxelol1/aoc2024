from collections import defaultdict

with open("input.txt") as f:
    input1, input2 = f.read().split("\n\n")
    rules: list[str] = input1.split("\n")
    updates: list[list[int]] = list(
        map(lambda x: list(map(int, x.split(","))), input2.split("\n")[:-1])
    )

rule_dict: dict[int, list[int]] = defaultdict(list)
for rule in rules:
    x, y = list(map(int, rule.split("|")))
    rule_dict[x].append(y)


def right_order(update: list[int], rule_dict: dict[int, list[int]]):
    incorrect = False
    for i in range(len(update)):
        x = update[i]
        must_before = rule_dict[x]
        for y in must_before:
            try:
                if update.index(y) < i:
                    incorrect = True
                    break
            except ValueError:
                pass
        if incorrect:
            break
    return not incorrect


sol: int = 0
for update in updates:
    if right_order(update, rule_dict):
        sol += update[len(update) // 2]

print(f"Part 1: {sol}")

sol2 = 0
for update in updates:
    if right_order(update, rule_dict):
        continue
    correct = update.copy()
    while not right_order(correct, rule_dict):
        for i in range(len(correct)):
            x = correct[i]
            must_before = rule_dict[x]
            for y in must_before:
                try:
                    yidx = correct.index(y)
                    if yidx < i:
                        temp = correct[i]
                        correct[i] = correct[yidx]
                        correct[yidx] = temp
                except ValueError:
                    pass
    sol2 += correct[len(correct) // 2]

print(f"Part 2: {sol2}")
