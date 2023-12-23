neighbours = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
]
movement_slop = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}

with open("input.txt") as f:
    lines: list[list[str]] = [list(line.strip()) for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = 0, lines[0].index(".")
end = len(lines) - 1, lines[-1].index(".")

# print(start, end)


def max_length_to_end(pos: tuple[int, int], seen: set) -> int:
    this_seen = seen.copy()
    this_seen.add(pos)

    pi, pj = pos

    while True:
        # print(pos)
        this_seen.add(pos)
        if pos == end:
            return len(this_seen)
        valid_moves = []
        for next_move in neighbours:
            mi, mj = next_move
            ni, nj = pi + mi, pj + mj
            np = ni, nj
            if np in this_seen:
                continue
            if lines[ni][nj] == "#":
                continue
            if lines[ni][nj] in movement_slop and movement_slop[lines[ni][nj]] != next_move:
                # print(lines[ni][nj], next_move)
                continue
            valid_moves.append(np)

        if len(valid_moves) == 0:
            return 0

        if len(valid_moves) == 1:
            pos = valid_moves[0]
            pi, pj = pos
            continue

        return max([
            max_length_to_end(x, this_seen) for x in valid_moves
        ])


m = max_length_to_end(start, {(-1, start[1])})
print(m - 2)