lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

cmds = []

for line in lines:
    op, amt = line.split(" ")
    amt = int(amt)

    cmds += [(op, amt)]

acc = 0

for k in range(len(lines)):

    acc = 0
    i = 0

    visited = set()

    while i < len(cmds):
        visited.add(i)

        op, amt = cmds[i]

        if i == k:
            if op == "jmp":
                op = "nop"
            elif op == "nop":
                op = "jmp"

        if op == "acc":
            acc += amt
            i += 1
        elif op == "jmp":
            i += amt
        elif op == "nop":
            i += 1

        if i in visited:
            break
    else:
        break


print(acc)
