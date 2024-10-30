with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

X = 1
cycles = 0

strength = 0


def clock_tick():
    global cycles, strength

    cycles += 1
    if (cycles - 20) % 40 == 0:
        strength += X * cycles


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


print(strength)