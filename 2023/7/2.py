lines: list[str] = None
nums: list[int] = None

card_order = [
    "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"
]

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

hands: list[tuple] = []

for line in lines:
    id, num = line.split()
    num = int(num)

    max_hand_strength = 7
    final_cards = None

    for replacement in card_order:
        cards = list(id.replace("J", replacement))

        individual_weights = tuple(
            card_order.index(c) for c in cards
        )

        counter_map = {}

        for card in cards:
            if card not in counter_map:
                counter_map[card] = 0
            counter_map[card] += 1

        hand_strength = None

        cx = list(counter_map.values())

        cx_counterr = {}

        for cxx in cx:
            if cxx not in cx_counterr:
                cx_counterr[cxx] = 0
            cx_counterr[cxx] += 1

        if 5 in cx:  # five of a kind
            hand_strength = 0
        elif 4 in cx:  # four of a kind
            hand_strength = 1
        elif 3 in cx and 2 in cx:  # full house
            hand_strength = 2
        elif 3 in cx:  # three of a kind
            hand_strength = 3
        elif cx_counterr.get(2) == 2:
            hand_strength = 4
        elif 2 in cx:  # two of a kind
            hand_strength = 5
        else:
            hand_strength = 6

        if hand_strength < max_hand_strength:
            max_hand_strength = hand_strength
            final_cards = cards

    hand = (max_hand_strength, individual_weights, cards, num)

    hands.append(hand)

hands.sort(key=lambda x: (x[0], x[1]))

s = 0

for i, (_, _, cards, weight) in enumerate(hands):
    j = len(hands) - i
    s += (j * weight)

print(s)

