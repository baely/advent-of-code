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
        for neighbour in neighbours:
            if 0 <= i + neighbour[0] < len(heights) and 0 <= j + neighbour[1] < len(heights[0]):
                neigh = heights[i + neighbour[0]][j + neighbour[1]]
                if neigh <= n:
                    lowest = False
        if lowest:
            dips.append(n)

print(sum(dips) + len(dips))
