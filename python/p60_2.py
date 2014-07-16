"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import time
from p27 import get_primes_up_to, is_prime


def check_condition(pi, pj):
    # pi and pj are strings
    return is_prime(int(pi + pj)) and is_prime(int(pj + pi))


def search(prime_max):

    primes = get_primes_up_to(prime_max)

    # Using full list of primes, do the N^2 loop to create new list of
    # pairs of primes that satisfy the concat property. Using that list,
    # find 3-mers. Using that list, find 4-mers. Get the minimum sum. If none found,
    # increase max prime, and retry.

    pair_map = {}
    for i in range(len(primes)):
        pi = primes[i]
        spi = str(pi)
        tmp_list = []
        for j in range(i+1, len(primes)):
            if i == j:
                continue
            pj = primes[j]
            spj = str(pj)
            if check_condition(spi, spj):
                tmp_list.append(spj)

        if len(tmp_list) >= 3:
            pair_map[spi] = tmp_list

    # print pair_map

    found = []

    for spi in pair_map:
        pi_set = pair_map.get(spi)
        for j in range(len(pi_set)):
            spj = pi_set[j]
            for k in range(j+1, len(pi_set)):
                spk = pi_set[k]
                if check_condition(spj, spk):
                    for l in range(k+1, len(pi_set)):
                        spl = pi_set[l]
                        if check_condition(spj, spl) and check_condition(spk, spl):
                            # found.append([spi, spj, spk, spl])
                            for m in range(l+1, len(pi_set)):
                                spm = pi_set[m]
                                if check_condition(spj, spm) and check_condition(spk, spm) and check_condition(spl, spm):
                                    found.append([spi, spj, spk, spl, spm])

    return found


def main():

    start = time.time()
    prime_max = 1000
    found = []

    while len(found) == 0:
        iter_time = time.time()
        prime_max *= 2
        print prime_max,
        found = search(prime_max)
        print "time: {}".format(time.time() - iter_time)

    print found

    print "Run time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()

