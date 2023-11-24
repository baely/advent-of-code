lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

# stores inner bag -> set of parent bags
rels: dict[str, set[str]] = {}

for line in lines:
    outer, innerstr = line.split(" contain ")

    outer = " ".join(outer.split(" ")[:-1])

    innerlist = list(innerstr[:-1].split(", "))

    for inner in innerlist:
        amt, desc = inner.split(" ", 1)

        desc = " ".join(desc.split(" ")[:-1])

        if desc not in rels:
            rels[desc] = set()

        rels[desc].add(outer)


new_outers = rels["shiny gold"]
all_outers = set()

while len(new_outers) > 0:
    t = new_outers
    all_outers |= new_outers
    new_outers = set()

    for n in t:
        print(f"{n} can be contained in {rels.get(n, set())}")
        for c in rels.get(n, set()):
            new_outers.add(c)

    new_outers -= all_outers

print(len(all_outers))
print(list(all_outers))
