lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l.strip() for l in f.read().split("\n")]
    # nums = list(map(int, lines))

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
        continue

    for j in range(len(match)):
        k = i+j+1
        mults[k] += amt

print(sum(mults))

