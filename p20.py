# Find the sum of the digits in the number factorial(100)

# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# 3628800


def factorial(n):
    # dumb factorial
    if n <= 1:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f


def main():
    for i in range(100, 101):
        f = factorial(i)
        f_orig = f
        d = 1
        total = 0
        while f > 0:
            n = f % 10
            print n
            total += n
            d *= 10
            f /= 10

        print f_orig, total


if __name__ == '__main__':
    main()