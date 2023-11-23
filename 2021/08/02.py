def get_digit(l_s, s):
    for i, v in enumerate(l_s):
        if v == s:
            return i


with open("input.txt") as k:
    r = k.readlines()

    all_ns = 0

    for row in r:
        i, o = row.split(" | ")
        inputs = i.split()
        outputs = o.split()

        found = [set() for _ in range(10)]

        # Loop until at least all the output digits are found
        while not all(set(x) in found for x in outputs):
            for possible in inputs + outputs:
                ps = set(possible)
                # 1 uniquely has 2 segments
                if len(ps) == 2:
                    found[1] = ps
                # 7 uniquely has 3 segments
                if len(ps) == 3:
                    found[7] = ps
                # 4 uniquely has 4 segments
                if len(ps) == 4:
                    found[4] = ps
                # 2, 3, 5 all have 5 segments
                if len(ps) == 5:
                    if found[1] is not None:
                        # 3 is the only 5 segmented digit to have 3 additional segments than 1
                        if len(ps - found[1]) == 3:
                            found[3] = ps
                    if found[4] is not None:
                        # 2 is the only 5 segmented digit to have 3 additional segments than 4
                        if len(ps - found[4]) == 3:
                            found[2] = ps
                    if found[1] is not None and found[4] is not None:
                        # 5 is the only 5 segmented digit to not have 3 additional segments than 1 and 4
                        if len(ps - found[1]) != 3 and len(ps - found[4]) != 3:
                            found[5] = ps
                # 0, 6, 9 all have 6 segments
                if len(ps) == 6:
                    if found[1] is not None:
                        # 6 is the only 6 segmented digit to have 5 additional segments than 1
                        if len(ps - found[1]) == 5:
                            found[6] = ps
                    if found[4] is not None:
                        # 9 is the only 6 segmented digit to have 2 additional segments than 4
                        if len(ps - found[4]) == 2:
                            found[9] = ps
                    if found[1] is not None and found[4] is not None:
                        # 0 is the only 6 segmented digit to have 4 and 3 additional segments than 1 and 4 respectively
                        if len(ps - found[1]) == 4 and len(ps - found[4]) == 3:
                            found[0] = ps
                # 8 uniquely has 7 segments
                if len(ps) == 7:
                    found[8] = ps

        n = 0
        for dig in outputs:
            n *= 10
            n += get_digit(found, set(dig))

        all_ns += n

print(all_ns)
