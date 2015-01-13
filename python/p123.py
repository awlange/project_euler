import math
import time


def generate_first_n_primes(n):
    """
    Low memory usage prime generator
    Surely not as fast as Sieve of Eratosthenes but still reasonably fast (25,000 in less than a second)
    Does not require O(N) memory or an upper bound
    """
    primes = []
    m = 1
    nn = n - 1  # 2 will be added at the end
    while len(primes) < nn:
        m += 2
        div = False
        root = math.sqrt(m)
        for p in primes:
            if p > root:
                break
            if m % p == 0:
                div = True
                break
        if not div:
            primes.append(m)

    # add 2
    return [2] + primes


def main():
    start = time.time()

    N_MAX = 25000
    primes = generate_first_n_primes(N_MAX)
    print "got primes"

    for nn in xrange(N_MAX):
        p = primes[nn]
        n = nn+1
        rem = ((p-1)**n + (p+1)**n) % (p * p)
        if rem > 10**10:
            print p, n
            break

    print time.time() - start


if __name__ == '__main__':
    main()