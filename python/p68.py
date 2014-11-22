import time

from p32 import all_permutations


def verify(rings):
    s1 = rings[5] + rings[0] + rings[1]
    s2 = rings[6] + rings[1] + rings[2]
    if s1 != s2:
        return False
    s3 = rings[7] + rings[2] + rings[3]
    if s2 != s3:
        return False
    s4 = rings[8] + rings[3] + rings[4]
    if s3 != s4:
        return False
    s5 = rings[9] + rings[4] + rings[0]
    if s4 != s5:
        return False
    return True


def get_tuples(rings):
    unsorted = [
        int(str(rings[5]) + str(rings[0]) + str(rings[1])),
        int(str(rings[6]) + str(rings[1]) + str(rings[2])),
        int(str(rings[7]) + str(rings[2]) + str(rings[3])),
        int(str(rings[8]) + str(rings[3]) + str(rings[4])),
        int(str(rings[9]) + str(rings[4]) + str(rings[0]))]
    # find index of lowest outer ring
    index = sorted([(rings[5], 0), (rings[6], 1), (rings[7], 2), (rings[8], 3), (rings[9], 4)])[0][1]
    return unsorted[index:] + unsorted[:index]


def get_tuple_string(rings):
    return ''.join([str(x) for x in get_tuples(rings)])


def main():
    start = time.time()

    valid_tuples = set()

    for rings in all_permutations(range(1, 11)):
        if verify(rings):
            t = get_tuple_string(rings)
            valid_tuples.add(t)

    print "The max: {}".format(max(valid_tuples))
    print "time: {}".format(time.time() - start)

if __name__ == '__main__':
    main()