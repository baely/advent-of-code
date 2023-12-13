lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

all_groups: list[list[str]] = []

curr_group: list[str] = []

for line in lines:
    if line == "":
        all_groups.append(curr_group)
        curr_group = []
        continue

    curr_group.append(line)

all_groups.append(curr_group)

ans = []

for group in all_groups:
    found = False

    # Find row
    for i in range(1, len(group)):
        top_half = group[:i][::-1]
        bottom_half = group[i:]

        for j in range(min(len(top_half), len(bottom_half))):
            if top_half[j] != bottom_half[j]:
                break
        else:
            ans.append(100 * i)
            found = True
            break

    if found:
        continue

    # Transpose
    new_group = [[None for _ in range(len(group))] for _ in range(len(group[0]))]

    for i, r in enumerate(group):
        for j, c in enumerate(r):
            new_group[j][i] = c

    # Find col
    for i in range(1, len(new_group)):
        top_half = new_group[:i][::-1]
        bottom_half = new_group[i:]

        for j in range(min(len(top_half), len(bottom_half))):
            if top_half[j] != bottom_half[j]:
                break
        else:
            ans.append(i)
            found = True
            break

print(sum(ans))



