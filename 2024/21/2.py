import math
from functools import cache
from itertools import permutations
from time import perf_counter_ns


with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

num_pad: dict[str, tuple[int, int]] = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

dir_pad: dict[str, tuple[int, int]] = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

def validate_num(btn: str, path: str) -> bool:
    if btn == "A" and path.startswith("<<"):
        return False
    if btn == "0" and path.startswith("<"):
        return False
    if btn == "7" and path.startswith("vvv"):
        return False
    if btn == "4" and path.startswith("vv"):
        return False
    if btn == "1" and path.startswith("v"):
        return False
    return True

def validate_dir(btn: str, path: str) -> bool:
    if btn == "A" and path.startswith("<<"):
        return False
    if btn == "^" and path.startswith("<"):
        return False
    if btn == "<" and path.startswith("^"):
        return False
    return True

num_path: dict[tuple[str, str], list[str]] = {}
for a, (ai, aj) in num_pad.items():
    for b, (bi, bj) in num_pad.items():
        moves = ""

        # up, right, down, left
        if bi < ai:
            moves += "^" * (ai - bi)
        if bj > aj:
            moves += ">" * (bj - aj)
        if bi > ai:
            moves += "v" * (bi - ai)
        if bj < aj:
            moves += "<" * (aj - bj)

        all_moves = set("".join(x) for x in permutations(moves))

        # remove in valid
        for moves in list(all_moves):
            if not validate_num(a, moves):
                all_moves.remove(moves)

        k = (a, b)
        num_path[k] = [x + "A" for x in all_moves]

dir_path: dict[tuple[str, str], list[str]] = {}
for a, (ai, aj) in dir_pad.items():
    for b, (bi, bj) in dir_pad.items():
        moves = ""
        # right, down, left, up
        if bj > aj:
            moves += ">" * (bj - aj)
        if bi > ai:
            moves += "v" * (bi - ai)
        if bj < aj:
            moves += "<" * (aj - bj)
        if bi < ai:
            moves += "^" * (ai - bi)

        all_moves = set("".join(x) for x in permutations(moves))
        # remove in valid
        for moves in list(all_moves):
            if not validate_dir(a, moves):
                all_moves.remove(moves)

        k = (a, b)
        dir_path[k] = [x + "A" for x in all_moves]


def map_num(string: str) -> list[str]:
    cell = "A"
    moves = [""]
    next_moves = []
    for c in string:
        possible_moves = num_path[(cell, c)]
        for em in moves:
            for pm in possible_moves:
                next_moves.append(em + pm)
        cell = c
        moves = next_moves
        next_moves = []
    return moves


@cache
def score(this_path: str, depth: int) -> int:
    if depth == 0:
        return len(this_path)

    this_path = "A" + this_path
    s = 0
    for a, b in zip(this_path[:-1], this_path[1:]):
        s += find_shortest(a, b, depth-1)

    # print(this_path, depth, s)
    return s


@cache
def find_shortest(a: str, b: str, depth: int) -> int:
    this_paths = dir_path[a, b]
    min_score = None

    for this_path in this_paths:
        this_score = score(this_path, depth)
        if min_score is None:
            min_score = this_score
        min_score = min(min_score, this_score)

    return min_score

complexities = 0
for line in lines:
    n = int("".join(x for x in line if x.isnumeric()))
    all_num_paths = map_num(line)

    shortest = min(
        score(path, 2) for path in all_num_paths
    )

    complexities += shortest * n

print(complexities)


end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")

