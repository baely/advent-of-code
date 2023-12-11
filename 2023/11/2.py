lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

EXPANSION_FACTOR = 1000000

empty_cols = set([i for i in range(len(lines[0]))])
empty_rows = set()

empty_row = "." * len(lines[0])

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#" and j in empty_cols:
            empty_cols.remove(j)

    if all(c == "." for c in line):
        empty_rows.add(i)

points: list[tuple[int, int]] = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            new_i = i + len([x for x in empty_rows if x < i]) * (EXPANSION_FACTOR - 1)
            new_j = j + len([x for x in empty_cols if x < j]) * (EXPANSION_FACTOR - 1)

            points.append((new_i, new_j))

d = []

lp = len(points)

for m in range(len(points)):
    for n in range(m+1, len(points)):
        mi, mj = points[m]
        ni, nj = points[n]

        dist = abs(mi - ni) + abs(mj - nj)
        d.append(dist)

print(sum(d))

print(sum(sum(abs(points[m][0])+abs() for n in range(m+1,lp))for m in range(lp)))
