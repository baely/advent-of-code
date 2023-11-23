lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = f.readlines()
    # nums = list(map(int, lines))

valid = 0

for line in lines:
    parts = line.split(" ")

    minn, maxn = parts[0].split("-")
    num1 = int(minn)
    num2 = int(maxn)

    letter = parts[1].split(":")[0]

    password = parts[2][:-1]

    p1 = password[num1 - 1]
    p2 = password[num2 - 1]

    if (p1 == letter and p2 != letter) or (p1 != letter and p2 == letter):
        valid += 1

print(valid)
