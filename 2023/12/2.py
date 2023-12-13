from time import perf_counter

cache: dict[tuple, int] = {}


def num_possible_combos(row: str, records: list[int]) -> int:
    if not records:
        if "#" in row:
            return 0

        return 1

    t = (row, tuple(records))
    if t in cache:
        return cache[t]

    this_possibilities = 0

    record, other_records = records[0], records[1:]

    for i in range(len(row) - record + 1):
        if "#" in row[:i]:
            cache[t] = this_possibilities
            return this_possibilities
        if "." in row[i:i+record]:
            continue

        if i + record < len(row) and "#" == row[i+record]:
            continue

        this_possibilities += num_possible_combos(row[(i + record + 1):], other_records)

    cache[t] = this_possibilities
    return this_possibilities


lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

possibilities = []

for z, line in enumerate(lines):
    row, desc = line.split()

    row = "?".join([row for _ in range(5)])
    row = ".".join([x for x in row.split(".") if x != ""])
    lr = len(row)

    records = [int(x) for x in desc.split(",")]
    records = 5 * records
    lrc = len(records)

    possible = num_possible_combos(row, records)
    possibilities.append(possible)

print(sum(possibilities))
