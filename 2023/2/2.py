lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

amts = []

for line in lines:
    game, out = line.split(": ")
    _, game_id = game.split(" ")

    valid = True

    draws = out.split("; ")

    game_color_mins = dict()

    for draw in draws:
        picks = draw.split(", ")

        for pick in picks:
            amt, color = pick.split(" ")

            if color not in game_color_mins:
                game_color_mins[color] = 0

            game_color_mins[color] = max(game_color_mins[color], int(amt))

    this_amt = 1
    for _, v in game_color_mins.items():
        this_amt *= v

    amts.append(this_amt)

print(sum(amts))