lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

time = int("".join(lines[0].split(":")[1].strip().split()))
distance = int("".join(lines[1].split(":")[1].strip().split()))

possible_ways = 0

for i in range(time):
    time_held = i
    this_distance = (time - time_held) * time_held

    if this_distance > distance:
        possible_ways += 1

print(possible_ways)
