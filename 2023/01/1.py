lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

vals = []

for line in lines:
    n1 = None
    n2 = None
    for c in line:
        if c.isdigit():
            n1 = int(c)
            break

    for c in line[::-1]:
        if c.isdigit():
            n2 = int(c)
            break

    n = n1 * 10 + n2
    vals.append(n)

print(sum(vals))
