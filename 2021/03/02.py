gamma = "111111111111"
epsilon = "000000000000"

possibles = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        possibles.append(row.strip())

ox_possibles = possibles.copy()
ox_curr_index = 0

while len(ox_possibles) > 1 and ox_curr_index < len(gamma):
    count = {"0": 0, "1": 0}
    for possible in ox_possibles:
        count[possible[ox_curr_index]] += 1

    most_pop = "1" if count["1"] >= count["0"] else "0"

    new_ox_possibles = [x for x in ox_possibles if x[ox_curr_index] == most_pop]
    if len(new_ox_possibles) == 0:
        new_ox_possibles.append(ox_possibles[-1])
    
    ox_possibles = new_ox_possibles
    ox_curr_index += 1
    
ox = ox_possibles[0]

co_possibles = possibles.copy()
co_curr_index = 0

while len(co_possibles) > 1 and co_curr_index < len(epsilon):
    count = {"0": 0, "1": 0}
    for possible in co_possibles:
        count[possible[co_curr_index]] += 1

    least_pop = "0" if count["0"] <= count["1"] else "1"

    new_co_possibles = [x for x in co_possibles if x[co_curr_index] == least_pop]
    if len(new_co_possibles) == 0:
        new_co_possibles.append(co_possibles[-1])

    co_possibles = new_co_possibles
    co_curr_index += 1

co = co_possibles[0]

ox = int(ox, 2)
co = int(co, 2)

print(ox * co)
