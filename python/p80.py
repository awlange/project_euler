"""
For each n [1-100] that has an irrational sqrt,
compute the sum of the first 100 decimal digits of sqrt(n) and sum the total of those sums.

Note: All roots here will be < 10 except for sqrt(100)=10, whose decimal digit sum is just 0.
      So, we'll just go up to sqrt(99) and assume that all roots only have one digit to the left of the
      decimal point.
"""


def find_x_y(c, p):
    x = 9
    y = x * (20 * p + x)
    while y > c:
        x -= 1
        y = x * (20 * p + x)
    return x, y


def root_digits(n):
    digits = [int(d) for d in str(n)]
    i = 0

    p = 0
    c = digits[i]
    i += 1
    if i < len(digits):
        c = 10*c + digits[i]
        i += 1
    x, y = find_x_y(c, p)
    rem = c - y
    p = x
    if rem == 0 and i >= len(digits):
        return 0  # not irrational

    for _ in range(99):
        c = rem * 100
        if i < len(digits):
            c += digits[i] * 10
            i += 1
            if i < len(digits):
                c += digits[i]
        x, y = find_x_y(c, p)
        rem = c - y
        p = 10*p + x
        if rem == 0 and i >= len(digits):
            return 0  # not irrational

    return p


def main():
    skip = [n**2 for n in range(10)]
    total = 0
    for n in range(2, 100):
        if n not in skip:
            total += sum([int(d) for d in str(root_digits(n))])
    print total



if __name__ == '__main__':
    main()