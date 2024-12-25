import math
from time import perf_counter_ns

with open("input.txt") as f:
    schematics: list[str] = [line.strip() for line in f.read().strip().split("\n\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

locks = []
keys = []

for schematic in schematics:
    lines = schematic.split("\n")

    key = True
    if all(x == "." for x in lines[0]):
        key = False

    cols = [-1 for _ in range(len(lines[0]))]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                cols[j] += 1

    if key:
        keys.append(cols)
    else:
        locks.append(cols)

fit = 0

for key in keys:
    for lock in locks:
        if any(a + b > 5 for a, b in zip(key, lock)):
            continue

        fit += 1

print(fit)

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")