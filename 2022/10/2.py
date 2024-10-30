with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

X = 1
cycles = 0

strength = 0


def clock_tick():
    global X, cycles, strength


    x = cycles % 40

    if x - 1 <= X <= x + 1:
        print("#", end="")
    else:
        print(".", end="")
    if x == 39:
        print("")

    cycles += 1


def addx(*args):
    global X
    clock_tick()
    clock_tick()
    X += int(args[0])


def noop(*args):
    clock_tick()


funcmap = {
    "addx": addx,
    "noop": noop,
}

for line in lines:
    if not line:
        continue
    if " " in line:
        f, r = line.split(" ", 1)
    else:
        f = line
        r = []
    funcmap[f](r)
