cc = 0

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        i, o = row.split(" | ")
        iss = i.split()
        oss = o.split()
        for osss in oss:
            print(osss)
            if len(osss) in (2, 3, 4, 7):
                cc += 1

print(cc)
