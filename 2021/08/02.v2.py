UNIQUE_LENGTHS = {2: 1, 4: 4, 3: 7, 7: 8}
SHARED_LENGTHS = {(6, 4, 3): 0, (5, 4, 3): 2, (5, 3, 2): 3, (5, 4, 2): 5, (6, 5, 3): 6, (6, 4, 2): 9}


with open("input.txt") as k:
    r = k.readlines()

    all_ns = 0

    for row in r:
        i, o = row.split(" | ")
        inputs = i.split()
        outputs = o.split()

        found = [set() for _ in range(10)]

        while not all(set(x) in found for x in outputs):
            for possible in inputs + outputs:
                ps = set(possible)
                lps = len(ps)
                elps = (lps, len(ps - found[1]), len(ps - found[4]))

                if lps in UNIQUE_LENGTHS:
                    found[UNIQUE_LENGTHS[lps]] = ps
                elif elps in SHARED_LENGTHS:
                    found[SHARED_LENGTHS[elps]] = ps

        n = 0
        for dig in outputs:
            n *= 10
            n += found.index(set(dig))

        all_ns += n

print(all_ns)
