with open("input.txt") as f:
    top_lines, bottom_lines = f.read().strip().split("\n\n")

    top_lines = top_lines.split("\n")
    bottom_lines = bottom_lines.split("\n")
    # nums = list(map(int, lines))

all_rules: dict[str, list] = {}

for line in top_lines:
    name, rest = line.split("{")

    rules = rest[:-1].split(",")

    all_rules[name] = rules

q: list[tuple[str, dict[str, tuple[int, int]]]] = [
    ("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})
]

accepted = 0

while q:
    curr = q.pop()

    dest, ranges = curr

    if dest == "R":
        continue

    if dest == "A":
        ta = 1
        for tl, tu in ranges.values():
            ta *= (tu - tl) + 1
        accepted += ta
        continue

    rules = all_rules[dest]
    next_dest = ""

    for rule_set in rules:
        if ":" not in rule_set:
            next_dest = rule_set
            next_item = (next_dest, ranges.copy())
            q.append(next_item)
            continue
        rule, next_dest = rule_set.split(":")
        rule_cat = rule[0]
        rule_comp = rule[1]
        rule_amt = int(rule[2:])

        lower, upper = ranges[rule_cat]

        if rule_comp == ">" and lower <= rule_amt < upper:
            new_ranges = ranges.copy()
            new_ranges[rule_cat] = (rule_amt + 1, upper)
            ranges[rule_cat] = (lower, rule_amt)

            next_item = (next_dest, new_ranges)
            q.append(next_item)

        if rule_comp == "<" and lower < rule_amt <= upper:
            new_ranges = ranges.copy()
            new_ranges[rule_cat] = (lower, rule_amt - 1)
            ranges[rule_cat] = (rule_amt, upper)

            next_item = (next_dest, new_ranges)
            q.append(next_item)

print(accepted)
