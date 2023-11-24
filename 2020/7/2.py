lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

# stores outer bag, num inner bags
rels: dict[str, list[tuple[int, str]]] = {}

for line in lines:
    outer, innerstr = line.split(" contain ")

    outer = " ".join(outer.split(" ")[:-1])

    innerlist = list(innerstr[:-1].split(", "))

    for inner in innerlist:
        amt, desc = inner.split(" ", 1)

        if amt == "no":
            continue

        desc = " ".join(desc.split(" ")[:-1])

        if outer not in rels:
            rels[outer] = []

        rels[outer].append((int(amt), desc))


curr_layer: list[tuple[int, str]] = [(1, "shiny gold")]
next_layer: list[tuple[int, str]] = []

total_bags = -1

while len(curr_layer) > 0:

    for q, bag in curr_layer:
        total_bags += q

        for iq, inner in rels.get(bag, []):
            next_layer.append((iq * q, inner))

    curr_layer = next_layer
    next_layer = []

print(total_bags)
