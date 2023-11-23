heights: list[list[int]] = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        x = []
        for c in row:
            try:
                p = int(c)
                x.append(p)
            except ValueError:
                pass
        heights.append(x)

neighbours = [
    (0, -1), (-1, 0), (1, 0), (0, 1)
]

dips = []

for i, m in enumerate(heights):
    for j, n in enumerate(m):
        lowest = True
        for neighbour_d in neighbours:
            try:
                neighbour = heights[i + neighbour_d[0]][j + neighbour_d[1]]
                if neighbour <= n:
                    lowest = False
            except IndexError:
                pass
        if lowest:
            dips.append((i, j))

basins = []

for dip in dips:
    basin = []
    to_search = [dip]

    while to_search:
        pos = to_search.pop()
        if pos in basin:
            continue

        basin.append(pos)

        n = heights[pos[0]][pos[1]]

        for neighbour_d in neighbours:
            if 0 <= pos[0] + neighbour_d[0] < len(heights) and 0 <= pos[1] + neighbour_d[1] < len(heights[0]):
                neighbour = heights[pos[0] + neighbour_d[0]][pos[1] + neighbour_d[1]]
                if neighbour > n and neighbour != 9:
                    to_search.append((pos[0] + neighbour_d[0], pos[1] + neighbour_d[1]))

    basins.append(basin)

basin_lengths = sorted(len(x) for x in basins)
print(basin_lengths[-1] * basin_lengths[-2] * basin_lengths[-3])
