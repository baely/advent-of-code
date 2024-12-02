with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

safe = 0

for line in lines:
    ll = list(map(int, line.split(" ")))
    if ll[1] == ll[0]:
        continue

    inc = ll[1] > ll[0]

    for i, n in enumerate(ll):
        if i == 0:
            continue

        m = ll[i-1]

        d, ic = n - m, n > m

        if not (0 < abs(d) <= 3):
            break

        if (d > 0 and not inc) or (d < 0 and inc):
            break

    else:
        safe += 1


print(safe)