import math
from functools import cache
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

available = lines[0].split(", ")


@cache
def search(pattern: str) -> int:
    amt = 0

    if pattern == "":
        return 1

    for towel in available:
        if len(towel) > len(pattern):
            continue

        if pattern.startswith(towel):
            amt += search(pattern[len(towel):])

    return amt


possible = 0
for line in lines[2:]:
    possible += search(line.strip())

print(possible)


end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")
