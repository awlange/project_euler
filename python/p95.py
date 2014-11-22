import sys

MAX_FACTOR = 10**6


def factorize_integers_up_to(n):
    """
    Proper divisors, so not including self for n
    """
    factors = [[1] for _ in xrange(n+1)]
    for i in xrange(2, n+1):
        m = 2*i
        # m = i
        while m < n+1:
            factors[m].append(i)
            m += i
    return factors


def get_chain(n, factors):
    # return if prime
    if len(factors[n]) == 1:
        return None

    chain = [n]
    m = n
    i = 0
    max_iters = 20
    # while 1 and i < max_iters:
    while 1:
        # i += 1
        m = sum(factors[m])
        if m == n:
            # amicable!
            return chain
        elif m > MAX_FACTOR:
            # exceeded limit
            return None
        elif len(factors[m]) == 1:
            # prime number is end of a non-amicable chain
            return None
        elif m in chain:
            # Ran into a perfect number, non-amicable chain
            return None
        chain.append(m)


def main():
    factors = factorize_integers_up_to(2*MAX_FACTOR)
    # for n in range(MAX_FACTOR+1):
    #     print n, factors[n]

    # print get_chain(12496, factors)

    if 1:
        longest_chain = []
        longest_chain_length = 0
        longest_chain_min = 0
        for n in xrange(1, 2*MAX_FACTOR+1):
            # print n
            chain = get_chain(n, factors)
            if chain and len(chain) >= longest_chain_length:
                longest_chain = chain
                longest_chain_length = len(chain)
                longest_chain_min = min(chain)

        print longest_chain_length, longest_chain_min, longest_chain
        # print longest_chain_length, longest_chain_min

if __name__ == '__main__':
    main()
