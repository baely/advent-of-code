lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))



curr_set = set()

sums = 0

for line in lines:
    if line == "":
        sums += len(curr_set)
        curr_set = set()
        continue

    curr_set |= set(line)

sums += len(curr_set)

print(sums)
