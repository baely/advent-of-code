lines: list[str] = None
nums: list[int] = None

neighbours = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

vs: dict[int, set[int]] = {}

i, j = 0, 0

horizontal_lines: set[tuple[int, tuple[int, int]]] = set()
vertical_lines: set[tuple[tuple[int, int], int]] = set()

min_i, max_i, min_j, max_j = 0, 0, 0, 0

for line in lines:
    if line == "":
        break

    _, _, h = line.split()
    n = int("0x"+h[2:7], 0)
    d = h[7]

    if d in ("3", "U"):
        line = ((i - n, i), j)
        vertical_lines.add(line)
        i -= n
    if d in ("0", "R"):
        line = (i, (j, j + n))
        horizontal_lines.add(line)
        j += n
    if d in ("1", "D"):
        line = ((i, i + n), j)
        vertical_lines.add(line)
        i += n
    if d in ("2", "L"):
        line = (i, (j - n, j))
        horizontal_lines.add(line)
        j -= n

    min_i, max_i = min(min_i, i), max(max_i, i)
    min_j, max_j = min(min_j, j), max(max_j, j)

ss = []

for i in range(min_i, max_i + 1):
    intersecting_lines = sorted([
        (xj, (xi1 < i, xi2 > i)) for (xi1, xi2), xj in vertical_lines if xi1 <= i <= xi2
    ], reverse=True)  # Reverse order to that .pop() returns left to right

    sx = 0

    prev_start = None
    while intersecting_lines:
        j, (extends_above, extends_below) = intersecting_lines.pop()
        if extends_above and extends_below:
            if prev_start is not None:
                dist = j - prev_start + 1
                sx += dist
                prev_start = None
            else:
                prev_start = j

        else:
            j2, (ea2, eb2) = intersecting_lines.pop()
            if extends_above ^ ea2:
                if prev_start is not None:
                    dist = j2 - prev_start + 1
                    sx += dist
                    prev_start = None
                else:
                    prev_start = j
            else:
                if prev_start is None:
                    sx += j2 - j + 1

    ss.append(sx)

print(sum(ss))
