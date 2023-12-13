lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

possibilites = []

for line in lines:

    row, record = line.split()
    records = [int(x) for x in record.split(",")]

    wiggle_room = len(row) - sum(records) - len(records) + 2

    possible = 0

    for n in range(wiggle_room ** len(records)):
        valid = True
        preceding_operational = [0 for _ in records]
        k = n
        for i in range(len(records)):
            j = len(records) - i - 1
            k, r = divmod(k, wiggle_room)
            preceding_operational[j] = r

        if sum(preceding_operational) >= wiggle_room:
            continue

        pat = ".".join("." * n_prec + "#" * n_damaged for n_prec, n_damaged in zip(preceding_operational, records))
        pat += "." * (len(row) - len(pat))

        for c1, c2 in zip(row, pat):
            if c1 == "?":
                continue

            if c1 != c2:
                valid = False
                break

        if not valid:
            continue

        possible += 1

    possibilites.append(possible)

print(sum(possibilites))
