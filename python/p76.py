# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

# Researching, found that we want a "partition" of n: p(n)
# And found that the answer is actually p(100) = 190,569,292
# Now, before submitting that, let's see that we can actually compute that number
# However, I'm pretty sure that includes 100, so the answer is really 190,569,291 I think

# Sweet, I found this gem on Wikipedia:
# This theorem can be used to derive a recurrence for the partition function:
#
# p(k) = p(k-1) + p(k-2) - p(k-5) - p(k-7) + p(k-12) + ...
# where p(0) is taken to equal 1, and p(k) is taken to be zero for negative k.
# The sign of each term is (-1)^m, with m coming from a generalized pentagonal number defined by
# gpn = m(3m-1)/2 for m any integer
# p(0) = 1


# 6
# 5 + 1
# 4 + 2
# 4 + 1 + 1
# 3 + 3
# 3 + 2 + 1
# 3 + 1 + 1 + 1
# 2 + 2 + 2
# 2 + 2 + 1 + 1
# 2 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1 + 1

# 5
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1

# 3
# 2 + 1
# 1 + 1 + 1

# 2
# 1 + 1

# 1


# Cache of partitions that we'll bootstrap up to 100
partition_cache = {
    0: 1,
    1: 1
    # 2: 2,
    # 3: 3,
    # 4: 5,
    # 5: 7,
    # 6: 11
}


def gpn(m):
    """
    Generalized pentagonal number
    m can be negative
    gpn: m = (1, -1, 2, -2, 3, ...) = (1, 2, 5, 7, 12, ...)
    so alternate n, -n, n+1, -(n+1), ... to get increasing gpn
    """
    return (m * (3*m - 1)) / 2


def partition(n):
    if n < 0:
        return 0
    if n in partition_cache:
        return partition_cache[n]
    m = 1
    g = gpn(m)
    p = 0
    while n >= g:
        s = int(-(-1)**m)  # sign for this term
        p += s * partition(n - g)

        # update, alternating positive then negative to get increasing gpn
        m = -m if m > 0 else -m+1
        g = gpn(m)

    # update cache
    partition_cache[n] = p
    return p


def main():
    # subtract 1 to not include 100 b/c want partitions of 2 or more terms
    print partition(100) - 1

if __name__ == '__main__':
    main()