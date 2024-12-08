from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

freq_antennas = {}

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if not c.isalnum():
            continue

        if c not in freq_antennas:
            freq_antennas[c] = []

        freq_antennas[c].append((i, j))

ans = set()

for antennas in freq_antennas.values():
    for ant_a in antennas:
        for ant_b in antennas:
            if ant_a == ant_b:
                continue

            ai, aj = ant_a
            bi, bj = ant_b

            di, dj = ai - bi, aj - bj
            ni, nj = ai, aj

            while True:
                ans.add((ni, nj))
                ni, nj = ni + di, nj + dj

                if not (0 <= ni < len(lines) and 0 <= nj < len(lines[0])):
                    break

print(len(ans))

end = perf_counter_ns()
print(f"duration: {(end-start)/10**6:.2f}ms")
