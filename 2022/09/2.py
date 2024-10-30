with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

head, tail = (0, 0), (0, 0)

ROPE_LENGTH = 10
parts = [
    (0, 0) for _ in range(ROPE_LENGTH)
]

moves = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}

tail_seen = set()

def update_tail(k: int):
    global parts
    head_x, head_y = parts[k - 1]
    tail_x, tail_y = parts[k]

    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        mm = (
            1 if head_x > tail_x else -1 if head_x < tail_x else 0,
            1 if head_y > tail_y else -1 if head_y < tail_y else 0,
        )

        parts[k] = (parts[k][0] + mm[0], parts[k][1] + mm[1])

    if k == ROPE_LENGTH - 1:
        tail_seen.add(parts[k])


for lc, line in enumerate(lines):
    move, amt = line.split(" ")
    amt = int(amt)

    for _ in range(amt):
        m = moves[move]
        parts[0] = (parts[0][0] + m[0], parts[0][1] + m[1])
        for j in range(1, ROPE_LENGTH):
            update_tail(j)

print(len(tail_seen))
