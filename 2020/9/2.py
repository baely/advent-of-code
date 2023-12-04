lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
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

for i, n in enumerate(nums):
    s = 0
    xs = []
    j = i

    while s < num:
        s += nums[j]
        xs.append(nums[j])
        j += 1

    if s == num:
        print(min(xs) + max(xs))
        break
