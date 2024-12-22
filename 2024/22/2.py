import math
from time import perf_counter_ns

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

start = perf_counter_ns()

def bananas(a: int) -> int:
    return a % 10

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

buyers_prices: list[list[int]] = []

s = 0
for i, line in enumerate(lines):
    buyers_prices.append([])
    x = int(line)
    buyers_prices[i].append(x)
    for _ in range(2000):
        x = next_secret(x)
        buyers_prices[i].append(x)
    s += x


buyers_bananas: list[list[int]] = []
buyers_deltas: list[list[int]] = []

for i, prices in enumerate(buyers_prices):
    buyers_bananas.append([
        bananas(price) for price in prices
    ])
    buyers_deltas.append([
        bananas(b) - bananas(a) for a, b in zip(prices[:-1], prices[1:])
    ])

seen: set[tuple[str, int]] = set()
amt: dict[str, int] = {}

for b, deltas in enumerate(buyers_deltas):
    for i in range(len(deltas) - 3):
        k = ",".join(map(str, deltas[i:i+4]))

        if k not in amt:
            amt[k] = 0

        if (k, b) not in seen:
            seen.add((k, b))
            amt[k] += buyers_bananas[b][i+4]

print(max(amt.values()))


end = perf_counter_ns()
t = end - start
precision = min(3 * math.floor(math.log(t) / math.log(10) / 3), 9)
unit = ["ns", "μs", "ms", "s"][precision//3]
print(f"duration: {t/10**precision:.3f}{unit}")