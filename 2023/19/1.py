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

accepted_parts = []

for line in bottom_lines:
    categories = {}

    parts = line[1:-1].split(",")
    for part in parts:
        category, amt = part.split("=")
        amt = int(amt)
        categories[category] = amt

    process = "in"

    while True:
        rules = all_rules[process]
        dest = ""
        for rule_set in rules:
            if ":" not in rule_set:
                dest = rule_set
                continue
            rule, dest = rule_set.split(":")
            rule_cat = rule[0]
            rule_comp = rule[1]
            rule_amt = int(rule[2:])

            amt = categories[rule_cat]

            if rule_comp == ">" and amt > rule_amt:
                break
            
            if rule_comp == "<" and amt < rule_amt:
                break

        if dest == "R":
            break
        elif dest == "A":
            accepted_parts.append(sum(categories.values()))
            break
        else:
            process = dest

print(sum(accepted_parts))
