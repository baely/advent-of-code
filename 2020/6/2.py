lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))



curr_set = set()

sums = 0

new_group = True

for line in lines:
    if line == "":
        sums += len(curr_set)
        curr_set = set()
        new_group = True
        continue

    if new_group:
        curr_set = set(line)
        new_group = False
        continue

    curr_set &= set(line)

sums += len(curr_set)

print(sums)
