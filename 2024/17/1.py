import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

register_a = int(lines[0].split(": ")[1])
register_b = int(lines[1].split(": ")[1])
register_c = int(lines[2].split(": ")[1])
program = list(map(int, lines[4].split(": ")[1].split(",")))

instruction_pointer = 0

stdout = []
def combo(operand):
    global register_a, register_b, register_c, instruction_pointer

    if 0 <= operand <= 3:
        return operand

    if operand == 4:
        return register_a
    if operand == 5:
        return register_b
    if operand == 6:
        return register_c

    raise Exception(f"invalid operand: {operand}")


# 0
def op_adv(operand):
    global register_a, register_b, register_c, instruction_pointer

    num = register_a
    dem = 2 ** combo(operand)
    register_a = num // dem


# 1
def op_bxl(operand):
    global register_a, register_b, register_c, instruction_pointer

    register_b = register_b ^ operand


# 2
def op_bst(operand):
    global register_a, register_b, register_c, instruction_pointer

    register_b = combo(operand) % 8


# 3
def op_jnz(operand):
    global register_a, register_b, register_c, instruction_pointer

    if register_a == 0:
        return

    instruction_pointer = operand


# 4
def op_bxc(operand):
    global register_a, register_b, register_c, instruction_pointer

    register_b = register_b ^ register_c


# 5
def op_out(operand):
    global register_a, register_b, register_c, instruction_pointer, stdout

    # print(combo(operand) % 8)
    stdout.append(combo(operand) % 8)


# 6
def op_bdv(operand):
    global register_a, register_b, register_c, instruction_pointer

    num = register_a
    dem = 2 ** combo(operand)
    register_b = num // dem


# 7
def op_cdv(operand):
    global register_a, register_b, register_c, instruction_pointer

    num = register_a
    dem = 2 ** combo(operand)
    register_c = num // dem


instructions = [
    op_adv, op_bxl, op_bst, op_jnz, op_bxc, op_out, op_bdv, op_cdv,
]

while True:
    if instruction_pointer >= len(program):
        break

    op = instructions[program[instruction_pointer]]
    old_instruction = instruction_pointer
    op(program[instruction_pointer + 1])

    # assume there was not a jump
    if old_instruction == instruction_pointer:
        instruction_pointer += 2


print(",".join(str(x) for x in stdout))

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")
