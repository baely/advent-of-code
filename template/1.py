lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().split() if line and not line.isspace()]
    # nums = list(map(int, lines))

for line in lines:
    ...
