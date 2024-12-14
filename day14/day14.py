import sys
from PIL import Image
from functools import reduce

if len(sys.argv) != 2:
    print("Usage: python day14.py <input>")
    sys.exit(1)
file_name = sys.argv[1]
if file_name == "example.txt":
    dims = (11, 7)
else:
    dims = (101, 103)

robots: list[tuple[int, int, int, int]] = list()
with open(file_name) as f:
    for line in f:
        pos, v = line.split()
        x, y = pos[2:].split(",")
        dx, dy = v[2:].split(",")
        robots.append((int(x), int(y), int(dx), int(dy)))

quadrants: list[int] = [0, 0, 0, 0]

for robot in robots:
    x, y, dx, dy = robot
    final_x = (x + 100 * dx) % dims[0]
    final_y = (y + 100 * dy) % dims[1]
    mid_x = dims[0] // 2
    mid_y = dims[1] // 2
    if final_x < mid_x and final_y < mid_y:
        quadrants[0] += 1
    elif final_x > mid_x and final_y < mid_y:
        quadrants[1] += 1
    elif final_x < mid_x and final_y > mid_y:
        quadrants[2] += 1
    elif final_x > mid_x and final_y > mid_y:
        quadrants[3] += 1

print(f"Part 1: {reduce(lambda x, y: x * y, quadrants)}")


for second in range(10000):
    img = Image.new("1", dims)
    robot_coords = set(map(lambda x: (x[0], x[1]), robots))
    for i in range(dims[0]):
        for j in range(dims[1]):
            if (i, j) in robot_coords:
                img.putpixel((i, j), 1)
            else:
                img.putpixel((i, j), 0)
    img.save(f"{second}.png")
    for r in range(len(robots)):
        x, y, dx, dy = robots[r]
        robots[r] = ((x + dx) % dims[0], (y + dy) % dims[1], dx, dy)
