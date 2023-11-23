DAY_COUNT = 80

with open("input.txt") as f:
    initial_state = list(map(int, f.readline().split(",")))

fish_on_day = {i: 0 for i in range(9)}

for state in initial_state:
    fish_on_day[state] += 1


for i in range(DAY_COUNT):
    new_fish_on_day = {i: 0 for i in range(9)}
    for k, v in fish_on_day.copy().items():
        next_num = k - 1 if k > 0 else 6
        new_fish_on_day[next_num] += v
        if k == 0:
            new_fish_on_day[8] += v

    fish_on_day = new_fish_on_day.copy()

print(sum(v for v in fish_on_day.values()))
