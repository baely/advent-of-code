import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

grid = []

pos = (0, 0)

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "@":
            pos = i, j
            line = line.replace("@", ".")
    if line == "":
        break

    grid.append(line)

# for line in grid:
#     print(line)

skip = True
for line in lines:
    if line == "":
        skip = False
    if skip:
        continue

    for c in line:
        i, j = pos
        while grid[i][j] != "#":
            if c == ">":
                j += 1
            if c == "v":
                i += 1
            if c == "<":
                j -= 1
            if c == "^":
                i -= 1

            if grid[i][j] == ".":
                break

        else:
            # condition hits if found wall so stop trying.
            continue


        # safe to move pos
        if c == ">":
            pos = pos[0], pos[1] + 1
        if c == "v":
            pos = pos[0] + 1, pos[1]
        if c == "<":
            pos = pos[0], pos[1] - 1
        if c == "^":
            pos = pos[0] - 1, pos[1]

        # I, J is next .  if not same then there were same walls. swap wall with curr
        if pos != (i, j):
            grid[pos[0]] = grid[pos[0]][:pos[1]] + "." + grid[pos[0]][pos[1]+1:]
            grid[i] = grid[i][:j] + "O" + grid[i][j+1:]


total = 0

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "O":
            total += 100 * i + j

print(total)

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")