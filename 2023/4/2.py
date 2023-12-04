lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l.strip() for l in f.read().split("\n")]
    # nums = list(map(int, lines))

pts = []

mults = [1 for _ in lines]

for i, line in enumerate(lines):
    game, nums = line.split(": ")

    amt = mults[i]

    win, mine = nums.split("|")

    wins = [x for x in win.split(" ") if x != ""]
    mines = [x for x in mine.split(" ") if x != ""]

    win_set = set(map(int, wins))
    my_set = set(map(int, mines))

    match = my_set & win_set

    if len(match) == 0:
        pts.append(0)
        continue

    for j in range(len(match)):
        k = i+j+1

        mults[k] += amt

    pt = 2 ** (len(my_set & win_set) - 1)
    pt *= amt
    pts.append(pt)

print(mults)
print(pts)

# 8 2 2 1

print(sum(mults))

