letter_a = ord("a")
letter_A = ord("A")

priority = 0

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        n = int(len(row)/2)
        a = set(row[:n])
        b = set(row[n:])

        for c in (a & b):
            p = ord(c) - letter_a + 1 if c == c.lower() else ord(c) - letter_A + 27
            priority += p

print(priority)
