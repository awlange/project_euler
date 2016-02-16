from p124 import get_primes_up_to, get_prime_factor_list_up_to

import time

def main():
    ts = time.time()

    # N = 30
    N = 10**8

    total = 0

    primes = get_primes_up_to(N / 2 + 1)
    for i, p in enumerate(primes):
        for j in xrange(i, len(primes)):
            pq = p * primes[j]
            if pq >= N:
                break
            else:
                total += 1

    print total

    print time.time() - ts


if __name__ == "__main__":
    main()
