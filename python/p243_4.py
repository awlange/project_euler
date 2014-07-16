import time
from p27 import get_primes_up_to
from p72 import phi_float



def main():
    start = time.time()

    MAX_N = 10**8
    target = 15499.0 / 94744.0
    # target = 4.0 / 10.0
    print "Target: {}".format(target)

    # primes = get_primes_up_to(MAX_N)
    primes = get_primes_up_to(1000)[:15]  # First so many?
    print primes
    print "Done with primes: {}".format(time.time() - start)

    totients = [float(n) for n in xrange(MAX_N+1)]
    for p in primes:
        m = p
        x = 1.0 - 1.0/float(p)
        while m <= MAX_N:
            totients[m] *= x
            m += p

    print "Done with totients: {}".format(time.time() - start)

    for d in xrange(2, MAX_N + 1):
        totient = totients[d]
        if totient < target * float(d-1):
            resilience = totient / float(d-1)
            print "Found: {}/{} = {}".format(int(totient), d-1, resilience)
            print "Denominator: {}".format(d)
            break

    print "Time: {}".format(time.time() - start)


def prod(l):
    p = 1
    for e in l:
        p *= e
    return p


def main2():
    start = time.time()

    MAX_N = 29
    target = 15499.0 / 94744.0
    # target = 4.0 / 10.0
    print "Target: {}".format(target)

    # primes = get_primes_up_to(MAX_N)
    primes = get_primes_up_to(MAX_N)  # First hundred only?

    totient_product = 1.0  # just the (1-1/p) product part of the totient
    p_list = []
    for p in primes:
        p_list.append(p)
        totient_product *= 1.0 - 1.0/float(p)

    print totient_product, p_list

    d = prod(p_list)
    d *= 1

    totient = d * totient_product
    resilience = totient / float(d-1.0)
    print "d: {} totient: {} resilience: {}".format(d, totient, resilience)
    print resilience < target


    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()

# Some Reasoning:
# First totient product that falls below 15499.0 / 94744.0 if all primes in sequence are included
# 0.163588195356 [2, 3, 5, 7, 11, 13, 17, 19, 23]
# d/(d-1) approaches 1 for large d
# So, prime_product is 223092870
# Now, just multiply by the primes until d*totient_product/(d-1) < 15499.0 / 94744.0
# Which is accomplished simply by multiplying by 5
# But, it's not the answer: 1,115,464,350  <-- an upper bound at least
# So, it must be that a few of those primes aren't in that list, like [2, 3, 11, ...]
# But, we probably don't too many primes, b/c as the primes get larger the value of (p-1)/p gets closer to one.
#
# d * tp/(d-1) < x
# d * tp < x * (d-1)
# tp < x*(d-1)/d
