from itertools import product


def move_piece(p: int, r: int) -> int:
    return (p + r - 1) % 10 + 1


start_pos = []
player_wins = []

n_players = 0

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        start_pos.append(int(row.replace("\n", "")[28:]))
        player_wins.append(0)
        n_players += 1


# Game States dict, key is in form ((pos, score), ... for each player)
# ie. {((1, 1), (1, 1)): 0, ((1, 1), (1, 2)): 0 ... }
game_states: dict[tuple[tuple], int] = {}

possible_states = [[(pos, score) for pos in range(1, 11) for score in range(21)]] * n_players
possible_game_states = list(product(*possible_states))

for key in possible_game_states:
    game_states[key] = 0

starting_state_key = tuple((pos, 0) for pos in start_pos)
game_states[starting_state_key] = 1

all_rolls = [sum(roll_combo) for roll_combo in product(*[[1, 2, 3]] * 3)]

while sum(game_states.values()) > 0:
    new_game_states = game_states.copy()

    for state, count in game_states.items():
        if count == 0:
            continue

        new_all_player_states = []

        for player_pos, player_score in state:
            new_player_states = []
            for roll in all_rolls:
                new_pos = move_piece(player_pos, roll)
                new_score = player_score + new_pos
                new_player_states.append((new_pos, new_score))
            new_all_player_states.append(new_player_states)

        new_states = list(product(*new_all_player_states))

        # Remove current games from current state
        new_game_states[state] -= count

        # Check for winning games or update the next state
        for new_state in new_states:
            game_over = False
            for player, (player_pos, player_score) in enumerate(new_state):
                if player_score >= 21:
                    player_wins[player] += int(count / (len(all_rolls))**(n_players - player - 1))
                    game_over = True
                    break

            if not game_over:
                new_game_states[new_state] += count

    game_states = new_game_states

print(max(player_wins))
