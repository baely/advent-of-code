def triangle(n: int) -> int:
    return n * (n + 1) // 2


def inverse_triangle(n: int) -> float:
    return ((8 * n + 1) ** (1/2) - 1) / 2


with open("input.txt") as f:
    box_x, box_y = [list(map(int, t.split(".."))) for t in f.read().replace("\n", "")[15:].split(", y=")]

valid_count = 0

for x_velocity in range(max(box_x) + 1):
    for y_velocity in range(min(min(box_y), abs(max(box_y))), max(max(box_y), abs(min(box_y))) + 1):
        this_max_y = triangle(y_velocity)
        y_down_min = int(-(-inverse_triangle(this_max_y - max(box_y))//1) + 1)
        y_down_max = int(inverse_triangle(this_max_y - min(box_y))//1 + 1)
        steps_y = set(y_velocity + x for x in range(y_down_min, y_down_max + 1))
        steps_y |= set(2 * y_velocity - y + 1 for y in steps_y)

        if not steps_y:
            continue

        this_max_x = triangle(x_velocity)
        x_up_min = (x_velocity - int(inverse_triangle(this_max_x - min(box_x))//1)) if min(box_x) <= this_max_x else (max(steps_y) + 1)
        x_up_max = (x_velocity - int(-(-inverse_triangle(this_max_x - max(box_x))//1))) if max(box_x) <= this_max_x else (max(steps_y) + 1)
        steps_x = set(x for x in range(x_up_min, x_up_max + 1) if x >= 0)

        if steps_x & steps_y:
            valid_count += 1


print(valid_count)
