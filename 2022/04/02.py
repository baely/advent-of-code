counts = 0

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a, b = list(row.split(","))
        a_min, a_max = map(int, a.split("-"))
        b_min, b_max = map(int, b.split("-"))

        if a_min <= b_min <= a_max:
            counts += 1

        elif b_min <= a_min <= b_max:
            counts += 1

print(counts)
