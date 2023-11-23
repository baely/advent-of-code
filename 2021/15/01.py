grid: list[list[int]] = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a = list(map(int, row.replace("\n", "")))
        grid.append(a)

new_grid: list[list[int]] = []

d = len(grid)

last_len = 0

for k in range(2 * d - 1):
    this_diag: list[int] = [
        grid[i][j] for i, j in
        zip(reversed(range(max(0, k - d + 1), min(d - 1, k) + 1)), range(max(0, k - d + 1), min(d - 1, k) + 1))]
    this_len = len(this_diag)

    new_grid.append([0 for _ in this_diag])

    if not last_len:
        pass
    elif this_len > last_len:
        for i, v in enumerate(this_diag):
            if i == 0:
                new_grid[k][i] = new_grid[k - 1][0] + v
            elif i == this_len - 1:
                new_grid[k][i] = new_grid[k - 1][last_len - 1] + v
            else:
                new_grid[k][i] = min(new_grid[k - 1][i - 1], new_grid[k - 1][i]) + v
    elif this_len < last_len:
        for i, v in enumerate(this_diag):
            new_grid[k][i] = min(new_grid[k - 1][i], new_grid[k - 1][i + 1]) + v

    last_len = this_len

print(new_grid[-1][-1])
