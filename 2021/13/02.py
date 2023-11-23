dots = set()

folding = False

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        if not len(row.replace("\n", "").strip()):
            folding = True
            continue

        if not folding:
            x, y = list(map(int, row.replace("\n", "").split(",")))
            dots.add((x, y))

        if folding:
            desc = row.replace("\n", "").split("=")
            axis = desc[0][-1]
            pos = int(desc[1])
            if axis == "x":
                new_dots = set()
                for x, y in dots:
                    new_x = -abs(x - pos) + pos
                    new_dots.add((new_x, y))
                dots = new_dots
            if axis == "y":
                new_dots = set()
                for x, y in dots:
                    new_y = -abs(y - pos) + pos
                    new_dots.add((x, new_y))
                dots = new_dots

max_x = max(p[0] for p in dots)
max_y = max(p[1] for p in dots)

for y in range(max_y + 1):
    for x in range(max_x + 1):
        print("###" if (x, y) in dots else "   ", end="")
    print()
