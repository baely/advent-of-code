
def get_rolled_number(n: int) -> (int, int):
    return 6 + n * 9, n + 1


def move_piece(p: int, r: int) -> int:
    return (p + r - 1) % 10 + 1


pos = []
scores = []


with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        pos.append(int(row[28:].replace("\n", "")))
        scores.append(0)


turn_number = 0
curr_player = 0
while not any(score >= 1000 for score in scores):
    rolled_number, turn_number = get_rolled_number(turn_number)
    new_pos = move_piece(pos[curr_player], rolled_number)
    pos[curr_player] = new_pos
    scores[curr_player] += new_pos
    curr_player = (curr_player + 1) % len(pos)


print(min(scores) * turn_number * 3)
