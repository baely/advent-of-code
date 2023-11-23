pos = [0, 0, 0]

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        direction, amt = list(row.split(" "))
        amt = int(amt)
        if direction == "down":
            pos[2] += amt
        elif direction == "up":
            pos[2] -= amt
        elif direction == "forward":
            pos[1] += amt
            pos[0] += pos[2] * amt

print(pos[0] * pos[1])
