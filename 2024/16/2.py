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

# queue item: score, pos, direction, path taken to cell
q = PriorityQueue()
q.put((0, start_tile, 1, []))

MOVE_COST = 1
ROTATE_COST = 1000

seen_pos: dict[tuple, int] = {}

found = False
best_cost = 0

nice_seats = set()

while not q.empty():
    score, pos, direction, path = q.get()
    i, j = pos

    # check if worth continuing
    if found and score > best_cost:
        continue

    # hit wall
    if lines[i][j] == "#":
        continue

    # if at end, add all cells in path to the nice seats
    if pos == end_tile:
        found = True
        best_cost = score
        for cell in path:
            nice_seats.add(cell)

    # avoid rechecking if it's not better than already seen
    set_key = pos, direction
    if set_key in seen_pos and score > seen_pos[set_key]:
        continue
    seen_pos[set_key] = score

    next_path = path + [pos]

    # add in counter
    counter_clockwise = (direction - 1) % 4
    if counter_clockwise in valid_dirs[i][j]:
        q.put((score + ROTATE_COST, pos, counter_clockwise, next_path))

    # add in counter-clockwise
    clockwise = (direction + 1) % 4
    if clockwise in valid_dirs[i][j]:
        q.put((score + ROTATE_COST, pos, clockwise, next_path))

    # add in move forward
    if direction == 0:
        i -= 1
    if direction == 1:
        j += 1
    if direction == 2:
        i += 1
    if direction == 3:
        j -= 1
    q.put((score + MOVE_COST, (i, j), direction, next_path))


print(len(nice_seats) + 1)

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")