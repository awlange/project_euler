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

# Note: this works, but it is much too slow... the answer it eventually found is: 121313
# We need to look in the forums for a better way

import sys
import time
from p27 import get_primes_up_to
from p27 import is_prime

TARGET_FAMILY_SIZE = 8

found_families = []
lowest_prime = []


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


digits_list = [str(y) for y in range(0, 10)]


def search(n_digits, nums, occupied_positions, min_position):
    if len(occupied_positions) == n_digits-1 or min_position == n_digits:
        return

    for pos in range(min_position, n_digits):
        if pos in occupied_positions:
            continue

        for d in digits_list:
            sub_nums = substitute_digit(n_digits, nums, pos, d)
            if sub_nums and int(sub_nums[0]) >= lowest_prime[0]:
                continue

            filtered_nums = filter_to_keep_primes(sub_nums)
            if len(filtered_nums) == TARGET_FAMILY_SIZE:
                lowest_prime[0] = min(lowest_prime, filtered_nums[0])
                print filtered_nums, d, pos, min_position, occupied_positions, lowest_prime[0]
                found_families.append(filtered_nums)

            search(n_digits, sub_nums, occupied_positions + [pos], min_position + 1)


def main():
    ts = time.time()

    n_digits = 2
    while len(found_families) == 0:
        print "n_digits: {}".format(n_digits)
        nums = [''.join([str(x) for _ in range(0, n_digits)]) for x in range(0, 10)]
        lowest_prime.append(sys.maxint)
        search(n_digits, nums, [], 0)
        n_digits += 1

    print found_families

    print "Run time: {}".format(time.time() - ts)


if __name__ == '__main__':
    main()