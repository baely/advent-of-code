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


for num, row, col_start, col_end in nums_locs:

    start = max(0, col_start - 1)
    end = min(w - 1, col_end)

    if num == 922:
        pass

    part_num = False

    if row - 1 >= 0:
        for i in range(start, end+1):
            if lines[row - 1][i] != ".":
                part_num = True

    if row + 1 < l:
        for i in range(start, end+1):
            if lines[row + 1][i] != ".":
                part_num = True

    if start < col_start:
        if lines[row][start] != ".":
            part_num = True

    if end == col_end:
        if lines[row][end] != ".":
            part_num = True

    if part_num:
        valid_parts.append(num)


print(sum(valid_parts))
