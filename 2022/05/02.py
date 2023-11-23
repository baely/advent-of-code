from collections import deque

STACKS = 9

stacks = [
    deque() for _ in range(STACKS)
]

stacked = False

with open("input.txt") as f:
    r = f.readlines()

    for row in r:
        if row == "\n" or (len(row) > 2 and row[1] == "1"):
            stacked = True
            continue

        if not stacked:
            for i in range(STACKS):
                p = 4 * i + 1
                if len(row) > p and row[p] != " ":
                    stacks[i].appendleft(row[p])

        else:
            instructions = row.split()
            amt, f, t = map(int, [instructions[1], instructions[3], instructions[5]])

            temp_stack = deque()
            for _ in range(amt):
                block = stacks[f - 1].pop()
                temp_stack.append(block)

            temp_stack.reverse()
            stacks[t - 1] += temp_stack

for stack in stacks:
    print(stack[-1], end="")
