import math

lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

moves = {}

for i, line in enumerate(lines):
    if i < 2:
        continue

    a, l, r = line[0:3], line[7:10], line[12:15]
    moves[a] = (l, r)


starts = [
    k for k in moves.keys() if len(k) == 3 and k[-1] == "A"
]
terminals = [
    k for k in moves.keys() if len(k) == 3 and k[-1] == "Z"
]

passes = []

for start in starts:
    curr = start

    this_terminals = set(terminals)
    seen: set[tuple[str, int]] = set()  # Used to detect infinite loops
    p = []

    c = 0

    while True:
        curr_mod = (curr, c % len(lines[0]))
        if curr_mod in seen:
            break
        seen.add(curr_mod)

        move = lines[0][c % len(lines[0])]
        l, r = moves[curr]

        if move == "L":
            curr = l
        elif move == "R":
            curr = r

        c += 1

        if curr in this_terminals:
            this_terminals.remove(curr)
            p.append(c)

        if not this_terminals:
            break

    passes.append(p)

# Only because the input was forgiving and each "**A" passed through exactly one "**Z"
print(math.lcm(*[x[0] for x in passes]))
