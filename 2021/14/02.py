
rules: dict[tuple[str, str], str] = {}

pairs: dict[tuple[str, str], int] = {}

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

first_last_pair = (base[0], base[-1])

for i, c in enumerate(base):
    if i:
        pair = (base[i-1], c)
        if pair not in pairs:
            pairs[pair] = 0
        pairs[pair] += 1

for k in range(40):
    existing_pairs = pairs.copy()

    for pair, quantity in existing_pairs.items():
        new_c = rules[pair]
        p1 = (pair[0], new_c)
        p2 = (new_c, pair[1])
        if p1 not in pairs:
            pairs[p1] = 0
        if p2 not in pairs:
            pairs[p2] = 0
        pairs[p1] += quantity
        pairs[p2] += quantity
        pairs[pair] -= quantity

counts: dict[str, int] = {first_last_pair[0]: 1}

if first_last_pair[1] not in counts:
    counts[first_last_pair[1]] = 1
else:
    counts[first_last_pair[1]] += 1

for p, v in pairs.items():
    x, y = p
    if x not in counts:
        counts[x] = 0
    if y not in counts:
        counts[y] = 0
    counts[x] += v
    counts[y] += v

for p, v in counts.items():
    counts[p] = int(v / 2)

print(max(counts.values()) - min(counts.values()))
