import json
from typing import Union


class SnailFish:
    SPLIT_AMT = 10

    def __init__(self, parent: Union[None, "SnailFish"],  left: Union[int, list, "SnailFish"], right: Union[int, list, "SnailFish"]):
        self.parent = parent
        self.left = left if not isinstance(left, list) else SnailFish(self, *left)
        self.right = right if not isinstance(right, list) else SnailFish(self, *right)

    def get_depth(self) -> int:
        left_depth = 1 if isinstance(self.left, int) else self.left.get_depth() + 1
        right_depth = 1 if isinstance(self.right, int) else self.right.get_depth() + 1
        return max(left_depth, right_depth)

    def get_max_regular(self) -> int:
        left_depth = self.left if isinstance(self.left, int) else self.left.get_max_regular()
        right_depth = self.right if isinstance(self.right, int) else self.right.get_max_regular()
        return max(left_depth, right_depth)

    def get_magnitude(self) -> int:
        left_mag = 3 * (self.left.get_magnitude() if isinstance(self.left, SnailFish) else self.left)
        right_mag = 2 * (self.right.get_magnitude() if isinstance(self.right, SnailFish) else self.right)
        return left_mag + right_mag

    def reduce(self):
        while (to_explode := self.get_left_at_depth(4)) or (to_split := self.get_left_splittable()):
            if to_explode is not None:
                to_explode.explode()
            elif to_split is not None:
                to_split.split()

    def explode(self):
        left_pair, left_pair_right = self.get_regular_to_left()
        right_pair, right_pair_right = self.get_regular_to_right()
        if left_pair is not None:
            left_pair.inc_regular(left_pair_right, self.left)
        if right_pair is not None:
            right_pair.inc_regular(right_pair_right, self.right)
        if self.parent.left is self:
            self.parent.left = 0
        if self.parent.right is self:
            self.parent.right = 0

    def inc_regular(self, right: bool, amt: int) -> None:
        if right:
            self.right += amt
        else:
            self.left += amt

    def split(self):
        if isinstance(self.left, int) and self.left >= SnailFish.SPLIT_AMT:
            left_amt, right_amt = self.left // 2, -(-self.left // 2)
            new_snail_fish = SnailFish(self, left_amt, right_amt)
            self.left = new_snail_fish
            return
        if isinstance(self.right, int) and self.right >= SnailFish.SPLIT_AMT:
            left_amt, right_amt = self.right // 2, -(-self.right // 2)
            new_snail_fish = SnailFish(self, left_amt, right_amt)
            self.right = new_snail_fish
            return

    def get_left_at_depth(self, depth: int) -> Union[None, "SnailFish"]:
        if depth == 0:
            return self
        if isinstance(self.left, SnailFish):
            left_most = self.left.get_left_at_depth(depth - 1)
            if left_most is not None:
                return left_most
        if isinstance(self.right, SnailFish):
            left_most = self.right.get_left_at_depth(depth - 1)
            if left_most is not None:
                return left_most
        return None

    def get_left_splittable(self) -> Union[None, "SnailFish"]:
        if isinstance(self.left, int):
            if self.left >= SnailFish.SPLIT_AMT:
                return self
        else:
            if self.left.get_left_splittable() is not None:
                return self.left.get_left_splittable()
        if isinstance(self.right, int):
            if self.right >= SnailFish.SPLIT_AMT:
                return self
        else:
            if self.right.get_left_splittable() is not None:
                return self.right.get_left_splittable()
        return None

    def get_regular_to_left(self) -> (Union[None, "SnailFish"], bool):
        head = self
        while head.parent is not None and head.parent.left is head:
            head = head.parent
        if head.parent is None:
            return None, False
        if isinstance(head.parent.left, int):
            return head.parent, False
        head = head.parent.left
        while isinstance(head.right, SnailFish):
            head = head.right
        return head, True

    def get_regular_to_right(self) -> ("SnailFish", bool):
        head = self
        while head.parent is not None and head.parent.right is head:
            head = head.parent
        if head.parent is None:
            return None, False
        if isinstance(head.parent.right, int):
            return head.parent, True
        head = head.parent.right
        while isinstance(head.left, SnailFish):
            head = head.left
        return head, False

    def __add__(self, other):
        if isinstance(other, SnailFish):
            new_snail_fish = SnailFish(None, self, other)
            self.parent = new_snail_fish
            other.parent = new_snail_fish
            new_snail_fish.reduce()
            return new_snail_fish

    def __radd__(self, other):
        if other is None:
            return self
        if isinstance(other, SnailFish):
            return other + self

    def __str__(self):
        return f"[ {self.left}, {self.right} ]"

    def __repr__(self):
        return str(self)


snail_fish: list[SnailFish] = []

with open("input.txt") as f:
    r = f.readlines()
    for row in r:
        a = json.loads(row)
        snail_fish.append(SnailFish(None, *a))

for s in snail_fish:
    s.reduce()

print(sum(snail_fish, None).get_magnitude())
