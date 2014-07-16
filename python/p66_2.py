"""
Must use Chakravala method
x**2 - D*y**2 = 1
"""

from p45 import is_perfect_square
import sys


def method(D):
    if is_perfect_square(D):
        return None, None

    # Starting
    # Must have gcd(a, b) = 1
    a = 8
    b = 1
    k = a*a - D*b*b

    i = 0
    while True:
        i += 1

        # find m
        m = 0
        absk = k if k > 0 else -k
        prev = sys.maxint
        min_m = sys.maxint
        while True:
            m += 1
            if (a + b*m) % absk == 0:
                diff = m*m - D
                if diff < 0:
                    diff = -diff
                if diff < prev:
                    prev = diff
                    min_m = m
                else:
                    break

        m = min_m

        # scaled down
        new_a = (a*m + D*b) / absk
        new_b = (a + b*m) / absk
        new_k = (m*m - D) / k

        a = new_a
        b = new_b
        k = new_k

        if k == 1:
            return a, b


def main():

    max_x = 0
    special_D = 0
    for D in range(2, 1001):
        x, y = method(D)
        if x and x > max_x:
            max_x = x
            special_D = D

    print "Max x found: {}".format(max_x)
    print "Special D: {}".format(special_D)


if __name__ == '__main__':
    main()