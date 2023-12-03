lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

curr_num = ""

# number, row, start col, end col
nums_locs: list[tuple[int, int, int, int]] = []

l, w = len(lines), len(lines[0])

for i, line in enumerate(lines):
    curr_num = ""
    curr_start = None
    for j, c in enumerate(line):
        if c.isdigit():
            curr_num += c
            if curr_start is None:
                curr_start = j
        else:
            if curr_num != "":
                curr_num = int(curr_num)
                nums_locs.append((curr_num, i, curr_start, j))
                curr_num = ""
                curr_start = None
    else:
        if curr_num != "":
            curr_num = int(curr_num)
            nums_locs.append((curr_num, i, curr_start, j+1))
            curr_num = ""
            curr_start = None

valid_parts = []

potential_gears: dict[tuple[int, int], list[int]] = dict()


def add_pg(x: int, y: int, num2: int):
    t = (x, y)
    if t not in potential_gears:
        potential_gears[t] = []

    potential_gears[t].append(num2)


for i, (num, row, col_start, col_end) in enumerate(nums_locs):
    start = max(0, col_start - 1)
    end = min(w - 1, col_end)

    if num == 922:
        pass

    if row - 1 >= 0:
        for i in range(start, end+1):
            if lines[row - 1][i] == "*":
                add_pg(row-1, i, num)

    if row + 1 < l:
        for i in range(start, end+1):
            if lines[row + 1][i] == "*":
                add_pg(row+1, i, num)

    if start < col_start:
        if lines[row][start] == "*":
            add_pg(row, start, num)

    if end == col_end:
        if lines[row][end] == "*":
            add_pg(row, end, num)

ratios = []

for part in potential_gears.values():
    if len(part) != 2:
        continue

    x, y = part
    ratios.append(x * y)

print(sum(ratios))
