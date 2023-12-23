neighbours = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
]

with open("input.txt") as f:
    lines: list[list[str]] = [list(line.strip()) for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = 0, lines[0].index(".")
end = len(lines) - 1, lines[-1].index(".")

intersections = {start, end}

for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        if lines[i][j] == "#":
            continue
        if sum(1 for mi, mj in neighbours if lines[i+mi][j+mj] != "#") > 2:
            intersections.add((i, j))

connections: dict[tuple[int, int], dict[tuple[int, int], int]] = {
    x: {} for x in intersections
}

for intersection in intersections:
    i, j = intersection
    if intersection is start:
        paths = [(1, start[1])]
    elif intersection is end:
        paths = [(len(lines)-2 , end[1])]
    else:
        paths = [(i+mi,j+mj) for mi, mj in neighbours if lines[i + mi][j + mj] != "#"]

    for path in paths:
        this_set = {intersection}
        while True:
            this_set.add(path)
            pi, pj = path
            next_paths = ((pi+mi,pj+mj) for mi, mj in neighbours if lines[pi + mi][pj + mj] != "#" and (pi+mi,pj+mj) not in this_set)
            path = next(next_paths)
            if path in intersections:
                connections[intersection][path] = len(this_set)
                break


def calculate_len(full_path):
    d = 0
    for i, x in enumerate(full_path):
        if i == len(full_path) - 1:
            continue
        y = full_path[i + 1]
        d += connections[x][y]
    return d


def max_length_to_end(seen: list, conn: tuple[int, int]) -> int:
    this_seen = seen.copy()
    this_seen.append(conn)

    if conn == end:
        d = 0
        for i, x in enumerate(seen):
            y = this_seen[i + 1]
            d += connections[x][y]
        return d

    max_dist = 0

    for other_conn in connections[conn]:
        if other_conn in this_seen:
            continue

        max_dist = max(max_dist, max_length_to_end(this_seen, other_conn))

    return max_dist


print(max_length_to_end([], start))
