grid: list[str] = []

with open("input.txt") as f:
    grid = f.read().splitlines()

grid = list(map(lambda x: "..." + x + "...", grid))
n = len(grid[0])
grid = (["." * n] * 3) + grid + (["." * n] * 3)


def count_xmas(grid: list[str]) -> int:
    dirs = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 0), (1, -1), (2, -2), (3, -3)],
    ]

    for dir in dirs.copy():
        opposite = list(map(lambda x: (-x[0], -x[1]), dir))
        dirs.append(opposite)
    count = 0
    for i in range(3, len(grid) - 3):
        for j in range(3, len(grid) - 3):
            if grid[i][j] != "X":
                continue
            for dir in dirs:
                word = ""
                for di, dj in dir:
                    word += grid[i + di][j + dj]
                if word == "XMAS":
                    count += 1
    return count


def count_xmases(grid: list[str]) -> int:
    count = 0
    for i in range(3, len(grid) - 3):
        for j in range(3, len(grid) - 3):
            if grid[i][j] == "A":
                dia1 = (grid[i - 1][j - 1], grid[i + 1][j + 1])
                dia2 = (grid[i - 1][j + 1], grid[i + 1][j - 1])
                correct = [("M", "S"), ("S", "M")]
                if dia1 in correct and dia2 in correct:
                    count += 1
    return count


print(f"Part 1: {count_xmas(grid)}")
print(f"Part 2: {count_xmases(grid)}")
