cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}
MAX_NUM = cache[9] + 1


def factorial(n):
    # dumb factorial
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f


def factorial_sum(n):
    m = str(n)
    total = 0
    for i in m:
        total += cache[int(i)]
    return total


def main():

    sum_of_nums = 0
    for n in range(10, MAX_NUM):
        if factorial_sum(n) == n:
            sum_of_nums += n

    print sum_of_nums


if __name__ == '__main__':
    main()