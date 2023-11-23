from collections import deque

chunks = []
with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        chunks.append(row.replace("\n", ""))

illegals = {
    ")": 3, "]": 57, "}": 1197, ">": 25137
}

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]

illegal_c = 0

for chunk in chunks:
    curr_stack = deque()
    for c in chunk:
        if c in openers:
            curr_stack.append(openers.index(c))
        if c in closers:
            c_index = closers.index(c)
            if c_index == curr_stack[-1]:
                curr_stack.pop()
            else:
                illegal_c += illegals[c]
                break

print(illegal_c)
