# Slow iterative solution


def check_match(rss) -> bool:
    s = set()
    for ss in rss:
        s |= ss

    xx = damaged_set - s
    xy = operational_set & s

    return not xx and not xy


lines: list[str] = []
nums: list[int] = []

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

possibilities = []

# List of sets where possible_sets[i][j] = set(list(range(i, i + j)))
#  eg. possible_sets[5, 3] = {5, 6, 7}
possible_sets: list[list[set]] = []
for i in range(200):
    possible_sets.append([])
    for j in range(200):
        possible_sets[i].append(set(list(range(i, i + j))))


for line in lines:
    row, record = line.split()

    row = "?".join([row for _ in range(5)])
    row = ".".join([x for x in row.split(".") if x != ""])
    lr = len(row)

    records = [int(x) for x in record.split(",")]
    records = 5 * records
    lrc = len(records)


    ranges = []

    operational_set = set(i for i, c in enumerate(row) if c == ".")
    damaged_set = set(i for i, c in enumerate(row) if c == "#")

    # List of non-. ranges
    start = None
    for i, c in enumerate(row):
        if c == ".":
            if start is not None:
                ranges.append((start, i))
                start = None
            continue

        if start is None:
            start = i
            continue
    if start is not None:
        ranges.append((start, lr))

    # ranges_map maps each index to the end of its range or -1 if it is a .
    ranges_map: dict[int, int] = {}
    for i in range(lr):
        ranges_map[i] = -1
    for r1, r2 in ranges:
        for i in range(r1, r2):
            ranges_map[i] = r2

    # Find all valid positions for the start each block, ie. where a block if fully contained within a range
    valid_start_pos: list[list[int]] = []
    for i, record in enumerate(records):
        valid_start_pos.append([])
        for j in range(lr):
            if j + record <= ranges_map[j]:
                if j > 0 and row[j-1] == "#":
                    continue
                if j + record < lr and row[j + record] == "#":
                    continue
                valid_start_pos[i].append(j)

    # The same above back backwards, removes some of the latter positions for lefter blocks
    prev_max = None
    for i, record in reversed(list(enumerate(records))):
        if prev_max is not None:
            valid_start_pos[i] = [x for x in valid_start_pos[i] if x < prev_max - record]
        prev_max = max(valid_start_pos[i])

    # next_best_pos maps the next valid index for each block's starting position.
    # next_best_pos[n][i] where n is the nth block, and you want to check index i
    #  - i = i when the current i is a valid starting position
    #  - i = the next valid starting position to the right in other cases
    next_best_pos: list[list[int]] = []
    for i, valid in enumerate(valid_start_pos):
        next_best_pos.append([])
        for j in range(lr):
            next_best = min([x for x in valid if x >= j] or [-1])
            next_best_pos[i].append(next_best)
        next_best_pos[i].append(-1)

    # recorded_sets tracks the set of numbers of which each block is currently covering. Used for pattern matching
    record_sets = [set() for _ in records]

    # Put all blocks in their starting positions
    record_pos = [0 for _ in records]
    for i, record in enumerate(records):
        record_pos[i] = next_best_pos[i][record_pos[i]]
        record_sets[i] = possible_sets[record_pos[i]][record]
        if i < lrc - 1:
            record_pos[i + 1] = next_best_pos[i + 1][record_pos[i] + record + 1]

    possible = 0 + check_match(record_sets)

    curr_record = lrc - 1
    while True:
        if curr_record < 0:
            break
        record = records[curr_record]

        end = False

        next_pos = next_best_pos[curr_record][record_pos[curr_record] + 1]
        if next_pos == -1:
            end = True
        else:
            record_pos[curr_record] = next_pos
            record_sets[curr_record] = possible_sets[record_pos[curr_record]][record]

        prec_pos = record_pos[curr_record - 1] + records[curr_record - 1] if curr_record > 0 else 0
        if not end and "#" in row[prec_pos:record_pos[curr_record]]:
            end = True

        if end:
            curr_record -= 1
        if not end:
            if curr_record < lrc - 1:
                for i, other_record in enumerate(records):
                    if i < curr_record:
                        continue
                    if i < lrc - 1:
                        record_pos[i + 1] = next_best_pos[i + 1][record_pos[i] + other_record + 1]
                        record_sets[i + 1] = possible_sets[record_pos[i + 1]][records[i + 1]]

                curr_record = lrc - 1

            possible += check_match(record_sets)

    possibilities.append(possible)

print(sum(possibilities))
