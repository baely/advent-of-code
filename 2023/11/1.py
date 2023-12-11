lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))


empty_cols = set([i for i in range(len(lines[0]))])
empty_row = "." * len(lines[0])

i = 0
while i < len(lines):
    line = lines[i]

    for j, c in enumerate(line):
        if c == "#" and j in empty_cols:
            empty_cols.remove(j)

    if all(c == "." for c in line):
        lines.insert(i, empty_row)
        i += 1

    i += 1

for j in sorted(empty_cols, reverse=True):
    for i, row in enumerate(lines):
        strlist = list(row)
        strlist.insert(j, ".")
        lines[i] = "".join(strlist)

points: list[tuple[int, int]] = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            points.append((i, j))

d = []

for m in range(len(points)):
    for n in range(m+1, len(points)):
        mi, mj = points[m]
        ni, nj = points[n]

        dist = abs(mi - ni) + abs(mj - nj)
        d.append(dist)

print(sum(d))
