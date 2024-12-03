with open("input.txt") as f:
    reports: list[list[int]] = []
    for line in f:
        reports.append(list(map(int, line.split())))


def safe(report: list[int]) -> bool:
    asc = (report[1] - report[0]) > 0
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if (asc and diff not in [1, 2, 3]) or (not asc and diff not in [-1, -2, -3]):
            return False
    return True


def safe_p2(report: list[int]) -> bool:
    for i in range(len(report)):
        rep = report[:i] + report[i + 1 :]
        if safe(rep):
            return True
    return False


sol1 = sum(map(safe, reports))
print(f"Part 1: {sol1}")

sol2 = sum(map(safe_p2, reports))
print(f"Part 2: {sol2}")