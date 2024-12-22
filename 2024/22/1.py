import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

def mix_numbers(a: int, b: int) -> int:
    return a ^ b

def prune_number(a: int) -> int:
    return a % 16777216

def next_secret(last_secret: int) -> int:
    r = last_secret * 64
    last_secret = mix_numbers(last_secret, r)
    last_secret = prune_number(last_secret)

    r = last_secret//32
    last_secret = mix_numbers(last_secret, r)
    last_secret = prune_number(last_secret)

    r = last_secret * 2048
    last_secret = mix_numbers(last_secret, r)
    last_secret = prune_number(last_secret)
    return last_secret

s = 0
for line in lines:
    x = int(line)
    for _ in range(2000):
        # print(x)
        x = next_secret(x)
    s += x
    print(x)

print(s)

end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")