with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

bricks: list[tuple, tuple] = []

for line in lines:
    end_one, end_two = line.split("~")
    x1, y1, z1 = [int(x) for x in end_one.split(",")]
    x2, y2, z2 = [int(x) for x in end_two.split(",")]

    lower_end = min(x1, x2), min(y1, y2), min(z1, z2)
    higher_end = max(x1, x2), max(y1, y2), max(z1, z2)

    bricks.append((lower_end, higher_end))

bricks.sort(key=lambda x: x[0][2])

lowered_bricks: list[tuple[tuple, tuple]] = []


def share_shadow(x, y) -> bool:
    c1 = (y[0][0] <= x[0][0] <= y[1][0])
    c2 = (y[0][0] <= x[1][0] <= y[1][0])
    c3 = (x[0][0] <= y[0][0] <= x[1][0])
    c4 = (x[0][0] <= y[1][0] <= x[1][0])

    c5 = (y[0][1] <= x[0][1] <= y[1][1])
    c6 = (y[0][1] <= x[1][1] <= y[1][1])
    c7 = (x[0][1] <= y[0][1] <= x[1][1])
    c8 = (x[0][1] <= y[1][1] <= x[1][1])

    return any([c1, c2, c3, c4]) and any([c5, c6, c7, c8])


supporting: dict[int, set[int]] = {i: set() for i in range(len(bricks))}
supported: dict[int, set[int]] = {i: set() for i in range(len(bricks))}


for i, brick in enumerate(bricks):
    lower_end, higher_end = brick

    bricks_below = [
        (other_brick, j) for j, other_brick in enumerate(lowered_bricks) if share_shadow(other_brick, brick)
    ]

    highest_point = 0

    if bricks_below:
        highest_point = max(x[0][1][2] for x in bricks_below)
        supporting_bricks = [j for other_brick, j in bricks_below if other_brick[1][2] == highest_point]

        for j in supporting_bricks:
            supporting[j].add(i)
            supported[i].add(j)

    next_height = highest_point + 1
    drop_amount = lower_end[2] - next_height

    new_lower_end = (lower_end[0], lower_end[1], lower_end[2] - drop_amount)
    new_higher_end = (higher_end[0], higher_end[1], higher_end[2] - drop_amount)

    lowered_bricks.append((new_lower_end, new_higher_end))

total_fallen = 0

for i in range(len(bricks)):
    fallen = set()
    q = {i}
    while q:
        j = q.pop()
        fallen.add(j)
        for k in supporting[j]:
            r = supported[k] - fallen
            if not r:
                q.add(k)
    total_fallen += len(fallen) - 1

print(total_fallen)
