# Find the first four consecutive integers to have four
# distinct prime factors. What is the first of these numbers?

import time


# def get_primes_up_to(n):
#     prime_truths = [True for _ in range(n+1)]
#     i = 2
#     while i*i <= n:
#         if prime_truths[i]:
#             for j in range(i*i, n+1, i):
#                 prime_truths[j] = False
#         i += 1
#     primes = []
#     for i in range(2, n+1):
#         if prime_truths[i]:
#             primes.append(i)
#     return primes
def get_primes_up_to(n):
    """
    New, improved faster version
    """
    prime_list = [True for _ in xrange(n+1)]
    i = 3
    while i*i <= n:
        if prime_list[i]:
            for j in xrange(i*i, n+1, i):
                prime_list[j] = False
        i += 2

    primes = [2]
    for i in xrange(3, n+1, 2):
        if prime_list[i]:
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


def main():
    t_start = time.time()

    TARGET = 4

    i = 0

    max_n = 1000
    n_found = 0
    found = [0, 0, 0, 0]
    while n_found < TARGET:

        max_n *= 2
        primes = get_primes_up_to(max_n)

        while i < max_n:
            i += 1
            if i in primes:
                n_found = 0
                continue

            prime_factors = get_prime_factors(i, primes)

            if len(prime_factors) != TARGET:
                n_found = 0
                continue

            if len(set(prime_factors)) != TARGET:
                n_found = 0
                continue

            found[n_found] = i
            n_found += 1

            #print i, n_found, prime_factors

            if n_found == TARGET:
                break

    print found

    print "Run time: {}".format(time.time() - t_start)


if __name__ == '__main__':
    main()