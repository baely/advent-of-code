lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [list(line.strip()) for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

for i in range(len(lines) - 1):
    for j in range(len(lines) - 1 - i):
        line1 = lines[j]
        line2 = lines[j + 1]

        for k, (c1, c2) in enumerate(zip(line1, line2)):
            if (c1, c2) == (".", "O"):
                lines[j][k], lines[j+1][k] = lines[j+1][k], lines[j][k]

total_load = 0

for i, line in enumerate(lines):
    load = len(lines) - i
    total_load += load * sum([1 for c in line if c == "O"])

print(total_load)
