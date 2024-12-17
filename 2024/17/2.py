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

k = 15
# search_space is all multiples of 8**15.
# each multiple of 8**k between 8**k and 8**(k-q)
#  may produce unique values for the k-th digit.
search_space = [8 ** k + (n * (8 ** k)) for n in range(8)]

next_search = []

valid_a = []

while k >= 0:
    for a in search_space:
        register_a = a
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

        state_set = set()
        loop = False
        while True:
            if instruction_pointer >= len(program):
                break

            this_state = (register_a, register_b, register_c, instruction_pointer)
            if this_state in state_set:
                loop = True
                break
            state_set.add(this_state)

            op = instructions[program[instruction_pointer]]
            old_instruction = instruction_pointer
            op(program[instruction_pointer + 1])

            # assume there was not a jump
            if old_instruction == instruction_pointer:
                instruction_pointer += 2

        # not worth continuing
        if len(stdout) != len(program):
            continue

        # found a valid A
        if stdout == program:
            valid_a.append(a)

        if stdout[k] == program[k]:
            # add next k to next space
            # if the k-th digit matches, add all As for finding the (k-1)-th
            for n in range(8):
                next_search.append(a + (n * (8 ** (k-1))))

    search_space = next_search
    next_search = []

    k -= 1


print(min(valid_a))


end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")
