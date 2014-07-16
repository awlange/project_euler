import math


def is_prime(n):
    # Base for loop
    if n < 3:
        return True
    # Quick even check to let loop have stride of 2
    if n % 2 == 0:
        return False
    # Factorization bound
    sqrtn = int(math.sqrt(n))
    # Skip all even numbers b/c those are obviously not prime
    for i in range(3, sqrtn+1, 2):
        if n % i == 0:
            return False
    return True


MAX_DIGIT = 3

# 5 : 0
# 6 : 0
# 7 : 7652413
# 8 : 0
# 9 :


# Found on the interwebs
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def is_pandigital(sn):
    # Note: sn is a list of integers
    for i in range(1, len(sn)+1):
        if not i in sn:
            return False
    return True


def main():

    max_pan_prime = 2

    for max_digit in range(1, 10):
        print max_digit
        digits = [x for x in range(1, max_digit + 1)]
        for perm in all_perms(digits):
            n = int(''.join([str(x) for x in perm]))
            if is_prime(n) and n > max_pan_prime:
                max_pan_prime = n

    print 'Max pan prime found: {}'.format(max_pan_prime)



if __name__ == '__main__':
    main()
