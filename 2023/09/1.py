lines: list[str] = None
nums: list[int] = None

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    # nums = list(map(int, lines))

extraps = []

for line in lines:
    nums = list(map(int, line.split()))

    layers: list[list[int]] = []
    curr_layer: list[int] = nums

    while not all(x == 0 for x in curr_layer):
        layers.append(curr_layer)
        next_layer = []

        for i, x in enumerate(curr_layer):
            if i == len(curr_layer) - 1:
                continue

            diff = curr_layer[i + 1] - x
            next_layer.append(diff)

        curr_layer = next_layer

    layers.reverse()

    last_extrap = None

    for i, layer in enumerate(layers):
        if i == 0:
            continue

        extrap = layers[i][-1] + layers[i - 1][-1]
        last_extrap = extrap
        layers[i].append(extrap)

    extraps.append(last_extrap)

print(sum(extraps))
