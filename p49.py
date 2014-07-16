import time


# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit
# numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# 1) Get all 4-digit primes
# 2) Filter out ones that do not have 3 permutations
# 3) Look for the special 3 primes

def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def all_perms_as_int(string):
    int_perms = []
    for p in all_perms(string):
        int_perms.append(int(''.join(p)))
    return int_perms


def get_primes_up_to(n):
    prime_truths = [True for _ in range(n+1)]
    i = 2
    while i*i <= n:
        if prime_truths[i]:
            for j in range(i*i, n+1, i):
                prime_truths[j] = False
        i += 1

    primes = []
    for i in range(2, n+1):
        if prime_truths[i]:
            primes.append(i)

    return primes


def filter_by_4digits(nums):
    filtered_nums = []
    for num in nums:
        if 999 < num < 10000:
            filtered_nums.append(num)
    return filtered_nums


def filter_by_permutation(nums):
    filtered_nums = []
    for num in nums:
        perms_found = 0
        for perm in all_perms_as_int([d for d in str(num)]):
            if perm in nums:
                perms_found += 1
                if perms_found == 3:
                    filtered_nums.append(num)
                    break
    return filtered_nums


def get_triplets(nums):
    triplet = []
    for i in range(0, len(nums)):
        ni = nums[i]
        ni_perms = all_perms_as_int([d for d in str(ni)])
        for j in range(i+1, len(nums)):
            nj = nums[j]
            if nj in ni_perms:
                for k in range(j+1, len(nums)):
                    nk = nums[k]
                    if nk in ni_perms:
                        diff_nj_ni = nj - ni
                        diff_nk_nj = nk - nj
                        if diff_nj_ni == diff_nk_nj:
                            triplet.append((ni, nj, nk))
    return triplet


def main():
    t_start = time.time()

    primes_4digits = filter_by_4digits(get_primes_up_to(9999))
    primes_perms = filter_by_permutation(primes_4digits)
    print get_triplets(primes_perms)


    print "Run Time = {} seconds".format(time.time() - t_start)


if __name__ == '__main__':
    main()