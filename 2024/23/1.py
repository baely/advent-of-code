import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

NEIGHBOURS = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

connected_to: dict[str, set[str]] = {}

for i, line in enumerate(lines):
    # for j, c in enumerate(line):
    a, b = line.split("-")

    if a not in connected_to:
        connected_to[a] = set()
    if b not in connected_to:
        connected_to[b] = set()

    connected_to[a].add(b)
    connected_to[b].add(a)


triples: set[tuple] = set()

for a, others in connected_to.items():
    for b in others:
        for c in others:
            if b == c:
                continue

            if c in connected_to[b]:
                l = [a, b, c]
                ll = sorted(l)
                k = tuple(ll)
                triples.add(k)

print(len([
    t for t in triples if any(x.startswith("t") for x in t)
]))

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")