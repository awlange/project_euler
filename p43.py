import time


def all_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_permutations(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


primes = [2, 3, 5, 7, 11, 13, 17]
def digit_test(sn):
    if int(sn[1:4]) % 2 != 0:
        return False
    if int(sn[2:5]) % 3 != 0:
        return False
    if int(sn[3:6]) % 5 != 0:
        return False
    if int(sn[4:7]) % 7 != 0:
        return False
    if int(sn[5:8]) % 11 != 0:
        return False
    if int(sn[6:9]) % 13 != 0:
        return False
    if int(sn[7:]) % 17 != 0:
        return False
    return True


def main():
    t_start = time.time()

    total = 0

    # Get all permutations of pandigitals
    for perm in all_permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        if perm[0] == '0':
            continue
        sn = ''.join(perm)
        if digit_test(sn):
            total += int(sn)

    print total

    print "Run time: {}".format(time.time() - t_start)

if __name__ == '__main__':
    main()