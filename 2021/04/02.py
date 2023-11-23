cards: list[list[list[int]]] = []

with open("input.txt") as f:
    calls = list(map(int, f.readline().split(",")))

    curr_card = None

    for row in f.readlines():
        if row == "\n":
            if curr_card is not None:
                cards.append(curr_card)
            curr_card = []
            continue
        curr_card.append([int(x) for x in row.strip().split(" ") if x != ""])

possibilities = []
all_cards = []

for card in cards:
    curr_card = []

    for row in card:
        curr_card.append(set(row))
    for i in range(len(card[0])):
        curr_card.append(set(row[i] for row in card))

    possibilities.append(curr_card)
    all_cards.append(set(sum(card, [])))


for i in range(len(calls)):
    curr_set = set(calls[:i+1])

    found = 0
    final = False
    last_winner = None

    print(f"Current set: {curr_set}")

    for j, possible in enumerate(possibilities.copy()):
        for possibility in possible:
            if len(possibility - curr_set) == 0:
                print(f"{len(all_cards)=}")
                if len(all_cards) == 1:
                    final = True
                    last_winner = all_cards[j - found]
                del possibilities[j - found]
                del all_cards[j - found]
                found += 1
                break

    if final:
        print(all_cards)
        unmarked = last_winner - curr_set
        print(sum(unmarked) * calls[i])
        break
