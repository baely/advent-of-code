letter_a = ord("a")
letter_A = ord("A")

priority = 0

with open("input.txt") as f:
    while True:
        a = set(f.readline()[:-1])
        if len(a) == 0:
            break
        b = set(f.readline()[:-1])
        c = set(f.readline()[:-1])

        for d in (a & b & c):
            p = ord(d) - letter_a + 1 if d == d.lower() else ord(d) - letter_A + 27
            priority += p

print(priority)
