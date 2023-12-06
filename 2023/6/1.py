lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

times = list(map(int, lines[0].split(":")[1].split()))
distances = list(map(int, lines[1].split(":")[1].split()))

ways = []

for time, distance in zip(times, distances):
    possible_ways = 0

    for i in range(time):
        time_held = i
        # this_distance = (time - time_held) * time_held

        distance = (time - i) * i - distance

        if this_distance > distance:
            possible_ways += 1

    ways.append(possible_ways)

cum = 1
for way in ways:
    cum *= way

print(cum)
