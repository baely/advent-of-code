from time import perf_counter_ns

start = perf_counter_ns()

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))


xmas_count = 0

POSSIBLE_ARRANGEMENTS = {
    "MMASS",
    "MSAMS",
    "SMASM",
    "SSAMM",
}


for i, line in enumerate(lines):
    if i == 0 or i == len(lines) - 1:
        continue
    for j, c in enumerate(line):
        if j == 0 or j == len(line) - 1:
            continue

        s = lines[i-1][j-1] + lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1] + lines[i+1][j+1]
        if s in POSSIBLES:
            xmas_count += 1


print(xmas_count)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
