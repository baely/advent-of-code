hands = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

scores = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

hand_scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

score = 0

pairs = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a, b = list(row.split())

        pairs.append((a, b))

for (a, b) in pairs:
    a = hands[a]

    score += scores[b]

    if b == "X": # lose
        b = beats[a]
    if b == "Y": # draw
        b = a
    if b == "Z": # win
        b = beats[beats[a]]

    score += hand_scores[b]



print(score)
