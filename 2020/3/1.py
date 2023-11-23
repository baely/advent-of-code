lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = f.read().split("\n")
    # nums = list(map(int, lines))


pos = 0, 0
delta = 1, 3

h, w = len(lines), len(lines[0])

trees = 0

while pos[0] < h:
    if lines[pos[0]][pos[1]] == "#":
        trees += 1

    pos = pos[0] + delta[0], (pos[1] + delta[1]) % w

print(trees)
