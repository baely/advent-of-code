
with open("input.txt") as f:
    r = list(map(int,f.read().split(",")))

ordered_r = sorted(r)

min_amt = None
x = 0

def triangle_num(x):
    return int((x*x + x) / 2)

for i in range(ordered_r[0], ordered_r[-1] + 1):
    amt = sum(triangle_num(abs(x - i)) for x in ordered_r)
    if min_amt is None or amt < min_amt:
        min_amt = amt
        x = i

print(min_amt, x)
