import math

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

mod_states: dict[str, bool] = {}
mod_types: dict[str, str] = {}
mod_sends: dict[str, list[str]] = {}
mod_recvs: dict[str, dict[str, bool]] = {}

for line in lines:
    dept_module, dest_modules_str = line.split(" -> ")

    dept_mod_type = ""
    dept_mod_name = dept_module
    if dept_module[0] in "%&":
        dept_mod_type = dept_module[0]
        dept_mod_name = dept_module[1:]

    dest_modules = dest_modules_str.split(", ")

    mod_states[dept_mod_name] = False
    mod_types[dept_mod_name] = dept_mod_type
    mod_sends[dept_mod_name] = dest_modules

    for dest_module in dest_modules:
        if dest_module not in mod_recvs:
            mod_recvs[dest_module] = {}
        mod_recvs[dest_module][dept_mod_name] = False

button_presses = 0

prefinal_cycles: dict[str, int] = {y: 0 for x in mod_recvs["rx"].keys() for y in mod_recvs[x].keys()}

while True:
    button_presses += 1
    pulse_queue = [("button", "broadcaster", False)]
    found = False

    while pulse_queue:
        press, pulse_queue = pulse_queue[0], pulse_queue[1:]
        dept, dest, pulse = press

        if dest in mod_recvs["rx"] and pulse:
            if prefinal_cycles[dept] == 0:
                prefinal_cycles[dept] = button_presses

            if all(x > 0 for x in prefinal_cycles.values()):
                found = True
                break

        if dest not in mod_types:
            continue

        dest_type = mod_types[dest]

        next_pulse = False

        if dest_type == "%":
            if pulse:
                continue

            mod_states[dest] = not mod_states[dest]
            next_pulse = mod_states[dest]
        if dest_type == "&":
            mod_recvs[dest][dept] = pulse
            next_pulse = not all(mod_recvs[dest].values())

        next_dests = mod_sends[dest]
        for next_dest in next_dests:
            next_press = (dest, next_dest, next_pulse)
            pulse_queue.append(next_press)

    if found:
        break

print(math.lcm(*list(prefinal_cycles.values())))
