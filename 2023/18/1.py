lines: list[str] = None
nums: list[int] = None

neighbours = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

vs: dict[int, set[int]] = {}

i, j = 0, 0

for line in lines:
    if line == "":
        break

    d, n, h = line.split()
    n = int(n)

    if d == "U":
        for k in range(n):
            i -= 1
            if i not in vs:
                vs[i] = set()

            vs[i].add(j)

    if d == "R":
        if i not in vs:
            vs[i] = set()
        for k in range(n):
            j += 1
            vs[i].add(j)
    if d == "D":
        for k in range(n):
            i += 1
            if i not in vs:
                vs[i] = set()

            vs[i].add(j)
    if d == "L":
        if i not in vs:
            vs[i] = set()
        for k in range(n):
            j -= 1
            vs[i].add(j)

mnj = min(min(v) for v in vs.values())
mxj = max(max(v) for v in vs.values())

mni = min(vs.keys())
mxi = max(vs.keys())

grid = [
    ["." for _ in range(mxj - mnj + 1)] for _ in range(mxi - mni + 1)
]

for i, ss in vs.items():
    for j in ss:
        adji = i - mni
        adjj = j - mnj

        grid[adji][adjj] = "#"

outside = set()
new_outside = set()

for i in range(len(grid)):
    if grid[i][0] == ".":
        new_outside.add((i, 0))
    if grid[i][-1] == ".":
        new_outside.add((i, len(grid[0])-1))

for j in range(len(grid[0])):
    if grid[0][j] == ".":
        new_outside.add((0, j))
    if grid[-1][j] == ".":
        new_outside.add((len(grid)-1, j))

while new_outside:
    k = new_outside.pop()
    i, j = k
    outside.add(k)

    for di, dj in neighbours:
        ni, nj = i + di, j + dj
        nk = (ni, nj)
        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            continue

        if nk not in outside | new_outside:
            if grid[ni][nj] == ".":
                new_outside.add(nk)

# Size of grid - num of "outside" cells
print(((mxi - mni + 1) * (mxj - mnj + 1)) - len(outside))
