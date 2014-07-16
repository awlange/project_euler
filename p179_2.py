import time

from p179 import get_number_of_divisors


def get_divisor_map(n_max):
    # Make a big old map of divisors
    divmap = {}
    n = 1
    while n <= n_max:
        m = n
        while m <= n_max:
            divmap[m] = divmap.get(m, 0) + 1
            m += n
        n += 1
    return divmap


def get_divisor_list(n_max):
    # Make a big old list of divisors
    divlist = [0] * (n_max + 1)
    n = 1
    while n <= n_max:
        m = n
        while m <= n_max:
            divlist[m] += 1
            m += n
        n += 1
    return divlist


def main():
    ts = time.time()

    n_max = 10**7
    divlist = get_divisor_list(n_max)

    n_pairs = 0

    n = 2
    n_div_prev = 1
    while n <= n_max:
        n_div_this = divlist[n]
        if n_div_this == n_div_prev:
            n_pairs += 1
        n_div_prev = n_div_this
        n += 1

    print "n_pairs: {}".format(n_pairs)
    print "time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()