lines = []

running_total = 0

with open("input.txt") as f:
    for line in f.readlines():
        if line == "\n":
            lines.append(running_total)
            running_total = 0
        else:
            n = int(line)
            running_total += n

lines.append(running_total)

lines.sort(reverse=True)

print(sum(lines[0:min(3, len(lines))]))
