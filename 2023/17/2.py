movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

lines: list[str] = []
nums: list[list[int]] = []

with open("input.txt") as f:
    lines = [line.strip() for line in f.read().strip().split("\n")]
    nums = [[int(x) for x in line] for line in lines]

min_to = dict()

q: dict[int, set] = {
    0: {((0, 0), (0, 0), 0)}
}

found = False

while not found:
    heat = min([k for k in q.keys() if q[k]])
    while q[heat]:
        (i, j), (vi, vj), d = q[heat].pop()

        if (i, j) == (len(nums) - 1, len(nums[0]) - 1):
            found = True
            break

        for m in movements:
            mi, mj = m
            ni, nj = i + mi, j + mj
            nk = (ni, nj)

            if not 0 <= ni < len(nums) or not 0 <= nj < len(nums[0]):
                continue

            nh = heat + nums[ni][nj]

            nd = 1
            if m == (-vi, -vj):
                continue

            if m == (vi, vj):
                if d == 10:
                    continue
                nd = d + 1
            else:
                if d < 4 and (vi, vj) != (0, 0):
                    continue

            v = (nk, m, nd)

            if v in min_to:
                if min_to[v] <= nh:
                    continue

                q[min_to[v]].remove(v)

            min_to[v] = nh

            if nh not in q:
                q[nh] = set()
            q[nh].add(v)

print(heat)
