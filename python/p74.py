import time

factorial_map = {
    '0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120,
    '6': 720, '7': 5040, '8': 40320, '9': 362880
}


def main():

    start = time.time()
    sixties = 0

    cache = {}

    for m in xrange(3, 10**6):
        n = m
        non_repeats = []
        while n not in non_repeats:
            non_repeats.append(n)

            c = cache.get(n)
            if c:
                n = c
            else:
                x = n
                n = sum([factorial_map.get(d) for d in str(n)])
                cache[x] = n

        if len(non_repeats) == 60:
            sixties += 1

    print "n sixties: {}".format(sixties)
    print "time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()