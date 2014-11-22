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

from p32 import all_permutations

cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}


def factorial(n):
    # slightly better factorial
    global cache
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

# 3 digits = 4 valid ways

# with no restrictions on leading zeroes, for 4 digits there are
# (4 places) * (16 digits) * (6 10A permutations) = 384 numbers
# with regard to the place=0, we should only have 15 digits b/c 6 are improper
# (4 * 16 * 6) - 6 = 378
# Then, the leading 0 permutations of 01A and 0A1 amount to
# (3 places) * (16 digits) * (2 permutations) = 96
# So that for 4 digits, there are this many hex numbers
# (4 * 16 * 6) - (6) - (3 * 16 * 2)  = 282 ways
# BUT, there are 24 valid redundant ways... 36 unrestricted redundant ways
# 282 - 24 = 258 valid ways

#       unres        leading 0 01A perm   equiv perms  16^(# *)   leading 0 from unres
#print ((factorial(4) - factorial(3)) / factorial(1)) * 16**1 - (factorial(3) / factorial(0)) * 16**0
#print ((factorial(5) - factorial(4)) / factorial(2)) * 16**2 - (factorial(4) / factorial(1)) * 16**1

#     (*, 0, 1, A) unrestricted               (0, 1, A) leading zero from the *       (*, 1, A) leading zero from 0
print (factorial(4) / factorial(1)) * 16**1 - (factorial(3) / factorial(0)) * 16**0 - (factorial(3) / factorial(1)) * 16**1
#     (*, *, 0, 1, A) unrestricted            (*, 0, 1, A) leading zero from the *    (*, *, 1, A) leading zero from 0
print (factorial(5) / factorial(2)) * 16**2 - (factorial(4) / factorial(1)) * 16**1 - (factorial(4) / factorial(2)) * 16**2

# 4 digits with 1, 0, and A. note: * = [0-F], . = [1-F]
# set = (*, 1, 0, A) fac(4) = 24
# -- always okay
# 10A*, 10*A, 1*0A, .10A
# 1A0*, 1A*0, 1*A0, .1AO
# A10*, A1*0, A*10, .A10
# A01*, A0*1, A*01, .A10
# -- not okay, except the last column
# 01A*, 01*A, 0*1A, .01A  set = (*, 1, A) assumed leading zero --> fac(3)
# 0A1*, 0A*1, 0*A1, .0A1
# -- redundancy of leading zeroes
# 0*1A, *01A --> 001A
# 0*A1, *0A1 --> 00A1

# For 5 digits
# set = (a, b, 1, 0, A) fac(5) = 120
# consider redundancy of swapping two *'s, as a and b
# 10Aab, 10Aba, 10aAb, 10bAa --> 10A**, 10*A*
# so need to divide by number of permutations, or fac(# of *'s)
# for set = (a, b, c, 1, 0, A)
# 10Aabc, 10Aacb, 10Abac, 10Abca, 10cab, 10cba --> 10A***
# .*01A and .*0A1 still okay b/c not unique, so no perm division there
# 0 | (*, *, 1, A)
# **01A


total = 4  # accounting for the 3 digit examples
nstars = 1
for n in range(4, 17):
    total +=  (factorial(n) / factorial(nstars)) * 16**nstars \
            - (factorial(n-1) / factorial(nstars-1)) * 16**(nstars-1) \
            - (factorial(n-1) / factorial(nstars)) * 16**nstars

    ur = 3 * factorial(n) / factorial(nstars+1)
    ir = 2 * factorial(n-1) / factorial(nstars+1) + factorial(n-1) / factorial(nstars)
    total -= ur - ir

    nstars += 1

print hex(total)

# Convert to hexadecimal
n = 1
while n < total:
    n *= 16
n /= 16

hexmap = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

result = ''
t = total
while n > 0:
    r = t / n
    result += hexmap.get(t / n)
    t -= r * n
    n /= 16
print "Answer:", result, total


# unres = []
# valid = set()
# redun = set()
# perms = all_permutations(['*', '0', '1', 'A'])
# for p in perms:
#     i = p.index('*')
#     for k, v in hexmap.iteritems():
#         s = p
#         s[i] = v
#         t = ''.join(s)
#
#         if t in unres:
#             redun.add(t)
#         unres.append(t)
#
#         if t[0] != '0':
#             valid.add(t)
#
# print len(valid)
#
# print len(redun)
# for x in redun:
#     print x

# 3 cases of redundant permutations: 0, 1, A
# for each (e.g. A), can appear in (A, A, 0, 1) --> fac(4) ways,
# divided by the number of redundant perms of A --> fac(2)
#print 3 * factorial(4) / factorial(2)

# Then, how many of those are invalid b/c of leading zeroes?
# 0|(a, a, 1)
# 0|(1, 1, a)
# 0|(0, 1, a) # no redundant zero here, but for more stars, yes there will be
#print 2 * factorial(3) / factorial(2) + factorial(3)

#ur = 3 * factorial(n) / factorial(nstars+1)
#ir = 2 * factorial(n-1) / factorial(nstars+1) + factorial(n-1) / factorial(nstars)