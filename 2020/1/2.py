
with open("input.txt") as f:
    lines = f.readlines()
nums = set(map(int, lines))

GOAL = 2020
for x in nums:
    other = GOAL - x

    for y in nums:
        if y is x:
            continue

        other2 = other - y

        if other2 in nums:
            print(x * y * other2)
            break
