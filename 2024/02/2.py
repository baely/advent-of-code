from time import perf_counter

s = perf_counter()

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

safe = 0

for line in lines:
    ll = list(map(int, line.split(" ")))

    nl = [
        ll[:i] + ll[i+1:] for i in range(len(ll))
    ]

    tsafe = 0

    for ml in nl:

        if ml[1] == ml[0]:
            continue

        inc = ml[1] > ml[0]

        for i, n in enumerate(ml):
            if i == 0:
                continue

            m = ml[i-1]

            d, ic = abs(n - m), n > m

            if not (0 < d <= 3) or ic ^ inc:
                break

        else:
            tsafe += 1

    if tsafe > 0:
        safe += 1

e = perf_counter()
print(safe)
print(f"{e - s}")

