from heapq import heappush, heappop

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

# This is not great, but first solution that came to me
while file_ranges:
    if not free_ranges:
        break
    free_start, free_end = heappop(free_ranges)
    freesize = free_end - free_start + 1
    for i in reversed(range(len(file_ranges))):
        start, end, id = file_ranges[i]
        filesize = end - start + 1
        if filesize > freesize or start < free_start:
            continue
        _ = file_ranges.pop(i)
        if filesize < freesize:
            moved_files.append((free_start, free_start + filesize - 1, id))
            heappush(free_ranges, (free_start + filesize, free_end))
            heappush(free_ranges, (start, end))
            break
        elif filesize == freesize:
            moved_files.append((free_start, free_end, id))
            heappush(free_ranges, (start, end))
            break

p2sum = 0
moved_files.extend(file_ranges)
for start, end, id in moved_files:
    p2sum += id * ((end - start + 1) * (start + end) // 2)

print(p2sum)
