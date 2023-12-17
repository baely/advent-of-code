movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

lines: list[str] = []
nums: list[list[int]] = []

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    nums = [[int(x) for x in line] for line in lines]

min_to = dict()

queue: dict[int, set] = {
    0: {((0, 0), (0, 0), 0)}
}

found = False

while not found:
    heat = min([k for k in queue.keys() if queue[k]])
    while queue[heat]:
        (i, j), (vel_i, vel_j), distance = queue[heat].pop()

        if (i, j) == (len(nums) - 1, len(nums[0]) - 1):
            found = True
            break

        for movement in movements:
            movement_i, movement_j = movement
            new_i, new_j = i + movement_i, j + movement_j
            new_pos = (new_i, new_j)

            if not 0 <= new_i < len(nums) or not 0 <= new_j < len(nums[0]):
                continue

            new_heat = heat + nums[new_i][new_j]

            new_distance = 1
            if movement == (-vel_i, -vel_j):
                continue

            if movement == (vel_i, vel_j):
                if distance == 10:
                    continue
                new_distance = distance + 1
            else:
                if distance < 4 and (vel_i, vel_j) != (0, 0):
                    continue

            pos_mov_dist = (new_pos, movement, new_distance)

            if pos_mov_dist in min_to:
                if min_to[pos_mov_dist] <= new_heat:
                    continue

                queue[min_to[pos_mov_dist]].remove(pos_mov_dist)

            min_to[pos_mov_dist] = new_heat

            if new_heat not in queue:
                queue[new_heat] = set()
            queue[new_heat].add(pos_mov_dist)

print(heat)
