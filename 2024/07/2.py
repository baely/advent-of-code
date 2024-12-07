from time import perf_counter_ns
from functools import cache

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

t = 0

@cache
def perm(s, n) -> list[str]:
    out = []
    for i in range(len(s) ** n):
        o = ""
        x = i
        for k in range(n):
            x, c = divmod(x, len(s))
            o = s[c] + o
        out.append(o)
    return out


for line in lines:
    comp, rest = line.split(": ")
    comp = int(comp)
    rest = list(map(int, rest.split(" ")))

    for p in perm("012", len(rest)-1):

        ts = rest[0]

        for k, op in enumerate(p):
            if op == "0":
                ts += rest[k+1]
            if op == "1":
                ts *= rest[k+1]
            if op == "2":
                ts = int(str(ts) + str(rest[k+1]))

        if ts == comp:
            break
    else:
        continue

    t += comp

print(t)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
