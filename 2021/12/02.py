paths = {}

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a, b = list(row.replace("\n", "").split("-"))
        if a not in paths:
            paths[a] = []
        if b not in paths:
            paths[b] = []

        paths[a].append(b)
        paths[b].append(a)


def get_paths(head: str, curr_path: list[str], goal: str) -> list[list[str]]:
    possible_paths: list[list[str]] = []
    for i, next_cave in enumerate(paths[head]):
        # Just keep adding exit cases until it works
        if curr_path + [next_cave] in possible_paths:
            continue
        if next_cave == goal:
            possible_paths.append(curr_path + [next_cave])
            continue
        if next_cave.islower():
            if not (len([i for i in curr_path if i == next_cave]) < 1 or max(len([i for i in curr_path if i == next_cave]) for i in curr_path if i.islower()) < 2):
                continue
        if next_cave == "start":
            continue
        for possible_path in get_paths(next_cave, curr_path + [next_cave], goal):
            if possible_path in possible_paths:
                continue
            possible_paths.append(possible_path)
    return possible_paths


print(len(get_paths("start", ["start"], "end")))
