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

    # Value is one minus actual target
    target_convergent = 99
    k = target_convergent / 3

    if target_convergent % 3 == 0:
        pass
    elif target_convergent % 3 == 1:
        f = invert(add_fractions(one, f))
    elif target_convergent % 3 == 2:
        f = invert(add_fractions((2*(k+1), 1), f))
        f = invert(add_fractions(one, f))

    while k > 0:
        f = invert(add_fractions(one, f))
        f = invert(add_fractions((2*k, 1), f))
        f = invert(add_fractions(one, f))
        k -= 1

    final_fraction = add_fractions(two, f)

    print "Convergent {}: {}".format(target_convergent+1, final_fraction)
    print "approx: {}".format(float(final_fraction[0]) / float(final_fraction[1]))
    print "real: {}".format(math.exp(1))

    print "numerator digit sum: {}".format(digit_sum(final_fraction[0]))

if __name__ == '__main__':
    e()