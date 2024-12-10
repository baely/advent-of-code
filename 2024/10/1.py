from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

starts = [

]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "0":
            starts.append((i, j))

trailhead_scores = 0

NEIGHBOURS = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

for s in starts:
    this = {s}
    next_step = set()

    while this:
        for i, j in this:
            k = int(lines[i][j])
            if k == 9:
                trailhead_scores += 1
                continue
            for di, dj in NEIGHBOURS:
                ni, nj = i + di, j + dj
                if not (0 <= ni < len(lines) and 0 <= nj < len(lines[0])):
                    continue

                if lines[ni][nj] == ".":
                    continue

                k2 = int(lines[ni][nj])

                if k2 != k + 1:
                    continue

                next_step.add((ni, nj))

        this = next_step
        next_step = set()

print(trailhead_scores)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
