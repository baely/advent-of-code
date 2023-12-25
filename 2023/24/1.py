with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

START, END = 200000000000000, 400000000000000

new_lines: list[tuple[tuple, float, float, int]] = []

for line in lines:
    position, velocity = line.split(" @ ")
    px, py, pz = [int(x) for x in position.split(", ")]
    vx, vy, vz = [int(x) for x in velocity.split(", ")]

    m = vy / vx
    c = py - (m * px)

    p = (px, py), m, c, vx
    new_lines.append(p)

intersect = 0

for i, line1 in enumerate(new_lines[:-1]):
    (x1, y1), m1, c1, vx1 = line1
    for line2 in new_lines[i+1:]:
        (x2, y2), m2, c2, vx2 = line2

        if m1 == m2:
            continue

        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1

        if not START <= x <= END:
            continue
        if not START <= y <= END:
            continue

        if vx1 < 0:
            if x > x1:
                continue
        else:
            if x < x1:
                continue
        if vx2 < 0:
            if x > x2:
                continue
        else:
            if x < x2:
                continue

        intersect += 1

print(intersect)
