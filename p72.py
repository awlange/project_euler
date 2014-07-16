import time

from p27 import get_primes_up_to


def farey(n):
    """
    Thanks for the help Wikipedia!
    Python function to print the nth Farey sequence, either ascending or descending.
    """
    a, b, c, d = 0, 1, 1, n
    print "%d/%d" % (a,b)
    while c <= n:
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        print "%d/%d" % (a,b)


def phi(n, primes=None):
    """
    totient function of n for general use later
    below, we use a sieve approach and don't use this function
    """
    if not primes:
        primes = get_primes_up_to(n)

    result = float(n)
    for p in primes:
        if p > n:
            break
        elif n % p == 0:
            result *= 1.0 - 1.0/float(p)
    return int(result)


def phi_float(n, primes=None):
    """
    totient function of n for general use later
    below, we use a sieve approach and don't use this function
    """
    if not primes:
        primes = get_primes_up_to(n)

    result = float(n)
    for p in primes:
        if p > n:
            break
        elif n % p == 0:
            result *= 1.0 - 1.0/float(p)
    return result


def main():
    start = time.time()
    # Using formula found on Wikipedia under Farery sequence

    MAX_N = 1000000
    primes = get_primes_up_to(MAX_N)
    prime_divs = [[] for _ in xrange(MAX_N+1)]
    for p in primes:
        m = p
        while m <= MAX_N:
            prime_divs[m].append(p)
            m += p

    # Now compute the totient for each using the provided primes, and compute the Farey length
    answer = 0
    for m in xrange(2, MAX_N + 1):
        totient = float(m)
        for p in prime_divs[m]:
            totient *= 1.0 - 1.0/float(p)
        answer += int(totient)

    print answer
    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()