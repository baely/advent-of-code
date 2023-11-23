grid: list[list[int]] = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a = list(map(int, row.replace("\n", "")))
        grid.append(a)

d = len(grid)

grid = [[(((i // d) + (j // d)) + grid[i % d][j % d] - 1) % 9 + 1 for j in range(5 * d)] for i in range(5 * d)]
new_grid: list[list[int]] = [[-1 for _ in row] for row in grid]

d = 5 * d

last_len = 0

neighbour_deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]

new_grid[0][0] = 0

for p in range(d ** 2):
    changed = 0
    for i in range(d):
        for j in range(d):
            neighbours = [new_grid[i + x][j + y] + grid[i][j] for x, y in neighbour_deltas if 0 <= i + x < d and 0 <= j + y < d and new_grid[i + x][j + y] >= 0]
            if neighbours:
                if min(neighbours) < new_grid[i][j] or new_grid[i][j] < 0:
                    changed += 1
                    new_grid[i][j] = min(neighbours)

    if not changed:
        break

print(new_grid[-1][-1])
