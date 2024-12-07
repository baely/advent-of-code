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

seen = {guard}

MOVES = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]
move = 0

while 0 <= guard[0] < len(lines) and 0 <= guard[1] < len(lines[1]):
    # try move foward
    gi, gj = guard

    m = MOVES[move]
    mi, mj = m

    ni, nj = gi + mi, gj + mj

    if not (0 <= ni < len(lines) and 0 <= nj < len(lines[1])):
        break

    if lines[ni][nj] == "#":
        move = (move + 1) % 4
        continue

    guard = (ni, nj)
    seen.add(guard)

print(len(seen))

g = lines.copy()
for i, j in seen:
    g[i] = g[i][:j] + "x" + g[i][j+1:]

for x in g:
    print(x)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
