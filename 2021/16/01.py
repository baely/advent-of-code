from collections import deque

with open("input.txt") as f:
    i = deque(f.read().replace("\n", ""))


def load_buffer(buffer: deque, min_bits: int) -> None:
    global i
    while len(buffer) < min_bits:
        x = bin(int(i.popleft(), 16))[2:].zfill(4)
        for b in x:
            buffer.append(b)


def read_buffer_bits(buffer: deque, bits: int) -> list[str]:
    load_buffer(buffer, bits)
    return [buffer.popleft() for _ in range(bits)]


def read_buffer(buffer: deque, bits: int) -> int:
    x = "".join(read_buffer_bits(buffer, bits))
    return int(x, 2)


def read_literal_packet(buffer: deque) -> int:
    n = 0
    while (x := read_buffer(buffer, 5)) & 16:
        n *= 16
        n += x - 16
    else:
        n *= 16
        n += x
    return n


def read_operator_packet(buffer: deque) -> list[tuple[int, int]]:
    length_type_id = read_buffer(buffer, 1)

    packets = []

    if length_type_id == 0:
        n_bits = read_buffer(buffer, 15)
        packets = read_adjacent_packets(buffer, n_bits)
    elif length_type_id == 1:
        n_packets = read_buffer(buffer, 11)
        for _ in range(n_packets):
            packets.append(read_packet(buffer))

    return packets


def read_packet(buffer: deque) -> (int, int):
    version = read_buffer(buffer, 3)
    type_id = read_buffer(buffer, 3)

    if type_id == 4:
        return version, read_literal_packet(buffer)
    else:
        return version, read_operator_packet(buffer)


def read_adjacent_packets(buffer: deque, bits: int) -> list[tuple[int, int]]:
    temp_buffer = deque(read_buffer_bits(buffer, bits))
    packets = []
    while temp_buffer:
        packets.append(read_packet(temp_buffer))
    return packets


def sum_versions(packet: tuple) -> int:
    v, t = packet
    n = v
    if isinstance(t, list):
        n += sum(sum_versions(p) for p in t)
    return n


print(sum_versions(read_packet(deque())))
