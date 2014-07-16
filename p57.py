import math
import time


def add_fraction_to_x(x, (num, denom)):
    x = x * denom
    return num + x, x


def add_fractions((n_a, d_a), (n_b, d_b)):
    d = d_a * d_b
    n = n_a * d_b + n_b * d_a
    return n, d


def invert((n, d)):
    return d, n


def add_to_denom(d, (n_b, d_b)):
    return add_fractions((d, 1), (n_b, d_b))


# sqrt(2) continued fraction
# 3/2, 7/5, 17/12, 41/29
def sqrt2():

    n_with_more_numerator_digits = 0

    f = (1, 2)
    for i in range(1, 1001):
        # print i, add_fraction_to_x(1, f)
        g = add_fraction_to_x(1, f)
        if len(str(g[0])) > len(str(g[1])):
            n_with_more_numerator_digits += 1

        f = invert(add_fractions((2, 1), f))

    print n_with_more_numerator_digits

    # print 12, add_fraction_to_x(1, f)
    # print "approx: {}".format(1 + float(f[0]) / float(f[1]))
    # print "real: {}".format(math.sqrt(2))


def main():
    ts = time.time()
    sqrt2()
    print "Time: ", time.time() - ts

if __name__ == '__main__':
    main()