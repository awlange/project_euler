# P_j and P_k where sum and difference is pentagonal and D = |P_k - P_j| is minimized. What is D?

# Corollary: Find first j-k combo where the sum and difference are pentagonal.

def pen(n):
    return (3*n*n - n) / 2

MAXIMUM = 3000

# Warm cache
pen_cache = [pen(n) for n in range(1, MAXIMUM)]
pen_cache_2 = [2*p for p in pen_cache]
# pen_cache_half = []
# for p in pen_cache:
#     if p % 2 == 0:
#         pen_cache_half.append(p/2)


def slow_way():
    done = False
    for pd in pen_cache:
        psi = pen_cache.index(pd) + 1
        while psi < MAXIMUM-1:
            ps = pen_cache[psi]
            pd_plus_ps = pd + ps
            if pd_plus_ps % 2 == 0:
                ps_minus_pd = ps - pd
                if ps_minus_pd % 2 == 0:
                    if pd_plus_ps / 2 in pen_cache and ps_minus_pd / 2 in pen_cache:
                        pk = pd_plus_ps / 2
                        pj = ps_minus_pd / 2
                        print pd, ps, pd_plus_ps, pk, pj, pk in pen_cache, pj in pen_cache
                        done = True
                        break
            psi += 1
        if done:
            break

# Answer: 5482660
# But our code was pretty slow... can improve? MAX 3000 was good enough
# 5482660 8602840 14085500 7042750 1560090 True True


# Take advantage of of knowing that the sum of two odd numbers is even and so is the sum of two even numbers
def slow_way2():
    done = False
    for pd in pen_cache:
        psi = pen_cache.index(pd) + 1
        while psi < MAXIMUM-1:
            ps = pen_cache[psi]
            if pd + ps in pen_cache_2 and ps - pd in pen_cache_2:
                pk = (pd + ps) / 2
                pj = (ps - pd) / 2
                print pd, ps, pd + ps, ps - pd, pk, pj, pk in pen_cache, pj in pen_cache
                done = True
                break
            psi += 1
        if done:
            break

#slow_way2()

#### Below here is a solution from the forum that was nice that I wish I had thought of!

import time
tStart = time.time()
from math import sqrt

def is_pent_num(number):
    # This test was derived by rearranging the pentagonal number formula.
    # If the number is pentagonal, the result must be a whole number.
    return (1 + sqrt(1 + 24 * number))/6 % 1 == 0


pentagonal_numbers = set([1])
found = False
n = 2

while not found:
    pn = n*(3*n - 1)/2
    for i in pentagonal_numbers:
        d = pn - i
        if d in pentagonal_numbers and is_pent_num(pn + i):
            print d
            found = True
            break

    pentagonal_numbers.add(pn)
    n += 1

print "Run Time = " + str(time.time() - tStart)