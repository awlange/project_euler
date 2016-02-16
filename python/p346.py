import time
import pprint

pp = pprint.PrettyPrinter(indent=4)


def repunits(b, n):
    """
    Returns the decimal number for which in base b there are n repeated units.
    e.g. 111 in base 2 (n=3) is 7
    """
    return (b**n - 1) / (b - 1)


def main():
    """
    First pass. Too slow to work for 10**12
    """
    foo = {}
    MAXIMUM = 50
    ts = time.time()
    for b in range(2, MAXIMUM):
        n = 2
        r = repunits(b, n)
        foo[r] = foo.get(r, 0) + 1
        while r < MAXIMUM:
            n += 1
            r = repunits(b, n)
            foo[r] = foo.get(r, 0) + 1

    pp.pprint(foo)

    filtered = {n: c for n, c in foo.iteritems() if c > 1}
    pp.pprint(filtered)
    print sum(filtered.keys())
    print time.time() - ts


def main2():
    """
    The good solution. Iteration over n for each base as long as we are below max. Use set in case of multiples.
    Though, apparently only 31 and 8191 are the only numbers which would appear more than once.
    """
    ts = time.time()

    MAXIMUM = 10**12
    nums = set()

    n = 3
    while True:
        b = 2
        r = repunits(b, n)
        if r >= MAXIMUM:
            break
        while r < MAXIMUM:
            nums.add(r)
            b += 1
            r = repunits(b, n)
        n += 1

    # pp.pprint(nums)
    print(sum(nums) + 1)

    print time.time() - ts


if __name__ == "__main__":
    main2()
