import time
import math


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def main():

    start = time.time()
    limit_upper = 0.5
    limit_lower = 1.0 / 3.0

    # fractions = []
    n_fractions = 0
    for d in xrange(2, 12000 + 1):
        fd = float(d)
        inv_fd = 1.0 / fd

        # n = d / 2   # Start out at half and move back into window
        # approximate 1/2 for the given d, then move back
        n = int(math.ceil(fd * limit_upper))
        while True:
            val = float(n) * inv_fd
            if limit_lower < val < limit_upper:
                if gcd(n, d) == 1:
                    # fractions.append((val, n, d))
                    n_fractions += 1
            elif val < limit_lower:
                break
            n -= 1

    print "N fractions: {}".format(n_fractions)
    # print "sorting..."
    #
    # fractions.sort()
    # for i in range(len(fractions)):
    #     if fractions[i][1] == 3 and fractions[i][2] == 7:
    #         print fractions[i-1]
    #         break

    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()