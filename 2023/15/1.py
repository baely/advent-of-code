parts: list[str] = []
nums: list[int] = []

with open("input.txt") as f:
    parts = [line.strip() for line in f.read().strip().split(",")]
    # nums = list(map(int, lines))

results = []

for part in parts:
    print(part)

    h = 0

    for c in part:
        v = ord(c)
        h += v
        h *= 17
        h %= 256

    results.append(h)

print(sum(results))
