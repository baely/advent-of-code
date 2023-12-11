lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

seeds = [int(x) for x in lines[0].split(": ")[1].split()]
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

    for i, seed in enumerate(seeds):
        if moved[i]:
            continue

        if start <= seed < end:
            seeds[i] += delta
            moved[i] = True

print(min(seeds))
