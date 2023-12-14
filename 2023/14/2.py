lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [list(line.strip()) for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

CYCLES = 1000000000

states: dict[tuple, int] = {}

cycle_period = None

for n in range(CYCLES):
    lt = tuple(tuple(x) for x in lines)
    if lt in states:
        prev = states[lt]
        if cycle_period is None:
            cycle_period = n - prev
        if (CYCLES - n) % cycle_period == 0:
            break
    else:
        states[lt] = n

    for _ in range(4):
        for i in range(len(lines) - 1):
            for j in range(len(lines) - 1 - i):
                line1 = lines[j]
                line2 = lines[j + 1]

                for k, (c1, c2) in enumerate(zip(line1, line2)):
                    if (c1, c2) == (".", "O"):
                        lines[j][k], lines[j+1][k] = lines[j+1][k], lines[j][k]

        # Rotate clockwise
        new_group = [[None for _ in range(len(lines))] for _ in range(len(lines[0]))]

        for i, r in enumerate(lines):
            for j, c in enumerate(r):
                new_group[j][len(r) - i - 1] = c

        lines = new_group

total_load = 0

for i, line in enumerate(lines):
    load = len(lines) - i
    total_load += load * sum([1 for c in line if c == "O"])

print(total_load)
