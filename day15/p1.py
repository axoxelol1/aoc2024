type point = tuple[int, int]
walls: set[point] = set()
boxes: set[point] = set()
robot: point = (0, 0)

with open("input.txt") as f:
    wh_input, moves = f.read().strip().split("\n\n")
    for y, row in enumerate(wh_input.splitlines()):
        for x, c in enumerate(row.strip()):
            if c == "#":
                walls.add((x, y))
            elif c == "O":
                boxes.add((x, y))
            elif c == "@":
                robot = (x, y)


def print_warehouse(
    boxes: set[point], walls: set[point], robot: point, size: int
) -> None:
    for y in range(size):
        for x in range(size):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("O", end="")
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()


for move in moves:
    if move == "^":
        dx, dy = 0, -1
    elif move == ">":
        dx, dy = 1, 0
    elif move == "v":
        dx, dy = 0, 1
    elif move == "<":
        dx, dy = -1, 0
    else:
        continue

    new_robot = (robot[0] + dx, robot[1] + dy)
    if new_robot in walls:
        continue
    elif new_robot in boxes:
        free_spot = new_robot
        while True:
            free_spot = (free_spot[0] + dx, free_spot[1] + dy)
            if free_spot in walls:
                break
            elif free_spot not in boxes:
                robot = new_robot
                boxes.remove(new_robot)
                boxes.add(free_spot)
                break
    else:
        robot = new_robot

print(f"Part 1: {sum(map(lambda x: x[0] + x[1] * 100, boxes))}")
