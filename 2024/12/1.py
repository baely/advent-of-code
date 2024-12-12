from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

# area, perim
regions: dict[tuple[int, int], list[int]] = {
    (i, j): [1, 4] for j in range(len(lines[0])) for i in range(len(lines))
}

region_children: dict[tuple[int, int], list[tuple[int, int]]] = {
    (i, j): [(i, j)] for j in range(len(lines[0])) for i in range(len(lines))
}

region_map: list[list[tuple[int, int]]] = [
    [(i, j) for j in range(len(lines[0]))] for i in range(len(lines))
]

for i, line in enumerate(lines):
    for j, c in enumerate(line):

        for di, dj in [(0, 1), (1, 0)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < len(lines) and 0 <= nj < len(line)):
                continue

            if lines[i][j] != lines[ni][nj]:
                continue
                # collapse

            parent = region_map[i][j]
            other_parent = region_map[ni][nj]

            regions[parent][1] -= 2

            if parent != other_parent:
                regions[parent][0] += regions[other_parent][0]
                regions[parent][1] += regions[other_parent][1]
                region_children[parent] += region_children[other_parent]

                for other_children in region_children[other_parent]:
                    ci, cj = other_children
                    region_map[ci][cj] = parent

                del regions[other_parent]
                del region_children[other_parent]

            region_map[ni][nj] = parent

print(sum(area * perim for area, perim in regions.values()))

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
