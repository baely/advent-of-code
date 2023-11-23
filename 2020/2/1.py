lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = f.readlines()
    # nums = list(map(int, lines))

valid = 0

for line in lines:
    parts = line.split(" ")

    minn, maxn = parts[0].split("-")
    minn = int(minn)
    maxn = int(maxn)

    letter = parts[1].split(":")[0]

    password = parts[2][:-1]

    count = 0
    for c in password:
        if c == letter:
            count += 1

    if minn <= count <= maxn:
        valid += 1

print(valid)
