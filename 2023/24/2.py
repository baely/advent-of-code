import z3

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

s = z3.Solver()

p0, p1, p2 = z3.Int("p0"), z3.Int("p1"), z3.Int("p2")
v0, v1, v2 = z3.Int("v0"), z3.Int("v1"), z3.Int("v2")

for i, line in enumerate(lines):
    position, velocity = line.split(" @ ")
    px, py, pz = [int(x) for x in position.split(", ")]
    vx, vy, vz = [int(x) for x in velocity.split(", ")]

    t = z3.Int(f"t{i}")

    s.add(p0 + t * v0 == px + t * vx)
    s.add(p1 + t * v1 == py + t * vy)
    s.add(p2 + t * v2 == pz + t * vz)

s.check()
m = s.model()
x = int(str(m.evaluate(p0))) + int(str(m.evaluate(p1))) + int(str(m.evaluate(p2)))
print(x)
