def power_sum(n):
    m = str(n)
    total = 0
    for i in m:
        j = int(i)
        jj = j*j
        total += jj * jj
    return total

cache = {}
for i in range(0, 10):
    cache[i] = power_sum(i)

print cache


def power_sum_cache(n):
    m = str(n)
    total = 0
    for i in m:
        total += cache[int(i)]
    return total


def main():
    MIN_NUM = 2
    # Multiply by number of digits b/c 9, 90, 900, 9000, ...
    # all have the same power digit sum. However, once 9(0) goes
    # beyond power sum of 9, then we know that we cannot produce
    # a power digit sum that high. So, that's the max.
    MAX_NUM = power_sum_cache(9) * len(str(power_sum_cache(9)))
    total = 0
    print MIN_NUM, MAX_NUM
    for i in range(MIN_NUM, MAX_NUM):
        if power_sum_cache(i) == i:
            total += i
    print total

if __name__ == '__main__':
    main()