"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import time
from p27 import get_primes_up_to, is_prime


def check_concat_property(stack):
    prime_group = [p[0] for p in stack]

    if len(prime_group) == 1:
        return True

    for i in range(len(prime_group)):
        pi = str(prime_group[i])
        for j in range(i+1, len(prime_group)):
            pj = str(prime_group[j])
            if not (is_prime(int(pi + pj)) and is_prime(int(pj + pi))):
                return False
    return True


def find_primes_that_add_up_to_n(n, primes):
    """
    Try finding 4 primes that add up to n for now, make 5 later
    """
    stack = []
    m = n
    i = len(primes) - 1
    while m > 0 and i >= 0:
        pi = primes[i]

        if i == 0 and m - pi != 0:
            # Backtrack
            # Clear whole stack?
            tmp = stack[0]
            i = tmp[1] - 1
            pi = primes[i]
            stack = []
            m = n

        if pi > m:
            i -= 1
            continue

        m -= pi
        stack.append((pi, i))
        if not check_concat_property(stack):
            stack.pop()
            m += pi

        if i == 0 and m != 0:
            # Backtrack
            # Clear whole stack?
            tmp = stack[0]
            i = tmp[1] - 1
            pi = primes[i]
            stack = []
            m = n

        i -= 1

    return stack if not m else None


def main():

    start = time.time()
    prime_max = 5000
    primes = get_primes_up_to(prime_max)

    # stack = [(3, 0), (7, 0), (109, 0), (673, 0)]
    # print check_concat_property(stack, primes)

    # group = find_primes_that_add_up_to_n(792, primes)
    # print find_primes_that_add_up_to_n(17, [2, 3, 5, 7, 11])

    n = 10
    group = []
    while True:
        n += 1

        print n

        if n >= prime_max:
            prime_max *= 2
            primes = get_primes_up_to(prime_max)

        group = find_primes_that_add_up_to_n(n, primes)
        if group and len(group) == 5:
            break


    print group
    print sum([g[0] for g in group])

    print "Run time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()