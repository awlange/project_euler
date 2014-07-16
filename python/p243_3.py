import time


def get_primes_up_to(n):
    prime_truths = [True for _ in range(n+1)]
    i = 2
    while i*i <= n:
        if prime_truths[i]:
            for j in range(i*i, n+1, i):
                prime_truths[j] = False
        i += 1
    primes = []
    for i in range(2, n+1):
        if prime_truths[i]:
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


def get_prime_factor_list_up_to(n_max):
    primes = get_primes_up_to(n_max)
    prime_factors = [[] for _ in range(n_max+1)]
    while len(primes) > 0:
        n = primes.pop()
        m = n
        while m <= n_max:
            prime_factors[m].append(n)
            m += n
    return prime_factors


def main():
    ts = time.time()

    d_max = 100000
    prime_factors = get_prime_factor_list_up_to(d_max)

    target_ratio = float(15499) / float(94744)
    # target_ratio = 0.4

    d = 2
    d_minus_1 = 1
    while True:
        if d % 10000 == 0:
            print d

        # Sieve approach
        resilient_list = [1 for _ in range(d)]
        for n in prime_factors[d]:
            m = n
            while m < d:
                resilient_list[m] = 0
                m += n
        n_res = sum(resilient_list) - 1  # minus 1 b/c element 0 is left in there

        # print d, n_res, float(n_res) / float(d_minus_1)

        # Avoid a division flop by multiplying
        if float(n_res) / float(d_minus_1) < target_ratio or d >= d_max:
        # if float(n_res) < target_ratio * float(d_minus_1):
            break

        d_minus_1 = d
        d += 1

        # Check if d is too big
        if d > d_max:
            d_max *= 2
            print "re-upping... {}".format(d_max)
            primes = get_primes_up_to(d_max)


    print "d: {}".format(d)
    print "time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()
