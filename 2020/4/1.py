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

    if len(req_fields - set(m.keys())) == 0:
        valid += 1

    i += 1

print(valid)
