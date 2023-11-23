lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]

    # nums = list(map(int, lines))

i = 0

req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid = 0

while i < len(lines):
    m = {}

    deets = ""

    while i < len(lines) and (line := lines[i]) != "":
        deets += line + " "
        i += 1

    sepdeets = deets.split(" ")

    for deet in sepdeets:
        if not deet:
            continue
        k, v = deet.split(":")
        m[k] = v

    i += 1

    if len(req_fields - set(m.keys())) != 0:
        continue

    if not (1920 <= int(m["byr"]) <= 2002):
        continue

    if not (2010 <= int(m["iyr"]) <= 2020):
        continue

    if not (2020 <= int(m["eyr"]) <= 2030):
        continue

    ht, unit = int(m["hgt"][:-2]), m["hgt"][-2:]

    if unit not in {"cm", "in"}:
        continue

    if unit == "cm" and not (150 <= ht <= 193):
        continue

    if unit == "in" and not (59 <= ht <= 76):
        continue

    hcl = m["hcl"]
    if not hcl[0] == "#":
        continue

    if not len(hcl) == 7:
        continue

    if not all(x in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"} for x in hcl[1:]):
        continue

    if m["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        continue

    if not (len(m["pid"]) == 9 and str(m["pid"]).isnumeric()):
        continue

    valid += 1

print(valid)
