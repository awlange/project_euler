"""
It can be verified that there are 23 positive integers less than 1000
that are divisible by at least four distinct primes less than 100.

Find how many positive integers less than 10^16 are divisible by at least
four distinct primes less than 100.
"""

import time


def get_primes_up_to(n):
    prime_truths = [True for _ in range(n+1)]
    i = 2
    while i*i <= n:
        if prime_truths[i]:
            for j in range(i*i, n+1, i):
                prime_truths[j] = False
        i += 1
    primes = []
    for i in range(2, n+1):
        if prime_truths[i]:
            primes.append(i)
    return primes


def get_prime_factors(x, primes):
    prime_factors = []
    # b/c 2 is smallest prime factor, we can cut out half
    x_half = x / 2
    for p in primes:
        if x % p == 0:
            prime_factors.append(p)
        if p > x_half:
            break
    return prime_factors


BIG_NUMBER = 100


def main():
    ts = time.time()

    primes = get_primes_up_to(100)
    print primes

    print "Run time: {}".format(time.time() - ts)

if __name__ == '__main__':
    main()