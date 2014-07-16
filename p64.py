import math


def gcd((a, b)):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def reduce((a, b)):
    g = gcd((a, b))
    return a/g, b/g


def digit_sum(n):
    m = 0
    while n > 0:
        d = n % 10
        n /= 10
        m += d
    return m


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
    f = (1, 2)
    for i in range(1, 11):
        print i, add_fraction_to_x(1, f)
        f = invert(add_fractions((2, 1), f))

    print i+1, add_fraction_to_x(1, f)
    print "approx: {}".format(1 + float(f[0]) / float(f[1]))
    print "real: {}".format(math.sqrt(2))


def e():
    one = (1, 1)
    two = (2, 1)
    f = (0, 1)



if __name__ == '__main__':
    e()