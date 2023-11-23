lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

seats = []

for line in lines:
    row = 0

    for i in range(7):
        c = line[i]

        if c == "B":
            row += 2 ** (6-i)

    seat = 0

    for i in range(3):
        c = line[i + 7]

        if c == "R":
            seat += 2 ** (2 - i)

    n = row * 8 + seat

    seats.append(n)

i = min(seats)
m = max(seats)

while i < m:
    if i not in seats:
        print(i)
        break

    i += 1

