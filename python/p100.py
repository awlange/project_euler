import math

from p45 import is_perfect_square
from p124 import get_prime_factor_list_up_to


def is_perfect_square_mod(x):
    """
    Rule: Perfect squares can only end in 0, 1, 4, or 9 in base 16
    Helps to avoid the sqrt call 75% of the time!
    """
    d = int(x & 0xF)
    if d > 9:
        return False
    if d != 2 and d != 3 and d != 5 and d != 6 and d != 7 and d != 8:
        return True  # possibly a perfect square
    return False


def is_integer(x):
    """
    Not accurate for large numbers... precision
    """
    return int(x) == int(math.ceil(x))


# # testing
# minimum = 2
# maximum = 120
# for n in range(minimum, maximum + 1):
#     rad = 1 + 2*(n * (n-1))
#     if is_perfect_square(rad):
#         b = (1 + int(math.sqrt(1 + 2*(n * (n-1))))) / 2
#         print rad, math.sqrt(rad), n, b
#
#
# for b in range(3, 86, 2):
#     rad = 1 + 8*(b * (b-1))
#     if is_perfect_square(rad):
#         n = (1 + int(math.sqrt(rad))) / 2
#         print rad, math.sqrt(rad), n, n-b, b

for r in range(1, 36):
    # bb = 1 + 4*r
    # rad = bb*bb - 8 * (r * (r + 1))
    rad = 1 + 8*r*r
    if is_perfect_square(rad):
        n = (1 + 4*r + int(math.sqrt(rad))) / 2
        b = n - r
        print rad, n, r, b

# THE KEY!!!
# r**2 is a triangle number and a perfect square
# there is a recursive formula for generating triangle numbers that are also perfect squares!

Sm_2 = 0
Sm_1 = 1
m = 2
# for m in range(2, 10):
while 1:
    Sm = 34*Sm_1 - Sm_2 + 2
    r = int(math.sqrt(Sm))
    n = (1 + 4*r + int(math.sqrt(1 + 8*r*r))) / 2
    b = n - r
    # rad = 1 + 8*Sm
    # r = (int(math.sqrt(rad)) - 1) / 2
    # n = (1 + 4*r + (2*r+1)**2) / 2
    # b = n - r
    print n, r, b
    if n > 10**12:
        break

    # prepare for next iter
    Sm_2 = Sm_1
    Sm_1 = Sm
    m += 1