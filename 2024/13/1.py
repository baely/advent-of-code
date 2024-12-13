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

    p_x = int(prize.split("X=")[1].split(", Y=")[0])
    p_y = int(prize.split("X=")[1].split(", Y=")[1])
    p = p_x, p_y
    p_m = p_y / p_x

    a_x = int(line_a.split("X")[1].split(", Y")[0])
    a_y = int(line_a.split("X")[1].split(", Y")[1])
    b_x = int(line_b.split("X")[1].split(", Y")[0])
    b_y = int(line_b.split("X")[1].split(", Y")[1])

    c = 0, 0

    moves_a = 0
    moves_b = 0
    while c != p:
        m_a = c[0] + a_x, c[1] + a_y
        m_b = c[0] + b_x, c[1] + b_y

        m_a_m = m_a[1] / m_a[0]
        m_b_m = m_b[1] / m_b[0]

        if abs(m_a_m - p_m) < abs(m_b_m - p_m):
            moves_a += 1
            c = m_a
        else:
            moves_b += 1
            c = m_b

        if moves_a > 100 or moves_b > 100:
            break
    else:
        total_cost += moves_a * COST_A + moves_b * COST_B

    if len(lines) == 0:
        break

    lines.pop()

print(total_cost)

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
