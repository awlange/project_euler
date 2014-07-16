"""
In the hexadecimal number system numbers are represented using 16 different digits:

0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with all of the digits 0,1, and A present at least once?
Give your answer as a hexadecimal number.

(A,B,C,D,E and F in upper case, without any leading or trailing code that marks the number as hexadecimal and without leading zeroes , e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
"""

cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}


def factorial(n):
    # slightly better factorial
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    # Cache new results
    if f not in cache:
        cache[n] = f
    return f


def binomial(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))



# All permutation (minus the invalid ones)
# 10A
# 1A0
# A10
# A01
# 01A --
# 0A1 --

# print factorial(3) - factorial(2)
# print factorial(4) - factorial(3)

# Has to be at least 3 digits long...
# We know that there are 4 possibilites for 3 digits, so can start at 4 digits onward


