"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the
first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of
this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.
"""

import time
from p27 import get_primes_up_to
from p27 import is_prime

TARGET_FAMILY_SIZE = 1


# end exclusive
def get_primes_in_range(begin, end):
    range_primes = []
    for p in get_primes_up_to(end):
        if begin <= p:
            range_primes.append(p)
    return range_primes


def filter_primes(string_primes, position, string_value):
    filtered = []
    for sp in string_primes:
        if sp[position] == string_value:
            filtered.append(sp)
    return filtered


def substitute_digit(primes, digits, nums, position, sub):
    sub_nums = []
    pp = position + 1
    if pp < digits:
        for num in nums:
            tmp = num[0:position] + sub + num[pp:digits]
            if tmp in primes:
                sub_nums.append(tmp)
    else:
        for num in nums:
            tmp = num[0:position] + sub
            if tmp in primes:
                sub_nums.append(tmp)
    return sub_nums


def search(primes, digits, nums, occupied_positions):
    sub_list = []
    for pos in range(0, digits):
        if pos in occupied_positions:
            continue
        current = primes
        for d in [str(x) for x in range(0, 10)]:
            sub_list = substitute_digit(current, digits, nums, pos, d)
            if len(sub_list) >= TARGET_FAMILY_SIZE:
                print sub_list


def main():
    ts = time.time()

    digits = 2
    primes = [str(p) for p in get_primes_in_range(10**(digits-1), 10**digits)]

    nums = [''.join([str(x) for _ in range(0, digits)]) for x in range(0, 10)]
    print substitute_digit(primes, digits, nums, 1, str(3))

    # search(primes, digits, nums, [])

    # for pos in range(0, digits):
    #     current = primes
    #     for d in [str(x) for x in range(0, 10)]:
    #         result = substitute_digit(current, digits, nums, pos, d)
    #         if len(result) >= TARGET_FAMILY_SIZE:
    #             print result




    print "Run time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()