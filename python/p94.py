"""
Heron's formula for isosceles triangle area (T)
a = length of equal sides
b = length of unequal side
T = (b/4) * sqrt(4*a^2 - b^2)

T^2 = (b/4)^2 * (4*a^2 - b^2)
(T*4)^2 = b^2 * (4*a^2 - b^2)

If area must be an integer, then must meet following conditions:
    1. sqrt() is an integer (i.e. radicand is a perfect square)
        1a. 4|b
        1b. 4|sqrt()
    2. (T/4)^2 is a perfect square
        2a. 16|b^2
        2b. 16|(4*a^2 - b^2)

1.
b = a+1, a-1
PS = 4*a^2 - b^2

# plus case
PS = 4*a^2 - (a+1)^2
PS = 4*a^2 - a^2 - 2*a - 1
PS = 3*a^2 - 2*a - 1
0 = 3*a^2 - 2*a - (PS+1)

a = [2 + sqrt(4 + 4*3*(PS+1))] / 6
a = [2 + 2 * sqrt(1 + 3*(PS+1))] / 6
a = [1 + sqrt(4 + 3*PS)] / 3

a = [1 + sqrt(4 + 3*PS))] / 3
a = [1 - sqrt(4 + 3*PS))] / 3  # will always be negative, can ignore

# minus case
PS = 4*a^2 - (a-1)^2
PS = 4*a^2 - a^2 + 2*a - 1
PS = 3*a^2 + 2*a - 1
0 = 3*a^2 + 2*a - (PS+1)

a = [-2 + sqrt(4 + 4*3*(PS+1))] / 6

a = [-1 + sqrt(4 + 3*PS)] / 3
a = [-1 - sqrt(4 + 3*PS)] / 3  # will always be negative, can ignore


T = (b/4) * sqrt(4*a^2 - b^2)
T = ((a+1)/4) * sqrt(4*a^2 - (a+1)^2)
T = ((a+1)/4) * sqrt(4*a^2 - a^2 - 2*a - 1)
T = ((a+1)/4) * sqrt(3*a^2 - 2*a - 1)
T = sqrt[(3*a^2 - 2*a - 1) * (a+1)^2] / 4
T = sqrt[(3*a^2 - 2*a - 1) * (a^2 + 2*a + 1)] / 4


p = 3*a +- 1
p = 3*a + 1
a = (p-1)/3
a = (p+1)/3

p <= THRESH
3*a +- 1 <= THRESH
3*a <= THRESH +- 1

# One is odd, other is even, so only need to iterate over every other (++2). empirically, 2|b
b = a+1 -> a = b-1
b = a-1 -> a = b+1

T = (b/4) * sqrt(4*a^2 - b^2)
# plus
T = (b/4) * sqrt(4*(b+1)^2 - b^2)
T = (b/4) * sqrt(4*(b^2 + 2*b + 1) - b^2)
T = (b/4) * sqrt[3*b^2 + 8*b + 4]
# let 2|b, such that 2*c = b
T = (2*c/4) * sqrt[12*c^2 + 16*c + 4]
T = c * sqrt[3*c^2 + 4*c + 1]  <- radicand must be perfect square, empirically must also be divisible by 9 if not 3|c

# minus
T = (b/4) * sqrt(4*(b-1)^2 - b^2)
T = (b/4) * sqrt(4*(b^2 - 2*b + 1) - b^2)
T = (b/4) * sqrt[3*b^2 - 8*b + 4]
# let 2|b, such that 2*c = b
T = (2*c/4) * sqrt[12*c^2 - 16*c + 4]
T = c * sqrt[3*c^2 - 4*c + 1]  <- radicand must be perfect square, empirically must also be divisible by 9 if not 3|c
"""

import math
from p45 import is_perfect_square


def main():
    # Iterate through perfect squares to find valid a values, check conditions met

    total = 0

    too_big = False

    THRESH = 10**6

    p = 2
    while not too_big:
        p += 1
        PS = p*p
        radicand = 4 + 3*PS
        if is_perfect_square(radicand):
            root = int(math.sqrt(radicand))

            if (1 + root) % 3 == 0:
                a = (1 + root) // 3
                b = a + 1
                r = 4*a*a - b*b
                if is_perfect_square(r):
                    perim = 2*a + b
                    total += perim
                    print(p, a, b, (b * math.sqrt(4*a*a - b*b)) / 4)
                    if perim > THRESH:
                        too_big = True

            if (-1 + root) % 3 == 0:
                a = (-1 + root) // 3
                b = a - 1
                r = 4*a*a - b*b
                if is_perfect_square(r):
                    perim = 2*a + b
                    total += perim
                    print(p, a, b, (b * math.sqrt(4*a*a - b*b)) / 4)
                    if perim > THRESH:
                        too_big = True

    print(total)

def main2():
    total = 0

    too_big = False

    THRESH = 10**9

    c = 1
    while not too_big:
        c += 1
        b = 2*c
        if 3*b > THRESH:
            too_big = True

        tmp = 3*c*c + 1

        if c % 3 == 0:
            # plus
            radicand = tmp + 4*c
            if is_perfect_square(radicand):
                a = b+1
                total += 2*a + b
                print(a, b, (b * math.sqrt(4*a*a - b*b)) / 4)

            # minus
            radicand = tmp - 4*c
            if is_perfect_square(radicand):
                a = b-1
                total += 2*a + b
                print(a, b, (b * math.sqrt(4*a*a - b*b)) / 4)
        else:
            # plus
            radicand = tmp + 4*c
            if radicand % 9 == 0 and is_perfect_square(radicand):
                a = b+1
                total += 2*a + b
                print(a, b, (b * math.sqrt(4*a*a - b*b)) / 4)

            # minus
            radicand = tmp - 4*c
            if radicand % 9 == 0 and is_perfect_square(radicand):
                a = b-1
                total += 2*a + b
                print(a, b, (b * math.sqrt(4*a*a - b*b)) / 4)

    print(total)

if __name__ == "__main__":
    # main()
    main2()
