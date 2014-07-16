"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely
of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such
numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in
either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""

import time


def contains_odd_digit(sx):
    if '1' in sx or '3' in sx or '5' in sx or '7' in sx or '9' in sx:
        return True
    return False


def contains_even_digit(sx):
    if '0' in sx or '2' in sx or '4' in sx or '6' in sx or '8' in sx:
        return True
    return False


start = time.time()

n_reversible = 0
n = 0
while n < 10**6:
    # 2
    n += 2  # Can take stride 2 because must have that is n odd, then reverse(n) even and vice versa
    rn = int(str(n)[::-1])
    x = n + rn
    if x % 2 and not contains_even_digit(str(x)):
        # print n, rn, x
        n_reversible += 2

    # 4
    n += 2  # Can take stride 2 because must have that is n odd, then reverse(n) even and vice versa
    rn = int(str(n)[::-1])
    x = n + rn
    if x % 2 and not contains_even_digit(str(x)):
        # print n, rn, x
        n_reversible += 2

    # 6
    n += 2  # Can take stride 2 because must have that is n odd, then reverse(n) even and vice versa
    rn = int(str(n)[::-1])
    x = n + rn
    if x % 2 and not contains_even_digit(str(x)):
        # print n, rn, x
        n_reversible += 2

    # 8 --> skip 10 because can't have ending in zero... saving a modulus operation with unrolling
    n += 4  # Can take stride 2 because must have that is n odd, then reverse(n) even and vice versa
    rn = int(str(n)[::-1])
    x = n + rn
    if x % 2 and not contains_even_digit(str(x)):
        # print n, rn, x
        n_reversible += 2


print n_reversible

print "Time: {}".format(time.time() - start)