"""
x**2 - Dy**2 = 1
x**2 = Dy**2 + 1
D is a positive integer. So, x > y.

(x**2 - 1)/D = y**2
Therefore, x**2 - 1 is a multiple of D. So, we can take steps of D stride?
Or, also (x**2 - 1) % D = 0

(x**2 - 1)/y**2 = D
"""

from p45 import is_perfect_square
import math
import time


def solve(D):
    # Assumed that if D is square, there is no solution.
    if is_perfect_square(D):
        return None

    max_iter = 10000
    #
    # y = 0
    # while y < max_iter:
    #     y += 1
    #     x2 = D * y*y + 1
    #     if is_perfect_square(x2):
    #         return int(math.sqrt(x2))

    # x = 1
    # while x < max_iter:
    #     x += 1
    #     if not (x*x - 1) % D:
    #         if is_perfect_square((x*x - 1)/D):
    #             return x

    x = 1
    while x < max_iter:
        x += 1
        if not (x*x - 1) % D:
            if is_perfect_square((x*x - 1)/D):
                return x


def main():
    start = time.time()

    largest_x = 0

    # print solve(61)

    max_D = 7
    D = 2
    while D <= max_D:
        x = solve(D)
        print x
        if x and x > largest_x:
            largest_x = x
        D += 1

    print "Largest x: {}".format(largest_x)

    print "time: {}".format(time.time() - start)

if __name__ == '__main__':
    main()