from time import perf_counter_ns


with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

t = 0

for line in lines:
    comp, rest = line.split(": ")
    comp = int(comp)
    rest = list(map(int, rest.split(" ")))

    for i in range(2**(len(rest)-1)):
        n = bin(i)[2:].zfill(len(rest)-1)

        ts = rest[0]

        for k, op in enumerate(n):
            if op == "0":
                ts += rest[k+1]
            if op == "1":
                ts *= rest[k+1]

        if ts == comp:
            break
    else:
        continue

    t += comp

print(t)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
