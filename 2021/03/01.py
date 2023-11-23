n = "000000000000"
z = "000000000000"

with open("input.txt") as f:
    nrows = len(f.readlines())

counts = {}

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        for i, p in enumerate(row):
            if (i, p) not in counts:
                counts[(i, p)] = 0
            counts[(i, p)] += 1

for k, v in counts.items():
    print(k, v)
    print(v > (nrows / 2))
    print(n[:k[0]] + "..." + n[k[0]+1:])
    if v > (nrows / 2):
        n = n[:k[0]] + k[1] + n[k[0]+1:]
    else:
        z = z[:k[0]] + k[1] + z[k[0] + 1:]

gamma = int(n, 2)
eps = int(z, 2)

print(gamma * eps)
