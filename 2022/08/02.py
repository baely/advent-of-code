
scores = [

]

heights = [

]

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        scores.append([])
        heights.append([])

        for c in row:
            if c == "\n":
                break
            scores[-1].append(None)
            heights[-1].append(int(c))

for i, row in enumerate(heights):
    for j, height in enumerate(row):
        if i == 0 or i == len(heights) - 1 or j == 0 or j == len(row) - 1:
            scores[i][j] = 0

for i, row in enumerate(heights):
    for j, height in enumerate(row):
        if scores[i][j] == 0:
            continue

        above = 0
        for k in range(i)[::-1]:
            above += 1
            if heights[k][j] >= height:
                break

        right = 0
        for k in range(j + 1, len(row)):
            right += 1
            if heights[i][k] >= height:
                break

        below = 0
        for k in range(i + 1, len(heights)):
            below += 1
            if heights[k][j] >= height:
                break

        left = 0
        for k in range(j)[::-1]:
            left += 1
            if heights[i][k] >= height:
                break

        score = above * right * below * left

        scores[i][j] = score

print(max(max(row) for row in scores))
