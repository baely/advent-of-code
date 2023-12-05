lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

init = [int(x) for x in lines[0].split(": ")[1].split()]

seeds: list[tuple[int, int]] = []

for i in range(len(init)//2):
    start, end = init[i * 2], init[i * 2+1] + init[i * 2]
    seeds.append((start, end))

moved = [False for _ in seeds]

new_map = False

for k, line in enumerate(lines):
    if k == 0:
        continue

    if line == "":
        new_map = True
        continue

    if new_map:
        new_map = False
        moved = [False for _ in seeds]
        continue

    dest, source, r = map(int, line.split())
    start = source
    end = source + r
    delta = dest - source

    cs = seeds.copy()

    for i, (s, e) in enumerate(cs):
        if moved[i]:
            continue

        if s <= start < e:
            a1, a2 = (s, start), (start, e)

            seeds.append(a1)
            moved.append(False)
            seeds[i] = a2

        s, e = seeds[i]

        if s <= end < e:
            a2, a3 = (s, end), (end, e)

            seeds[i] = a2
            seeds.append(a3)
            moved.append(False)

        s, e = seeds[i]

        if start <= s <= e <= end:
            seeds[i] = (s + delta, e + delta)
            moved[i] = True

# Do not ask, I do not know
print(sorted(seeds)[1][0])
