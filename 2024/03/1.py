from time import perf_counter_ns
import re
start = perf_counter_ns()

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

n = 0

for line in lines:
    r = re.findall(r"mul\((\d+),(\d+)\)", line)
    for a, b in r:
        n += int(a) * int(b)

print(n)


end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
