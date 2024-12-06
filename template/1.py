from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

for line in lines:
    ...


end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
