parts: list[str] = []
nums: list[int] = []

with open("input.txt") as f:
    parts = [line.strip() for line in f.read().strip().split(",")]
    # nums = list(map(int, lines))

boxes = {
    i: [] for i in range(256)
}

for part in parts:
    h = 0
    c = None
    for c in part:
        if c in "-=":
            break

        v = ord(c)
        h += v
        h *= 17
        h %= 256

    if c == "=":
        po, n = part.split("=")
        no = int(n)

        for i, (p, n) in enumerate(boxes[h]):
            if po == p:
                boxes[h][i] = (po, no)
                break
        else:
            boxes[h].append((po, no))

    if c == "-":
        po = part.split("-")[0]
        for i, (p, n) in enumerate(boxes[h]):
            if po == p:
                boxes[h] = boxes[h][:i] + boxes[h][i+1:]
                break

s = 0

for i in range(256):
    box = boxes[i]
    k = i + 1
    for j, (p, n) in enumerate(box):
        m = j + 1
        s += (k * m * n)

print(s)
