import time


def get_number_of_divisors(n):
    n_divisors = 2
    m = 2
    while m*m <= n:
        if n % m == 0:
            n_divisors += 2
        m += 1
    return n_divisors


def main():

    ts = time.time()

    n_pairs = 0

    n = 2
    n_divisors_prev = 1
    while n <= 10**5:

        n_divisors_this = get_number_of_divisors(n)
        if n_divisors_prev == n_divisors_this:
            n_pairs += 1

        n_divisors_prev = n_divisors_this
        n += 1

    print n_pairs

    print "time: {}".format(time.time() - ts)

if __name__ == '__main__':
    main()