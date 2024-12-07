from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

guard = (0, 0)

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "^":
            guard = (i, j)

MOVES = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

loops = 0

height = len(lines)
width = len(lines[0])
upper_bound = height * width * 4

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if lines[i][j] != ".":
            continue

        lines[i] = lines[i][:j] + "#" + lines[i][j+1:]

        move = 0

        new_guard = guard

        moves = 0

        while 0 <= new_guard[0] < height and 0 <= new_guard[1] < width:
            gi, gj = new_guard

            m = MOVES[move]
            mi, mj = m

            ni, nj = gi + mi, gj + mj

            if not (0 <= ni < height and 0 <= nj < width):
                break

            if lines[ni][nj] == "#":
                move = (move + 1) % 4
                continue

            new_guard = (ni, nj)
            new_k = (new_guard, move)

            moves += 1
            if moves > upper_bound:
                loops += 1
                break

        lines[i] = lines[i][:j] + "." + lines[i][j+1:]


print(loops)


end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
