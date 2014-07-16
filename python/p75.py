"""
12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly
one integer sided right angle triangle be formed?
"""

from p27 import get_primes_up_to
import math
import time

# a^2 + b^2 = c^2
# a < b < c < L
# a^2 < b^2 < c^2 < L^2
# L = a + b + c

# because a < b < c and L = a + b + c,
# at most, L ~ 3*a, which means L/3 <= a, defines maximum to search over

# c = L - (a + b)
# c^2 = [L - (a + b)]^2 = L^2 - 2*L*(a+b) + (a + b)^2
# a^2 + b^2 = L^2 - 2*L*(a+b) + (a + b)^2
# a^2 + b^2 = L^2 - 2*L*(a+b) + a^2 + 2*a*b + b^2
# 0 = L^2 - 2*L*(a+b) + 2*a*b

# L = [2*(a+b) + sqrt{4(a+b)^2 - 8*a*b}] / 2
# 2L = 2*(a+b) + sqrt{4(a+b)^2 - 8*a*b}
# 2L = 2*(a+b) + 2*sqrt{(a+b)^2 - 2*a*b}
# 2L = 2*(a+b) + 2*sqrt{a^2 + 2*a*b + b^2 - 2*a*b}
# L = (a+b) + sqrt{a^2 + b^2}  # derp
# L^2 = (a+b)^2 + 2*(a+b)*sqrt{a^2 + b^2} + (a^2 + b^2)


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

cache = {}
L_cache = []
a_cache = []

# MAXIMUM = 49  # 6
# MAXIMUM = 1500  # 161
# MAXIMUM = 15000  # 1663
# MAXIMUM = 150000  # 16414
MAXIMUM = 1500000  # 161667
MAXIMUM_THIRD = MAXIMUM / 3
MAXIMUM_SQUARED = MAXIMUM * MAXIMUM


def main():
    t_start = time.time()

    # Get primitive triangles by using the Pythagorean triplets
    # Use Euclid's formula!
    # Must have that n and m are co-prime and m - n is odd to guarantee a Pythagorean triplet
    n = 0
    n2 = 0
    while n2 < MAXIMUM_SQUARED:
        n += 1
        n2 = n*n
        m = n
        while 1:
            m += 1
            if not gcd(n, m) == 1 or not (m - n) % 2:
                continue
            m2 = m*m
            a = m2 - n2
            b = 2*m*n
            c = m2 + n2
            L = a + b + c
            if L > MAXIMUM:
                break

            # Get similar triangles
            orig_L = L
            while L <= MAXIMUM:
                cache[L] = cache.get(L, 0) + 1
                L += orig_L


    total = 0
    for L in cache:
        if cache[L] == 1:
            total += 1

    print total

    print "Run time: {}".format(time.time() - t_start)


def main4():
    t_start = time.time()

    for a in xrange(3, MAXIMUM_THIRD):
        if a in a_cache:
            continue
        a2 = a*a
        for b in xrange(a+1, MAXIMUM / 2):
            radical = math.sqrt(a2 + b*b)
            if not radical % 1:
                # probably need to avoid redundant work here...

                L = a + b + int(radical)

                # Get similar triangles
                orig_L = L
                aa = a
                while L <= MAXIMUM:
                    cache[L] = cache.get(L, 0) + 1
                    L += orig_L
                    a_cache.append(aa)
                    aa += a

    total = 0
    for L in cache:
        if cache[L] == 1:
            total += 1

    print total

    print "Run time: {}".format(time.time() - t_start)


def main3():
    t_start = time.time()

    for a in range(1, MAXIMUM):
        a2 = a*a
        for b in range(a+1, MAXIMUM):
            b2 = b*b
            c2 = a2 + b2
            c = int(math.sqrt(c2))
            if c*c == c2:
                L = a + b + c
                cache[L] = cache.get(L, 0) + 1


    total = 0
    for L in cache:
        if cache[L] == 1:
            total += 1

    print total

    print "Run time: {}".format(time.time() - t_start)


def main2():
    t_start = time.time()

    valid_L_values = 0

    # Meh... this is cubic w/r L

    for L in range(3, MAXIMUM):
        n_solutions = 0
        for a in range(1, L / 3):
            a2 = a*a
            for b in range(a+1, L / 3):
                c = L - (a + b)
                if c < 1:
                    break
                c2 = c*c
                b2 = b*b
                a2_plus_b2 = a2 + b2
                if a2_plus_b2 > c2:
                    break
                elif a2_plus_b2 == c2:
                    n_solutions += 1

                # Only want the L's for which there is only one solution
                if n_solutions > 1:
                    break

        if n_solutions == 1:
            valid_L_values += 1

    print valid_L_values
    print "Run time: {}".format(time.time() - t_start)


if __name__ == '__main__':
    main()
