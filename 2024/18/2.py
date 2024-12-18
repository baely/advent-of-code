import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

LENGTH = 71

for num_bytes in range(len(lines)):
    grid = [
        ["." for _ in range(LENGTH)] for _ in range(LENGTH)
    ]

    for k, line in enumerate(lines):
        if k >= num_bytes:
            break
        i, j = list(map(int, line.split(",")))
        grid[j][i] = "#"

    search = {(0, 0)}
    seen = set()

    NEIGHBOURS = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]

    k = 0
    while search:
        next_search = set()

        found = False

        for pos in search:
            i, j = pos
            seen.add(pos)

            if (i, j) == (LENGTH - 1, LENGTH - 1):
                found = True
                break

            for di, dj in NEIGHBOURS:
                ni, nj = i + di, j + dj
                if not (0 <= ni < LENGTH and 0 <= nj < LENGTH):
                    continue

                if grid[ni][nj] == "#":
                    continue

                if (ni, nj) in seen:
                    continue

                next_search.add((ni, nj))

        if found:
            break

        search = next_search
        k += 1

    else:
        break


print(num_bytes)
print(lines[num_bytes - 1])

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")