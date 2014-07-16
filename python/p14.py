# Seed number under 1 million with the longest Collatz sequence
# n even -> n/2
# n odd _ 3*n + 1

# Use >> to divide by 2
# Can probably memoize some of the first so many numbers

LIMIT = 1000000
CACHE_LIMIT = 200000
cache = {}


def get_next(n):
    if n % 2 == 0:
        return n >> 1
    return 3*n + 1


def get_collatz(n):
    # Check storage
    if n < CACHE_LIMIT and n in cache:
        return cache[n]

    n_orig = n
    length = 1
    while n != 1:
        n = get_next(n)

        # Check storage
        if n < CACHE_LIMIT and n in cache:
            length += cache[n]
            n = 1
        else:
            length += 1

    # Store lengths with n_orig under 10000
    if n_orig < CACHE_LIMIT:
        cache[n_orig] = length

    return length


def main():
    longest = 0
    seed = 0
    for n in range(1, LIMIT):
        col = get_collatz(n)
        if longest < col:
            longest = col
            seed = n
    print "Longest found: seed = ", seed, " length =", longest

if __name__ == '__main__':
    main()
