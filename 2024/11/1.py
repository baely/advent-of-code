from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

for line in lines:
    stones = list(map(int, line.split(" ")))

    for _ in range(25):
        next_stones = []
        for stone in stones:
            if stone == 0:
                next_stones.append(1)
            elif len(stone_str := str(stone)) % 2 == 0:
                next_stones.append(int(stone_str[:len(stone_str)//2]))
                next_stones.append(int(stone_str[len(stone_str)//2:]))
            else:
                next_stones.append(stone * 2024)

        stones = next_stones

    print(len(next_stones))


end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
