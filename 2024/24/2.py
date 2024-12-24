import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()


def count_bits(n: int) -> int:
    b = 0
    while n > 0:
        b += n & 1
        n >>= 1
    return b


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

x = 0
for i, wire in enumerate([x for x in sorted(wire_values.keys()) if x.startswith("x")]):
    x |= wire_values[wire] << i

y = 0
for i, wire in enumerate([x for x in sorted(wire_values.keys()) if x.startswith("y")]):
    y |= wire_values[wire] << i

target = x + y


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

    ops[o] = (op, ia, ib)


def run():
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

    return k ^ target


# print(ops["z05"])
# ops["z05"], ops["z00"] = ops["z00"], ops["z05"]
# ops["z02"], ops["z01"] = ops["z01"], ops["z02"]
# print(ops["z05"])

k = run()

def find_dependents(op: str) -> list[str]:
    if op not in ops:
        return []

    _, a, b = ops[op]
    deps = []
    if a.startswith("x") or a.startswith("y"):
        deps.append(a)
    else:
        deps += find_dependents(a)

    if b.startswith("x") or b.startswith("y"):
        deps.append(b)
    else:
        deps += find_dependents(b)

    return deps

print(k)
x = 1
while x < k:
    if (x & k) > 0:
        n = x
        b = -1
        while n >= 1:
            b += 1
            n >>= 1
        w = f"z{b:02}"
        print(w)
        print(find_dependents(w))

    x <<= 1

#
# base_k = k
#
# print("kk", count_bits(base_k))
# pairs: list[str] = []
#
# for _ in range(2):
#     best_pair = None
#     best_count = None
#     for out1 in ops:
#         for out2 in ops:
#             if out1 in pairs or out2 in pairs:
#                 continue
#
#             if out1 == out2:
#                 continue
#
#             # temp swap
#             ops[out1], ops[out2] = ops[out2], ops[out1]
#             new_k = run()
#             # swap back
#             ops[out1], ops[out2] = ops[out2], ops[out1]
#             bc = count_bits(new_k)
#             if bc == 0:
#                 print(new_k)
#             if best_count is None or bc < best_count:
#                 best_count = bc
#                 best_pair = out1, out2
#
#     print(best_pair, best_count)
#     a, b = best_pair
#     pairs += [a, b]
#     ops[a], ops[b] = ops[b], ops[a]
#
# print(",".join(sorted(pairs)))
#
# # k = run()
# #
# # print(bin(k))
# #
# # wrong_bits = k ^ target
# # print(bin(wrong_bits + (1 << 45)))
# # print(count_bits(wrong_bits))

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")
