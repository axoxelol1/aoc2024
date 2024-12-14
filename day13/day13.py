from math import gcd
from typing import override


class Clawmachine:
    def __init__(self, ax: str, ay: str, bx: str, by: str, px: str, py: str):
        self.ax = int(ax)
        self.ay = int(ay)
        self.bx = int(bx)
        self.by = int(by)
        self.px = int(px)
        self.py = int(py)

    @override
    def __repr__(self):
        return f"Clawmachine({self.ax}, {self.ay}, {self.bx}, {self.by}, {self.px}, {self.py})"


with open("input.txt") as f:
    claws: list[Clawmachine] = []
    for claw in f.read().split("\n\n"):
        a, b, p = claw.strip().split("\n")
        ax, ay = a[12:].split(", Y+")
        bx, by = b[12:].split(", Y+")
        px, py = p[9:].split(", Y=")
        claws.append(Clawmachine(ax, ay, bx, by, px, py))

p1_total = 0
for claw in claws:
    gcd_x = gcd(claw.ax, claw.bx)
    gcd_y = gcd(claw.ay, claw.by)
    if claw.px % gcd_x == 0 and claw.py % gcd_y == 0:
        # Seperate equations for x and y are solvable
        b_press = int(
            (claw.ay * claw.px - claw.ax * claw.py)
            / (claw.bx * claw.ay - claw.by * claw.ax)
        )
        a_press = int((claw.py - b_press * claw.by) / claw.ay)
        x_right = a_press * claw.ax + b_press * claw.bx == claw.px
        y_right = a_press * claw.ay + b_press * claw.by == claw.py
        if not x_right or not y_right:
            continue
        cost = a_press * 3 + b_press
        if a_press <= 100 and b_press <= 100:
            p1_total += cost

print(p1_total)

p2_total = 0
for claw in claws:
    claw.px = claw.px + 10000000000000
    claw.py = claw.py + 10000000000000
    gcd_x = gcd(claw.ax, claw.bx)
    gcd_y = gcd(claw.ay, claw.by)
    if claw.px % gcd_x == 0 and claw.py % gcd_y == 0:
        # Seperate equations for x and y are solvable
        b_press = int(
            (claw.ay * claw.px - claw.ax * claw.py)
            / (claw.bx * claw.ay - claw.by * claw.ax)
        )
        a_press = int((claw.py - b_press * claw.by) / claw.ay)
        x_right = a_press * claw.ax + b_press * claw.bx == claw.px
        y_right = a_press * claw.ay + b_press * claw.by == claw.py
        if not x_right or not y_right:
            continue
        cost = a_press * 3 + b_press
        p2_total += cost

print(p2_total)
