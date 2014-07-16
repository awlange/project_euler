import time
import sys
from p27 import get_primes_up_to


def bucketize(n):
    sn = str(n)
    buckets = [0 for _ in xrange(10)]
    for digit in sn:
        buckets[int(digit)] += 1
    return buckets


def equal_buckets(a, b):
    for n in xrange(10):
        if a[n] != b[n]:
            return False
    return True


def main():
    start = time.time()
    MAX_N = 10**7
    primes = get_primes_up_to(MAX_N)
    print "Done with primes: {}".format(time.time() - start)

    totients = [float(n) for n in xrange(MAX_N+1)]
    for p in primes:
        m = p
        x = 1.0 - 1.0/float(p)
        while m <= MAX_N:
            totients[m] *= x
            m += p
    print "Done with totients: {}".format(time.time() - start)

    minimum = (float(sys.maxint), 0)
    for n in xrange(2, MAX_N+1):
        ratio = float(n) / totients[n]
        if ratio < minimum[0]:
            if equal_buckets(bucketize(n), bucketize(int(totients[n]))):
                # print n, ratio
                minimum = (ratio, n)

    print "Min: {}".format(minimum)
    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()