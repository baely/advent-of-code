from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

# size, ID
disk_slots: list[tuple[int, int or str]] = []

for line in lines:
    for i, c in enumerate(line):
        c = int(c)
        if i % 2 == 0:
            disk_slots.append((c, i//2))
        else:
            disk_slots.append((c, "."))

    j = len(disk_slots) - 1

    while j > 0:
        i = 0
        while disk_slots[j][1] == ".":
            j -= 1

        no_better = False
        while disk_slots[i][1] != "." or disk_slots[i][0] < disk_slots[j][0]:
            i += 1
            if i >= j:
                no_better = True
                break

        if no_better:
            j -= 1
            continue

        if disk_slots[i][0] == disk_slots[j][0]:
            # perfect match
            disk_slots[i], disk_slots[j] = disk_slots[j], disk_slots[i]

        if disk_slots[i][0] > disk_slots[j][0]:
            # imperfect match
            amt = disk_slots[j][0]
            diff = disk_slots[i][0] - amt

            disk_slots.insert(i, (amt, disk_slots[j][1]))  # move disk space to left-most of empty space
            disk_slots[i+1] = (diff, ".")                          # create empty slot to fill space to next disk space
            disk_slots[j+1] = (amt, ".")                           # replace old slot with empty

    s = 0

    i = -1
    for amt, c in disk_slots:
        for _ in range(amt):
            i += 1
            if c == ".":
                continue
            s += i * c

    print(s)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
