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

        if lines[ni][nj] != "#":
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

        if lines[ni][nj] != "#":
            pq.put((score + 1, (ni, nj)))

THRESHOLD = 100
amt = 0
JUMP = 20

goal = from_start[end] - THRESHOLD

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if (i, j) not in from_start:
            continue

        best_start = from_start[(i, j)]

        for jump in range(JUMP):
            jump = jump + 1
            for a in range(jump):
                b = jump-a
                for di, dj in [
                    (a, -b),
                    (b, a),
                    (-a, b),
                    (-b, -a)
                ]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < len(lines) and 0 <= nj < len(lines[0])):
                        continue

                    if (ni, nj) not in from_end:
                        continue

                    if from_start[(i, j)] + from_end[(ni, nj)] + jump <= goal:
                        amt += 1

print(amt)

end = perf_counter_ns()
t = end - start_time
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")