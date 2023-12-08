lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

moves = {}

for i, line in enumerate(lines):
    if i < 2:
        continue

    a, l, r = line[0:3], line[7:10], line[12:15]
    moves[a] = (l, r)

curr = "AAA"

c = 0

while True:
    move = lines[0][c % len(lines[0])]
    l, r = moves[curr]

    if move == "L":
        curr = l
    elif move == "R":
        curr = r

    c += 1

    if curr == "ZZZ":
        break

print(c)
