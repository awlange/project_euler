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
    limit_upper = 3.0 / 7.0
    limit_lower = 0.42857

    fractions = [(limit_upper, 3, 7)]
    for d in xrange(2, 10**6 + 1):
        fd = float(d)
        inv_fd = 1.0 / fd

        # n = d / 2   # Start out at half and move back into window
        # approximate 3/7 for the given d, then move back
        n = int(math.ceil(fd * limit_upper))
        while True:
            val = float(n) * inv_fd
            if limit_lower < val < limit_upper:
                if gcd(n, d) == 1:
                    fractions.append((val, n, d))
            elif val < limit_lower:
                break
            n -= 1


    print "sorting..."

    fractions.sort()
    for i in range(len(fractions)):
        if fractions[i][1] == 3 and fractions[i][2] == 7:
            print fractions[i-1]
            break

    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()