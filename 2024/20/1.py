import math
from time import perf_counter_ns

from queue import PriorityQueue

with open("input.txt") as f:
    # lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    lines: list[list[str]] = [list(line.strip()) for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start_time = perf_counter_ns()

start = 0, 0
end = 0, 0

NEIGHBOURS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "S":
            start = i, j
            lines[i][j] = "."
        if c == "E":
            end = i, j
            lines[i][j] = "."


pq = PriorityQueue()

pq.put((0, start))

from_start: dict[tuple[int, int], int] = {}

while not pq.empty():
    score, pos = pq.get()

    if pos in from_start:
        if score >= from_start[pos]:
            continue
    from_start[pos] = score

    i, j = pos
    for di, dj in NEIGHBOURS:
        ni, nj = i + di, j + dj

        if lines[ni][nj] == ".":
            pq.put((score + 1, (ni, nj)))


pq = PriorityQueue()

pq.put((0, end))

from_end: dict[tuple[int, int], int] = {}

while not pq.empty():
    score, pos = pq.get()

    if pos in from_end:
        if score >= from_end[pos]:
            continue
    from_end[pos] = score

    i, j = pos
    for di, dj in NEIGHBOURS:
        ni, nj = i + di, j + dj

        if lines[ni][nj] == ".":
            pq.put((score + 1, (ni, nj)))

THRESHOLD = 100

amt = 0

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c != "#":
            continue

        tfs = from_start.copy()

        fs = min([tfs[(i+di,j+dj)] for di, dj in NEIGHBOURS if (i+di,j+dj) in tfs] or [-1])
        if fs < 0:
            continue

        tfe = from_end.copy()

        fe = min([tfe[(i + di, j + dj)] for di, dj in NEIGHBOURS if (i + di, j + dj) in tfe] or [-1])
        if fe < 0:
            continue

        if fs + fe + 1 < from_start[end] - THRESHOLD:
            amt += 1

print(amt)

end = perf_counter_ns()
t = end - start_time
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")