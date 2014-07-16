import time

cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}


def factorial(n):
    # slightly better factorial
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    # Cache new results
    if f not in cache:
        cache[n] = f
    return f


def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def main():

    t_start = time.time()

    millions = 0
    for n in range(23, 101):
        for r in range(1, n/2 + n % 2 + 1):
            if binomial(n, r) > 1000000:
                millions += (n - 2*r) + 1
                break

    print "Millions found: {}".format(millions)

    print "Run time: {} seconds".format(time.time() - t_start)

if __name__ == '__main__':
    main()