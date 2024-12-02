with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

ll = []
rl = {}

for line in lines:
    l, r = line.split()

    ll.append(int(l))

    r = int(r)

    if r not in rl:
        rl[r] = 0
    rl[r] += 1

x = 0

for l in ll:
    if l not in rl:
        continue

    x += l * rl[l]

print(x)
