with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

head, tail = (0, 0), (0, 0)

moves = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}

tail_seen = set()

def update_tail(mv: tuple[int, int]):
    global head, tail
    head_x, head_y = head
    tail_x, tail_y = tail

    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        # tail = head - mv
        tail = (head[0] - mv[0], head[1] - mv[1])

    tail_seen.add(tail)

for line in lines:
    move, amt = line.split(" ")
    amt = int(amt)

    for i in range(amt):
        m = moves[move]
        head = (head[0] + m[0], head[1] + m[1])
        update_tail(m)

print(len(tail_seen))
