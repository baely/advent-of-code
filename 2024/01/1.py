with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

ll = []
rl = []

for line in lines:
    l, r = line.split()

    ll.append(l)
    rl.append(r)

ll.sort()
rl.sort()

x = 0
for l, r in zip(ll, rl):
    l, r = int(l), int(r)

    x += abs(l - r)

print(x)
