import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

COST_A = 3
COST_B = 1

total_cost = 0

while True:
    prize = lines.pop()
    line_b = lines.pop()
    line_a = lines.pop()

    p_x = int(prize.split("X=")[1].split(", Y=")[0]) + 10000000000000
    p_y = int(prize.split("X=")[1].split(", Y=")[1]) + 10000000000000

    a_x = int(line_a.split("X")[1].split(", Y")[0])
    a_y = int(line_a.split("X")[1].split(", Y")[1])
    b_x = int(line_b.split("X")[1].split(", Y")[0])
    b_y = int(line_b.split("X")[1].split(", Y")[1])

    echelon: list[list[int]] = [
        [a_x, b_x, p_x],
        [a_y, b_y, p_y],
    ]

    # reduce 2nd row to 0, ..., ...
    lcm = math.lcm(echelon[0][0], echelon[1][0])
    lm = lcm // echelon[0][0]
    rm = lcm // echelon[1][0]

    echelon[1][0] = rm * echelon[1][0] - lm * echelon[0][0]
    echelon[1][1] = rm * echelon[1][1] - lm * echelon[0][1]
    echelon[1][2] = rm * echelon[1][2] - lm * echelon[0][2]

    # reduce 1st row to ..., 0, ...
    lcm = math.lcm(echelon[0][1], echelon[1][1])
    lm = int(lcm / echelon[0][1])
    rm = int(lcm / echelon[1][1])

    echelon[0][0] = rm * echelon[1][0] - lm * echelon[0][0]
    echelon[0][1] = rm * echelon[1][1] - lm * echelon[0][1]
    echelon[0][2] = rm * echelon[1][2] - lm * echelon[0][2]

    if echelon[0][2] % echelon[0][0] == 0 and echelon[1][2] % echelon[1][1] == 0:
        a_presses = echelon[0][2] / echelon[0][0]
        b_presses = echelon[1][2] / echelon[1][1]

        if a_presses >= 0 and b_presses >= 0:
            cost = int(a_presses * COST_A + b_presses * COST_B)
            total_cost += cost


    if len(lines) == 0:
        break

    lines.pop()


print(total_cost)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
