"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number,
134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

# Note: for x^n, must have 1 <= x < 10 because 10^1 has 2 digits and same for all x > 10
# but still need to include 1 because 1^1 = 1 satisfies the condition

import math


def is_perfect_power(x, p):
    """
    We don't need this function for this problem, but maybe we will for others
    """
    t = int(math.pow(x, 1.0/p))
    return t**int(p) == x


num_positive_integers_satisfy = 0

for x in range(1, 10):
    n = 1
    xp = x
    num_positive_integers_satisfy += 1
    print x, n, xp
    while True:
        xp *= x
        n += 1
        if len(str(xp)) != n:
            break
        print x, n, xp
        num_positive_integers_satisfy += 1

print num_positive_integers_satisfy