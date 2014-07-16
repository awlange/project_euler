def factorial(n):
    # dumb factorial
    if n <= 1:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f


def binomial(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))


def main():
    n = 20
    print binomial(2*n, n)


if __name__ == '__main__':
    main()