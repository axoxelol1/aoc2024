import re

with open("input.txt", "r") as file:
    input = file.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", input)

part1 = sum(map(lambda t: int(t[0]) * int(t[1]), matches))
print(f"Part 1: {part1}")

matches: list[tuple[str, str, str, str]] = re.findall(
    r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input
)

part2 = 0
curr_do = True
for x, y, do, dont in matches:
    if dont:
        curr_do = False
    elif do:
        curr_do = True
    elif curr_do:
        part2 += int(x) * int(y)
print(f"Part 2: {part2}")
