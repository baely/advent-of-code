octopuses: list[list[int]] = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a = list(map(int, row.replace("\n", "")))
        octopuses.append(a)


neighbours = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
]

total_flashes = 0

for _ in range(100):
    new_octopuses = [[octopus + 1 for octopus in row] for row in octopuses]

    flashed = [[0 for _ in row] for row in octopuses]

    for _ in range(len(octopuses) * len(octopuses[0])):
        for i, row in enumerate(new_octopuses):
            for j, octopus in enumerate(row):
                if octopus > 9 and flashed[i][j] == 0:
                    flashed[i][j] = 1
                    for m, n in neighbours:
                        if 0 <= i + m < len(new_octopuses) and 0 <= j + n < len(new_octopuses[i]):
                            new_octopuses[i + m][j + n] += 1

    total_flashes += sum([sum(1 for octopus in row if octopus > 9) for row in new_octopuses])

    new_octopuses = [[octopus if octopus <= 9 else 0 for octopus in row] for row in new_octopuses]

    octopuses = new_octopuses

print(total_flashes)
