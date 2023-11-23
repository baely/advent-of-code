beats = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

pairs = [

]

heir = {
    "Y": "X",
    "Z": "Y",
    "X": "Z",
}

score = 0

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a, b = list(row.split())

        pairs.append((a, b))

for (a, b) in pairs:
    a = beats[a]

    print(a, b)

    score += scores[b]

    if a == b:
        score += 3
    elif heir[b] == a:
        score += 6


print(score)
