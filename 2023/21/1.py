with open("input.txt") as f:
    lines: list[list[str]] = [list(line.strip()) for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start_i, start_j = 0, 0

found = False
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "S":
            start_i = i
            start_j = j
            found = True
            break

    if found:
        break

pos = {(start_i, start_j)}
next_pos = set()

neighbours = [
    (0, -1), (-1, 0), (1, 0), (0, 1)
]

for step in range(64):

    for (i, j) in pos:
        for (di, dj) in neighbours:
            ni, nj = i + di, j + dj
            if not (0 <= ni < len(lines) and 0 <= nj < len(lines[0])):
                continue

            nc = lines[ni][nj]
            if nc == "#":
                continue

            next_pos.add((ni, nj))

    pos = next_pos
    next_pos = set()

print(len(pos))
