ROLLING_AVERAGE_WINDOW = 3

measurements = []

with open("input.txt") as f:
    for line in f.readlines():
        measurements.append(int(line))

increasing = 0

for i, measurement in enumerate(measurements):
    if i < ROLLING_AVERAGE_WINDOW:
        continue

    if measurement > measurements[i - ROLLING_AVERAGE_WINDOW]:
        increasing += 1

print(increasing)
