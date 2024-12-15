import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

grid = []

pos = (0, 0)

for i, line in enumerate(lines):
    line = line.replace("#", "##")
    line = line.replace("O", "[]")
    line = line.replace(".", "..")
    line = line.replace("@", "@.")

    for j, c in enumerate(line):
        if c == "@":
            pos = i, j
            line = line.replace("@", ".")
    if line == "":
        break

    grid.append(line)

skip = True
for line in lines:
    if line == "":
        skip = False
    if skip:
        continue

    for c in line:
        # MOVE RIGHT
        if c == ">":
            i, j = pos
            while grid[i][j] != "#":
                j += 1
                if grid[i][j] == ".":
                    break
            else:
                continue

            pos = pos[0], pos[1] + 1

            # shift boxes
            if pos != (i, j):  # if boxes were in way
                grid[i] = grid[i][:pos[1]] + "." + ("[]" * ((j - pos[1]) // 2)) + grid[i][j+1:]

        # MOVE LEFT
        if c == "<":
            i, j = pos
            while grid[i][j] != "#":
                j -= 1
                if grid[i][j] == ".":
                    break
            else:
                continue

            pos = pos[0], pos[1] - 1

            # shift boxes
            if pos != (i, j):  # if boxes were in way
                grid[i] = grid[i][:j] + ("[]" * ((pos[1] - j) // 2)) + "." + grid[i][pos[1]+1:]


        # MOVE DOWN
        if c == "v":
            i, j = pos
            safe = True
            to_check = [(i + 1, j)]
            shift = set()
            while to_check:
                next_check = to_check.pop()
                ci, cj = next_check
                c = grid[ci][cj]

                if c == "#":
                    safe = False
                    break
                if c == "[":
                    # check below and to right
                    to_check.append((ci + 1, cj))
                    to_check.append((ci + 1, cj + 1))

                    shift.add((ci, cj))
                if c == "]":
                    # check below and to left
                    to_check.append((ci + 1, cj - 1))
                    to_check.append((ci + 1, cj))

                    shift.add((ci, cj -1)) # only shift [
            if not safe:
                continue

            shift = list(shift)
            shift.sort()

            while shift:
                next_ij = shift.pop()
                i, j = next_ij
                grid[i] = grid[i][:j] + ".." + grid[i][j+2:]
                grid[i+1] = grid[i+1][:j] + "[]" + grid[i+1][j+2:]

            pos = pos[0] + 1, pos[1]


        # MOVE UP
        if c == "^":
            i, j = pos
            safe = True
            to_check = [(i - 1, j)]
            shift = set()
            while to_check:
                next_check = to_check.pop()
                ci, cj = next_check
                c = grid[ci][cj]

                if c == "#":
                    safe = False
                    break
                if c == "[":
                    # check below and to right
                    to_check.append((ci - 1, cj))
                    to_check.append((ci - 1, cj + 1))

                    shift.add((ci, cj))
                if c == "]":
                    # check below and to left
                    to_check.append((ci - 1, cj - 1))
                    to_check.append((ci - 1, cj))

                    shift.add((ci, cj -1)) # only shift [
            if not safe:
                continue

            shift = list(shift)
            shift.sort(reverse=True)

            while shift:
                next_ij = shift.pop()
                i, j = next_ij
                grid[i] = grid[i][:j] + ".." + grid[i][j+2:]
                grid[i-1] = grid[i-1][:j] + "[]" + grid[i-1][j+2:]

            pos = pos[0] - 1, pos[1]


total = 0

for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "[":
            total += 100 * i + j

print(total)

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")