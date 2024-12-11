from time import perf_counter_ns
from collections import defaultdict

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

for line in lines:
    stones = list(map(int, line.split(" ")))

    counts = defaultdict(int)

    for stone in stones:
        counts[stone] += 1

    for i in range(75):
        next_counts = defaultdict(int)

        for stone, c in counts.items():
            if stone == 0:
                next_counts[1] += c
            elif len(stone_str := str(stone)) % 2 == 0:
                next_counts[int(stone_str[:len(stone_str)//2])] += c
                next_counts[int(stone_str[len(stone_str)//2:])] += c
            else:
                next_counts[stone * 2024] += c

        counts = next_counts

    print(sum(counts.values()))


end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
