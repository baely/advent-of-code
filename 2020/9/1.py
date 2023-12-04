lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l.strip() for l in f.read().split()]
    nums = list(map(int, lines))

num = 0

for i, num in enumerate(nums):
    if i < 25:
        continue

    prev = set(nums[i-25:i])

    found = False

    for a in prev:
        r = num - a
        if a == r:
            continue

        if r in prev:
            found = True
            break

    if not found:
        break

print(num)
