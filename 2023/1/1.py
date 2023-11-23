lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = f.readlines()
    nums = list(map(int, lines))
