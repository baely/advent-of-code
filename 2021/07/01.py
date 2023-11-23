
with open("input.txt") as f:
    r = list(map(int,f.read().split(",")))

ordered_r = sorted(r)

print(ordered_r)

min_amt = None
x = 0

for i in range(ordered_r[0], ordered_r[-1] + 1):
    if i == 2:
        print([abs(x-i) for x in ordered_r])
    amt = sum(abs(x - i) for x in ordered_r)
    if min_amt is None or amt < min_amt:
        min_amt = amt
        x = i

print(min_amt, x)
