import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

NEIGHBOURS = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]

wire_values: dict[str, bool] = {}


for i, line in enumerate(lines):
    if line == "":
        break

    wire, value = line.split(": ")
    value = int(value)

    wire_values[wire] = value == 1

ops: dict[str, tuple[str, str, str]] = {}

found = False
for line in lines:
    if line == "":
        found = True
        continue

    if not found:
        continue

    i, o = line.split(" -> ")
    ia, op, ib = i.split(" ")
    print(ia, op, ib, o)

    ops[o] = (op, ia, ib)


# evaled: dict[str, bool] = {}

def eval_wire(wire: str) -> None:
    op, ia, ib = ops[wire]

    if ia not in wire_values:
        eval_wire(ia)

    if ib not in wire_values:
        eval_wire(ib)

    out = None
    if op == "AND":
        out = wire_values[ia] and wire_values[ib]
    if op == "OR":
        out = wire_values[ia] or wire_values[ib]
    if op == "XOR":
        out = wire_values[ia] ^ wire_values[ib]

    wire_values[wire] = out


for wire in sorted(ops.keys()):
    eval_wire(wire)

k = 0
for i, wire in enumerate([x for x in sorted(ops.keys()) if x.startswith("z")]):
    k |= wire_values[wire] << i
    print(wire, wire_values[wire])

print(bin(k))
print(k)

print(ops)



end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")
