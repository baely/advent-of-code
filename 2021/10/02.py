from collections import deque

chunks = []
with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        chunks.append(row.replace("\n", ""))

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]

illegal_c = 0
all_scores = []

for chunk in chunks:
    curr_stack = deque()
    valid = True
    for c in chunk:
        if c in openers:
            curr_stack.append(openers.index(c))
        if c in closers:
            c_index = closers.index(c)
            if c_index == curr_stack[-1]:
                curr_stack.pop()
            else:
                valid = False
                break
    if valid:
        score = 0
        while len(curr_stack) >= 1:
            curr_c = curr_stack.pop()
            score *= 5
            score += curr_c + 1
        all_scores.append(score)

all_scores.sort()

print(all_scores[int((len(all_scores) - 1) / 2)])
