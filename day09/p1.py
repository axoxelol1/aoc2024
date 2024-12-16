from heapq import heappop, heappush

free_ranges: list[tuple[int, int]] = []
file_ranges: list[tuple[int, int, int]] = []
moved_files: list[tuple[int, int, int]] = []

with open("input.txt") as f:
    total_filesize = 0
    line = f.read().strip()
    file = True
    id = 0
    curr_index = 0
    for c in line:
        size = int(c)
        if file:
            file_ranges.append((curr_index, curr_index + size - 1, id))
            id += 1
        else:
            heappush(free_ranges, (curr_index, curr_index + size - 1))
        curr_index += size
        file = not file

while file_ranges:
    start, end, id = file_ranges.pop()
    filesize = end - start + 1
    left = filesize
    while True:
        free_start, free_end = heappop(free_ranges)
        freesize = free_end - free_start + 1
        if start < free_start:
            moved_files.append((start, end, id))
            heappush(free_ranges, (free_start, free_end))
            break
        elif filesize < freesize:
            moved_files.append((free_start, free_start + filesize - 1, id))
            heappush(free_ranges, (free_start + filesize, free_end))
            break
        elif filesize == freesize:
            moved_files.append((free_start, free_end, id))
            break
        else:
            moved_files.append((free_start, free_end, id))
            end -= freesize
            filesize = end - start + 1

sol = 0
for start, end, id in moved_files:
    sol += id * ((end - start + 1) * (start + end) // 2)
print(sol)
