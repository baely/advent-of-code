
with open("input.txt") as f:
    lines = f.readlines()
nums = set(map(int, lines))

GOAL = 2020
for x in nums:
    other = 2020 - x

    if other in nums:
        print(x * other)
        break
