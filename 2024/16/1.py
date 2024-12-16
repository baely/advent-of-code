import math
from time import perf_counter_ns

from queue import PriorityQueue

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

start_tile = 0, 0
end_tile = 0, 0

valid_dirs: list[list[set[int]]] = [
    [set() for _ in range(len(lines[0]))] for _ in range(len(lines))
]

NEIGHBOURS = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "S":
            start_tile = i, j
        if c == "E":
            end_tile = i, j

        if c != "#":
            for d, (di, dj) in enumerate(NEIGHBOURS):
                ni, nj = i + di, j + dj
                if lines[ni][nj] != "#":
                    valid_dirs[i][j].add(d)

# queue item: score, pos, direction
q = PriorityQueue()

q.put((0, start_tile, 1))

MOVE_COST = 1
ROTATE_COST = 1000

seen_pos = set()

while not q.empty():
    score, pos, direction = q.get()
    i, j = pos

    set_key = pos, direction
    if set_key in seen_pos:
        continue

    seen_pos.add(set_key)

    if lines[i][j] == "#":
        continue

    if pos == end_tile:
        print(score)
        break

    # add in counter
    counter_clockwise = (direction - 1) % 4
    if counter_clockwise in valid_dirs[i][j]:
        q.put((score + ROTATE_COST, pos, counter_clockwise))

    # add in counter-clockwise
    clockwise = (direction + 1) % 4
    if clockwise in valid_dirs[i][j]:
        q.put((score + ROTATE_COST, pos, (direction + 1) % 4))

    # add in move forward
    if direction == 0:
        i -= 1
    if direction == 1:
        j += 1
    if direction == 2:
        i += 1
    if direction == 3:
        j -= 1
    q.put((score + MOVE_COST, (i, j), direction))


end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")