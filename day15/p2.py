type point = tuple[int, int]
walls: set[point] = set()
boxes: set[point] = set()
robot: point = (0, 0)

with open("input.txt") as f:
    wh_input, moves = f.read().strip().split("\n\n")
    for y, row in enumerate(wh_input.splitlines()):
        for x, c in enumerate(row.strip()):
            if c == "#":
                walls.add((x * 2, y))
            elif c == "O":
                boxes.add((x * 2, y))
            elif c == "@":
                robot = (x * 2, y)


def print_warehouse(
    boxes: set[point], walls: set[point], robot: point, size: int
) -> None:
    for y in range(size):
        for x in range(size * 2):
            if (x, y) in walls or (x - 1, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("[", end="")
            elif (x - 1, y) in boxes:
                print("]", end="")
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()


def movable_up(
    boxes: set[point], walls: set[point], box: point
) -> tuple[bool, set[point]]:
    if box not in boxes:
        raise ValueError("Box not in boxes")
    x, y = box
    collisions: list[point] = []
    if (x - 1, y - 1) in walls or (x, y - 1) in walls or (x + 1, y - 1) in walls:
        return False, set()
    for i in range(3):
        if (x - 1 + i, y - 1) in boxes:
            collisions.append((x - 1 + i, y - 1))
    if len(collisions) == 0:
        return True, set([box])
    to_move: set[point] = set([box])
    for box in collisions:
        movable, moves = movable_up(boxes, walls, box)
        if not movable:
            return False, set()
        to_move = to_move.union(moves)
    return True, to_move


def movable_down(
    boxes: set[point], walls: set[point], box: point
) -> tuple[bool, set[point]]:
    if box not in boxes:
        raise ValueError("Box not in boxes")
    x, y = box
    collisions: list[point] = []
    if (x - 1, y + 1) in walls or (x, y + 1) in walls or (x + 1, y + 1) in walls:
        return False, set()
    for i in range(3):
        if (x - 1 + i, y + 1) in boxes:
            collisions.append((x - 1 + i, y + 1))
    if len(collisions) == 0:
        return True, set([box])
    to_move: set[point] = set([box])
    for box in collisions:
        movable, moves = movable_down(boxes, walls, box)
        if not movable:
            return False, set()
        to_move = to_move.union(moves)
    return True, to_move


imgnum = 0
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
    if new_robot in walls or (new_robot[0] - 1, new_robot[1]) in walls:
        continue
    elif move == ">" and new_robot in boxes:
        free_x, y = new_robot
        box_xs: list[int] = []
        while True:
            if (free_x, y) in walls:
                break
            if (free_x, y) in boxes:
                box_xs.append(free_x)
            elif (free_x, y) not in boxes and (free_x - 1, y) not in boxes:
                robot = new_robot
                for box_x in box_xs:
                    boxes.remove((box_x, y))
                    boxes.add((box_x + 1, y))
                break
            free_x += 1
    elif move == "<" and (new_robot[0] - 1, new_robot[1]) in boxes:
        free_x, y = new_robot
        box_xs = []
        while True:
            if (free_x, y) in walls or (free_x - 1, y) in walls:
                break
            if (free_x, y) in boxes:
                box_xs.append(free_x)
            elif (free_x, y) not in boxes and (free_x - 1, y) not in boxes:
                robot = new_robot
                for box_x in box_xs:
                    boxes.remove((box_x, y))
                    boxes.add((box_x - 1, y))
                break
            free_x -= 1
    elif move == "^" and (
        new_robot in boxes or (new_robot[0] - 1, new_robot[1]) in boxes
    ):
        if new_robot in boxes:
            box = new_robot
        else:
            box = (new_robot[0] - 1, new_robot[1])
        movable, to_move = movable_up(boxes, walls, box)
        if not movable:
            continue
        robot = new_robot
        new_boxes = map(lambda x: (x[0], x[1] - 1), to_move)
        for box in to_move:
            boxes.remove(box)
        for box in new_boxes:
            boxes.add(box)
    elif move == "v" and (
        new_robot in boxes or (new_robot[0] - 1, new_robot[1]) in boxes
    ):
        if new_robot in boxes:
            box = new_robot
        else:
            box = (new_robot[0] - 1, new_robot[1])
        movable, to_move = movable_down(boxes, walls, box)
        if not movable:
            continue
        robot = new_robot
        new_boxes = map(lambda x: (x[0], x[1] + 1), to_move)
        for box in to_move:
            boxes.remove(box)
        for box in new_boxes:
            boxes.add(box)
    else:
        robot = new_robot

print(f"Part 2: {sum(map(lambda x: x[0] + x[1] * 100, boxes))}")
