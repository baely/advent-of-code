lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

q = [((0, -1), (0, 1))]
q_seen = set()

energised: set[tuple[int, int]] = set()
energised.add((0, 0))

while q:
    p = q.pop()
    if p in q_seen:
        continue
    q_seen.add(p)
    ((pos_i, pos_j), (vel_i, vel_j)) = p

    new_pos_i = pos_i + vel_i
    new_pos_j = pos_j + vel_j

    if not 0 <= new_pos_i < len(lines) or not 0 <= new_pos_j < len(lines[0]):
        continue

    energised.add((new_pos_i, new_pos_j))

    c = lines[new_pos_i][new_pos_j]

    if c == "/":
        vel_i, vel_j = -vel_j, -vel_i
        q.append(((new_pos_i, new_pos_j), (vel_i, vel_j)))
    elif c == "\\":
        vel_i, vel_j = vel_j, vel_i
        q.append(((new_pos_i, new_pos_j), (vel_i, vel_j)))
    elif (c == "-" and vel_j == 0):
        q.append(((new_pos_i, new_pos_j), (0, 1)))
        q.append(((new_pos_i, new_pos_j), (0, -1)))
    elif (c == "|" and vel_i == 0):
        q.append(((new_pos_i, new_pos_j), (1, 0)))
        q.append(((new_pos_i, new_pos_j), (-1, 0)))
    else:
        q.append(((new_pos_i, new_pos_j), (vel_i, vel_j)))

print(len(energised))
