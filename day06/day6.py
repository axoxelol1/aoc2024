input_obstacles: set[tuple[int, int]] = set()
input_guard: tuple[tuple[int, int], tuple[int, int]] = ((0, 0), (0, 1))

with open("input.txt") as f:
    input = f.read().splitlines()
    limit = len(input)
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "#":
                input_obstacles.add((x, limit - 1 - y))
            elif c == "^":
                input_guard = ((x, limit - 1 - y), input_guard[1])

visited: set[tuple[int, int]] = set()


def in_bounds(pos: tuple[int, int], limit: int) -> bool:
    return 0 <= pos[0] < limit and 0 <= pos[1] < limit


guard = input_guard
while in_bounds(guard[0], limit):
    (x, y), (dx, dy) = guard
    visited.add((x, y))
    while (x + dx, y + dy) in input_obstacles:
        temp = dx
        dx = dy
        dy = -temp
    guard = ((x + dx, y + dy), (dx, dy))

print(f"Part 1: {len(visited)}")

visited_in_p1 = visited.copy()

loop_count = 0
for possible_stone in visited_in_p1:
    obstacles = input_obstacles.copy()
    obstacles.add(possible_stone)
    visited_with_dir: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    guard = input_guard
    while in_bounds(guard[0], limit):
        (x, y), (dx, dy) = guard
        if guard in visited_with_dir:
            loop_count += 1
            break
        visited_with_dir.add(guard)
        while (x + dx, y + dy) in obstacles:
            temp = dx
            dx = dy
            dy = -temp
        guard = ((x + dx, y + dy), (dx, dy))

print(f"Part 2: {loop_count}")
