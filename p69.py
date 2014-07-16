"""
Looking up how to compute the Totient function, phi(n), find that
it can be done as a product of factors involving
all primes that divide n for phi(n). So, program that.
"""

from p27 import get_primes_up_to


def main():

    MAX_N = 10**6
    primes = get_primes_up_to(MAX_N)
    n_over_phi = [1.0 for _ in xrange(MAX_N+1)]

    for p in primes:
        fp = float(p)
        x = fp / (fp - 1.0)
        q = p
        while q <= MAX_N:
            n_over_phi[q] *= x
            q += p

    max_totient = 0.0
    max_n = 0
    for n in xrange(MAX_N+1):
        if n_over_phi[n] > max_totient:
            max_totient = n_over_phi[n]
            max_n = n

    print "Max totient n: {}".format(max_n)

if __name__ == '__main__':
    main()