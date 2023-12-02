lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

valid_ids = []

for line in lines:
    game, out = line.split(": ")
    print(game)

    _, game_id = game.split(" ")

    valid = True

    draws = out.split("; ")
    for draw in draws:
        picks = draw.split(", ")

        for pick in picks:
            print(pick)
            amt, color = pick.split(" ")

            if int(amt) > maxes[color]:
                valid = False
                break

        if not valid:
            break

    if valid:
        valid_ids.append(int(game_id))

print(sum(valid_ids))