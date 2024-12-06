from time import perf_counter_ns

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

skip = True
for line in lines:
    if line.strip() == "":
        skip = False
        continue
    if skip:
        continue

    ns = list(map(int, line.split(",")))

    invalid = False

    for i, a in enumerate(ns):
        for b in ns[i+1:]:

            if (b, a) in rules:
                invalid = True

    if not invalid:
        summids += ns[len(ns) // 2]

print(summids)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
