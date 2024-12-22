import math
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

num_path: dict[tuple[str, str], set[str]] = {}
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
        num_path[k] = all_moves

dir_path: dict[tuple[str, str], set[str]] = {}
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
        dir_path[k] = all_moves


def map_num(string: str) -> str:
    cell = "A"
    moves = [""]
    next_moves = []
    for c in string:
        possible_moves = num_path[(cell, c)]
        for em in moves:
            for pm in possible_moves:
                next_moves.append(em + pm + "A")

        cell = c
        moves = next_moves
        next_moves = []
    return moves

def map_dir(strings: str) -> str:
    alll_moves = []
    for string in strings:
        cell = "A"
        moves = [""]
        next_moves = []
        for c in string:
            possible_moves = dir_path[(cell, c)]
            for em in moves:
                for pm in possible_moves:
                    next_moves.append(em + pm + "A")
            cell = c
            moves = next_moves
            next_moves = []
        alll_moves  += moves
    return alll_moves

complexities = 0
for line in lines:
    n = int("".join(x for x in line if x.isnumeric()))
    line = map_num(line)
    # print(line)
    for _ in range(2):
        line = map_dir(line)
        # print(line)
    ll = min(len(l) for l in line)
    # print(len(line), [x for x in line if len(x) == ll])
    complexity = n * ll
    complexities += complexity
    print(ll, n, complexity)

print(complexities)


end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")

# v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A
# A  <   A > A   <   AA  v <   AA >>  ^ A  v  AA ^ A  v <   AAA >  ^ A
# A      ^   A       ^^        <<       A     >>   A        vvv      A
# A          3                          7          9                 A
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# A  <   A > A  v <<   AA >  ^ AA > A  v  AA ^ A   < v  AAA >  ^ A
# A      ^   A         <<      ^^   A     >>   A        vvv      A
# A          3                      7          9                 A

#            Av<A<AA>>^AAvA<^A>AAvA^A
#            A  v <<   AA >  ^ AA > A

print(map_dir(map_dir("<<^^A")))