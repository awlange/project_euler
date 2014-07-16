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


def get_radical_list_up_to(n_max):
    """
    Similar to above, but here we just multiply to get the rad
    """
    primes = get_primes_up_to(n_max)
    radicals = [1 for _ in range(n_max+1)]
    while len(primes) > 0:
        n = primes.pop()
        m = n
        while m <= n_max:
            radicals[m] *= n
            m += n
    return radicals


def main():
    radicals = get_radical_list_up_to(100000)
    sorted_radicals = []
    for n in range(len(radicals)):
        sorted_radicals.append((radicals[n], n))
    sorted_radicals.sort()

    print sorted_radicals[10000]


if __name__ == '__main__':
    main()