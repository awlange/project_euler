"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import time
from p27 import get_primes_up_to, is_prime


def check_condition(pi, pj, pair_map=None):
    return is_prime(int(pi + pj)) and is_prime(int(pj + pi))


def add_to_map(pi, pj, pair_map):
    tmp = pair_map.get(pi)
    if not tmp:
        tmp = set()
    tmp.add(pj)
    pair_map[pi] = tmp
    return pair_map


def search(primes):
    """
    Brute force search. Scales like shit! But works!
    """

    # for i in xrange(len(primes)):
    for i in xrange(100):
        pi = primes[i]
        # for j in xrange(i+1, len(primes)):
        for j in xrange(i+1, len(primes)):
            pj = primes[j]
            if check_condition(pi, pj):
                for k in xrange(j+1, len(primes)):
                    pk = primes[k]
                    if check_condition(pi, pk) and check_condition(pj, pk):
                        for l in xrange(k+1, len(primes)):
                            pl = primes[l]
                            if check_condition(pi, pl) and check_condition(pj, pl) and check_condition(pk, pl):
                                # return pi, pj, pk, pl
                                for m in xrange(l+1, len(primes)):
                                    pm = primes[m]
                                    if check_condition(pi, pm) and check_condition(pj, pm):
                                        if check_condition(pk, pm) and check_condition(pl, pm):
                                            return pi, pj, pk, pl, pm


def main():

    start = time.time()
    prime_max = 8000

    while True:
        iter_time = time.time()
        prime_max *= 2
        primes = get_primes_up_to(prime_max)
        print "prime max: {}".format(prime_max)
        found = search([str(p) for p in primes])
        if found:
            print "Found: {} Sum: {}".format(found, sum([int(x) for x in found]))
            break
        else:
            print "Not found. time: {}".format(time.time() - iter_time)

    print "Run time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()