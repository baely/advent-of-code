DIRECTION_MULT = {
    "forward": (0, 1),
    "down": (1, 1),
    "up": (1, -1)
}

pos = [0, 0]

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        direction, amt = list(row.split(" "))
        amt = int(amt)
        pos[DIRECTION_MULT[direction][0]] += DIRECTION_MULT[direction][1] * amt

print(pos[0] * pos[1])
