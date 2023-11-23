
visibility = [

]

heights = [

]

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        visibility.append([])
        heights.append([])

        for c in row:
            if c == "\n":
                break
            visibility[-1].append(False)
            heights[-1].append(int(c))

for i, row in enumerate(heights):
    for j, height in enumerate(row):
        if i == 0 or i == len(heights) - 1 or j == 0 or j == len(row) - 1:
            visibility[i][j] = True

for i, row in enumerate(heights):
    for j, height in enumerate(row):
        if visibility[i][j]:
            continue

        above = max(heights[k][j] for k in range(i))
        right = max(heights[i][k] for k in range(j + 1, len(row)))
        below = max(heights[k][j] for k in range(i + 1, len(heights)))
        left = max(heights[i][k] for k in range(j))

        if height > min(above, right, below, left):
            visibility[i][j] = True

print(sum(sum(row) for row in visibility))
