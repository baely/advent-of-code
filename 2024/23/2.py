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


def all_selections(ll: list) -> list[list]:
    k = 2 ** len(ll)
    al = []
    for n in range(k):
        tl = []
        for i, x in enumerate(ll):
            if n & (1 << i) > 0:
                tl.append(x)
        al.append(tl)
    return al


connection_counts: dict[str, int] = {}

for a, others in connected_to.items():
    combos = all_selections(list(others))

    for cc in combos:
        cc = cc + [a]
        cc.sort()
        k = ",".join(cc)
        if k not in connection_counts:
            connection_counts[k] = 0
        connection_counts[k] += 1

print(sorted(connection_counts.items(), key=lambda x: x[1], reverse=True)[0][0])
end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision // 3]
print(f"duration: {t / 10 ** precision:.3f}{unit}")
