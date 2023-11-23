measurements = []

with open("input.txt") as f:
    for line in f.readlines():
        measurements.append(int(line))

increasing = 0

for i, measurement in enumerate(measurements):
    if not i:
        continue
    if measurement > measurements[i-1]:
        increasing += 1

print(increasing)
