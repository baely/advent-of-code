max_x, max_y = 0, 0

lines = []

with open("input.txt") as f:

    for row in f.readlines():
        s1, s2 = row.split(" -> ")
        x1, y1 = list(map(int, s1.split(",")))
        x2, y2 = list(map(int, s2.split(",")))

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

        lines.append(((x1, y1), (x2, y2)))

grid = [[0 for x in range(max_y + 1)] for y in range(max_x + 1)]

for line in lines:
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[x1][y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[x][y1] += 1

multiples = sum(sum(1 for c in row if c >= 2) for row in grid)

print(multiples)
