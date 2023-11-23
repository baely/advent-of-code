from typing import Sequence

ROTATION_MATRICES = [
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
    [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
    [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
    [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
    [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
    [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
    [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
    [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
    [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
    [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
    [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
    [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
    [[0, 0, 1], [0, -1, 0], [1, 0, 0]],
    [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
    [[0, 0, -1], [0, -1, 0], [-1, 0, 0]],
    [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
    [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
    [[0, 1, 0], [0, 0, -1], [-1, 0, 0]]
]

OVERLAP_THRESHOLD = 12


# Scanners is list of scanners in the form:
# [0: beacons, 1: relative_parent, 2: relative_position (after rotation)]
scanners: list[list[list[tuple[int]], int, tuple[int]]] = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        row = row.replace("\n", "")
        if row.startswith("---"):
            scanner = []
        elif row == "":
            new_scanner = [scanner, None, [0, 0, 0], len(scanners)]
            scanners.append(new_scanner)
        else:
            new_beacon = tuple(map(int, row.split(",")))
            scanner.append(new_beacon)

    new_scanner = [scanner, None, [0, 0, 0], len(scanners)]
    scanners.append(new_scanner)

print("Starting with", sum(len(x[0]) for x in scanners), "beacons.")

scanners[0][1] = -1
scanners[0][2] = (0, 0, 0)


def dot_product(m1: Sequence[int], m2: Sequence[int]) -> int:
    return sum(a * b for a, b in zip(m1, m2))


def beacon_rotate(beacon: Sequence[int], rotation: list[list[int]]) -> tuple[int]:
    return tuple(dot_product(beacon, rotation_row) for rotation_row in rotation)


def beacon_add(beacon1: Sequence[int], beacon2: Sequence[int]) -> tuple[int]:
    return tuple(a + b for a, b in zip(beacon1, beacon2))


def beacon_diff(beacon1: Sequence[int], beacon2: Sequence[int]) -> tuple[int]:
    return tuple(a - b for a, b in zip(beacon1, beacon2))


def beacon_prod(beacon1: Sequence[int], beacon2: Sequence[int]) -> tuple[int]:
    return tuple(a * b for a, b in zip(beacon1, beacon2))


def beacon_distance(beacon1: Sequence[int], beacon2: Sequence[int]) -> float:
    return beacon_magnitude(beacon_diff(beacon1, beacon2))


def beacon_magnitude(beacon: Sequence[int]) -> float:
    return sum(a ** 2 for a in beacon) ** 1/2


def scanner_overlap(scanner1: list[list[int]], scanner2: list[list[int]]) -> (bool, tuple[list[int], list[int]]):
    """
    Returns
    bool: whether the two scanners have at least OVERLAP_THRESHOLD overlapping beacons
    tuple[int, list[int]]: tuple of the s2 beacons rotated to align with s1, and the position delta from s1 to s2
    """
    for rotation in ROTATION_MATRICES:
        distances: dict[tuple[int], list[int, list[tuple]]] = {}
        for beacon1 in scanner1:
            for beacon2 in scanner2:
                beacon2_rotated = beacon_rotate(beacon2, rotation)
                delta = beacon_diff(beacon1, beacon2_rotated)
                if delta == (0, 0, 0):
                    print(delta, beacon1, beacon2_rotated)
                if delta not in distances:
                    distances[delta] = [0, []]
                distances[delta][0] += 1
                distances[delta][1].append((beacon1, beacon2_rotated))
        delta, (count, n) = [(delta, count) for delta, count in sorted(distances.items(), key=lambda x: -x[1][0])][0]
        if count >= OVERLAP_THRESHOLD:
            new_beacons = [beacon_rotate(beacon, rotation) for beacon in scanner2]
            return True, (new_beacons, delta)
    return False, (None, [])


# Find matching pairs to iterate over and avoid circular dependencies
print("Find matching pairs")
overlapping_beacon_pairs: list[list[int]] = []
for i, s1 in enumerate(scanners):
    for j, s2 in enumerate(scanners[i+1:], start=i+1):
        is_overlap, _ = scanner_overlap(s1[0], s2[0])
        if is_overlap:
            overlapping_beacon_pairs.append([s1[3], s2[3]])


# Create network of relative mappings between scanners
print("Creating network")
seen_scanners = set()
next_scan = {0}
while not all(scanner[1] is not None for scanner in scanners):
    for parent_scanner_id in (next_scan - seen_scanners).copy():
        parent_scanner = scanners[parent_scanner_id]
        for overlapping_pair in overlapping_beacon_pairs:
            if parent_scanner_id in overlapping_pair:
                other_scanner_id = overlapping_pair[parent_scanner_id == overlapping_pair[0]]
                if other_scanner_id in seen_scanners:
                    continue
                other_scanner = scanners[other_scanner_id]

                is_overlap, overlap_details = scanner_overlap(parent_scanner[0], other_scanner[0])

                scanners[other_scanner_id][0] = overlap_details[0]
                scanners[other_scanner_id][1] = parent_scanner_id
                scanners[other_scanner_id][2] = overlap_details[1]

                next_scan.add(other_scanner_id)

        seen_scanners.add(parent_scanner_id)

# Make all scanners relative position to scanner #0
print("Moving all scanners relative to #0")
while not all(scanner[1] == -1 for scanner in scanners):

    for i, scanner in enumerate(scanners):
        if scanner[1] != -1:
            parent_scanner = scanners[scanner[1]]
            if parent_scanner[1] == -1:
                scanners[i][1] = parent_scanner[1]
                scanners[i][2] = beacon_add(scanner[2], parent_scanner[2])

# Make all beacons relative to scanner #0
print("Moving all beacons relative to #0")
for i, scanner in enumerate(scanners):
    scanners[i][0] = [beacon_add(beacon, scanner[2]) for beacon in scanner[0]]

# Stick in set
print("Putting all beacons into stack")
all_beacons = set()

for scanner in scanners:
    for beacon in scanner[0]:
        all_beacons.add(beacon)

print(len(all_beacons))

for beacon in sorted(all_beacons):
    print(beacon)
