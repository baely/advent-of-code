lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l.strip() for l in f.read().split("\n")]
    # nums = list(map(int, lines))

pts = []

for line in lines:
    game, nums = line.split(": ")

    win, mine = nums.split("|")

    wins = [x for x in win.split(" ") if x != ""]
    mines = [x for x in mine.split(" ") if x != ""]

    win_set = set(map(int, wins))
    my_set = set(map(int, mines))

    match = my_set  & win_set

    if len(match) == 0:
        continue

    pt = 2 ** (len(my_set & win_set) -1)

    pts.append(pt)

print(sum(pts))

