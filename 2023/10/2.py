lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

PIPES: dict[str, list[tuple[int, int]]] = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(0, 1), (1, 0)],
}

start = ()

for i, row in enumerate(lines):
    for j, cell in enumerate(row):
        if cell == "S":
            start = i, j

seen = set()

i, j = start
next_pos = start

if lines[i - 1][j] in ("|", "F", "7"):
    next_pos = i - 1, j
elif lines[i][j + 1] in ("-", "J", "7"):
    next_pos = i, j + 1
elif lines[i + 1][j] in ("|", "L", "J"):
    next_pos = i + 1, j
elif lines[i][j - 1] in ("-", "L", "F"):
    next_pos = i, j - 1

while True:
    seen.add(next_pos)

    i, j = next_pos
    pipe = lines[i][j]

    if pipe == "S":
        break

    (delt1_i, delt1_j), (delt2_i, delt2_j) = PIPES[pipe]

    pos1 = i + delt1_i, j + delt1_j
    pos2 = i + delt2_i, j + delt2_j

    if pos1 not in seen:
        next_pos = pos1
        continue

    if pos2 not in seen:
        next_pos = pos2
        continue

c = 0

for i, row in enumerate(lines):
    inside = False
    start_bend = None

    for j, cell in enumerate(row):
        if (i, j) in seen:
            if cell == "|":
                inside = not inside

            if cell in ("L", "F"):
                start_bend = cell

            if cell in ("7", "J"):
                if (start_bend, cell) in (
                    ("L", "7"),
                    ("F", "J")
                ):
                    inside = not inside

                start_bend = None
        else:
            c += inside

print(c)
