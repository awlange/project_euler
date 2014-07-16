import time


def get_divisor_list(n_max):
    # Make a big old list of divisors, ignoring 1
    divlist = [[] for _ in range(n_max+1)]
    n = 2
    while n <= n_max:
        m = n
        while m <= n_max:
            divlist[m].append(n)
            m += n
        n += 1
    return divlist


def main():
    ts = time.time()

    d_max = 10000
    divlist = get_divisor_list(d_max)

    target_ratio = float(15499) / float(94744)
    # target_ratio = 0.4

    d = 2
    d_minus_1 = 1
    while True:
        if d % 10000 == 0:
            print d

        # Turn this into a sieve?
        # n_res = 1
        # for m in range(2, d):
        #     if not divlist[d].intersection(divlist[m]):
        #         n_res += 1

        # Sieve approach
        resilient_list = [1 for _ in range(d)]
        for n in divlist[d]:
            m = n
            while m < d:
                resilient_list[m] = 0
                m += n
        n_res = sum(resilient_list) - 1  # minus 1 b/c element 0 is left in there

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
            divlist = get_divisor_list(d_max)

    print "d: {}".format(d)
    print "time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()
