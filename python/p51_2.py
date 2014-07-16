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

import sys
import time
from p27 import get_primes_up_to
from p27 import is_prime

TARGET_FAMILY_SIZE = 7

found_families = []


def substitute_digit(digits, nums, position, sub):
    sub_nums = []
    for num in nums:
        tmp = num[0:position] + sub + num[position+1:digits]
        if tmp[0] != '0':
            sub_nums.append(tmp)
    return sub_nums


def filter_to_keep_primes(nums):
    filter_nums = []
    for num in nums:
        n = int(num)
        if is_prime(n):
            filter_nums.append(n)
    return filter_nums


def search(digits, nums, occupied_positions, lowest_prime):
    if len(occupied_positions) == digits-1:
        return

    for pos in range(0, digits):
        if pos in occupied_positions:
            continue

        for d in [str(x) for x in range(0, 10)]:
            sub_nums = substitute_digit(digits, nums, pos, d)
            if sub_nums and int(sub_nums[0]) >= lowest_prime:
                continue

            filtered_nums = filter_to_keep_primes(sub_nums)
            if len(filtered_nums) >= TARGET_FAMILY_SIZE:
                if filtered_nums not in found_families:
                    print filtered_nums
                    lowest_prime = min(lowest_prime, filtered_nums[0])
                    found_families.append(filtered_nums)

            search(digits, sub_nums, occupied_positions + [d], lowest_prime)


def main():
    ts = time.time()

    digits = 5
    nums = [''.join([str(x) for _ in range(0, digits)]) for x in range(0, 10)]
    # print substitute_digit(digits, nums, 1, str(3))
    search(digits, nums, [], sys.maxint)

    print found_families

    print "Run time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()