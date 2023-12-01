lines: list[str] = None
# nums: list[int] = None

with open("input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]
    # nums = list(map(int, lines))

vals = []

nums: list[str] = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

real_nums = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

for line in lines:
    n1_index = None
    n1_word = ""

    for num in nums + real_nums:
        try:
            i = line.index(num)
        except ValueError:
            continue

        if n1_index is None or i < n1_index:
            n1_index = i
            n1_word = num

    n2_index = None
    n2_word = ""

    for num in nums + real_nums:
        try:
            i = line[::-1].index(num[::-1])
        except ValueError:
            continue

        if n2_index is None or i < n2_index:
            n2_index = i
            n2_word = num

    if n1_word == "" or n2_word == "":
        print(line, n1_word, n2_word)

    if n1_word in nums:
        n1 = nums.index(n1_word)
    else:
        n1 = real_nums.index(n1_word)

    if n2_word in nums:
        n2 = nums.index(n2_word)
    else:
        n2 = real_nums.index(n2_word)

    v = n1 * 10 + n2
    vals.append(v)

print(sum(vals))
