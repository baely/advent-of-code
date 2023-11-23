
rules: dict[tuple[str, str], str] = {}

with open("input.txt") as f:
    base = f.readline().replace("\n", "")
    f.readline()
    r = f.readlines()
    for row in r:
        row2 = row.replace("\n", "")
        n1 = row2[0]
        n2 = row2[1]
        o = row2[6]
        rules[(n1, n2)] = o

for k in range(10):
    new_base = ""

    for i, c in enumerate(base):
        if i:
            new_base += rules[(base[i - 1], c)]

        new_base += c

    base = new_base

counts: dict[str, int] = {}

for c in base:
    if c not in counts:
        counts[c] = 0
    counts[c] += 1


print(max(counts.values()) - min(counts.values()))
