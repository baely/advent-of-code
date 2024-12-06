from time import perf_counter_ns
from functools import cmp_to_key


with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

rules = set()

for line in lines:
    if line.strip() == "":
        break

    a, b = line.split("|")
    a, b = int(a), int(b)

    rules.add((a, b))

summids = 0


def valid(ms: list[int]) -> bool:
    invalid = False

    for i, aa in enumerate(ms):
        for bb in ms[i + 1:]:

            if (bb, aa) in rules:
                invalid = True

    return not invalid


def comp(aa: int, bb: int) -> int:
    if (aa, bb) in rules:
        return -1
    if (bb, aa) in rules:
        return 1
    return 0


skip = True
for line in lines:
    if line.strip() == "":
        skip = False
        continue
    if skip:
        continue

    ns = list(map(int, line.split(",")))

    if valid(ns):
        continue

    ns = sorted(ns, key=cmp_to_key(comp))

    summids += ns[len(ns) // 2]

print(summids)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
