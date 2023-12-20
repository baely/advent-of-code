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
        # mod_recvs[dest_module].append(dept_module)
        mod_recvs[dest_module][dept_mod_name] = False

button_presses = 0
high_pulses = 0
low_pulses = 0


for _ in range(1000):
    button_presses += 1
    pulse_queue = [("button", "broadcaster", False)]

    while pulse_queue:
        press, pulse_queue = pulse_queue[0], pulse_queue[1:]
        dept, dest, pulse = press

        if pulse:
            high_pulses += 1
        else:
            low_pulses += 1

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
            # send_pulse(dest, next_dest, next_pulse)
            next_press = (dest, next_dest, next_pulse)
            pulse_queue.append(next_press)

print(button_presses, high_pulses, low_pulses)
print(high_pulses * low_pulses)
