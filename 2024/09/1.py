from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

disk = []

for line in lines:
    for i, c in enumerate(line):

        for _ in range(int(c)):

            if i % 2 == 0:
                disk.append(i//2)
            else:
                disk.append(".")

    i = 0
    j = len(disk)-1

    while i < j:
        while disk[i] != ".":
            i += 1

        while disk[j] == ".":
            j -= 1

        if i >= j:
            break

        disk[i], disk[j] = disk[j], disk[i]

    s = 0

    for i, c in enumerate(disk):
        if c == ".":
            continue

        s += i * c

    print(s)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
