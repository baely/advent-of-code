from time import perf_counter_ns

start = perf_counter_ns()

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))


xmas_count = 0

LETTERS = "XMAS"
NEIGHBOURS = [
    (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
]


for i, line in enumerate(lines):
    for j, c in enumerate(line):
        for di, dj in NEIGHBOURS:
            ni, nj = i, j
            nc = c
            for k, xc in enumerate(LETTERS):
                if nc != xc:
                    break

                if nc == "S":
                    continue

                # move
                ni += di
                nj += dj
                if not (0 <= ni < len(lines)):
                    break
                if not (0 <= nj < len(line)):
                    break

                nc = lines[ni][nj]
            else:
                xmas_count += 1

print(xmas_count)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
