# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


import time


def get_primes_up_to_n(n):
    # For convenience, let list be of size n+1, so that we can use list[n] as indexing.
    # For example, list[4] = false

    # Initialize all to true
    prime_truths = [True for _ in range(n+1)]

    i = 2
    while i*i <= n:
        if prime_truths[i]:
            for j in range(i*i, n+1, i):
                prime_truths[j] = False
        i += 1

    # Only keep the trues
    primes = []
    for i in range(2, n+1):
        if prime_truths[i]:
            primes.append(i)

    return primes

single_digit_primes = ['2', '3', '5', '7']

TARGET_FOUND = 11

def main():
    t_start = time.time()

    max_prime = 2000
    last_p = 10
    truncatable_primes = []

    while len(truncatable_primes) < TARGET_FOUND:
        max_prime *= 2
        print truncatable_primes, max_prime
        primes = get_primes_up_to_n(max_prime)

        for p in primes:
            if p < last_p:
                continue
            last_p = p

            # Check left-most and right-most digits
            sp = str(p)
            if sp[0] not in single_digit_primes:
                continue
            elif sp[len(sp)-1] not in single_digit_primes:
                continue

            # Attempt to truncate from the left
            left_truncatable = True
            while len(sp) > 1:
                sp = sp[1:]
                if int(sp) not in primes:
                    left_truncatable = False
                    break

            if left_truncatable:
                # Attempt to truncate from the left
                right_truncatable = True
                sp = str(p)
                while len(sp) > 1:
                    sp = sp[:len(sp)-1]
                    if int(sp) not in primes:
                        right_truncatable = False
                        break

                if right_truncatable:
                    truncatable_primes.append(p)

            if len(truncatable_primes) == TARGET_FOUND:
                break


    print "Primes found: {}".format(truncatable_primes)
    print "Prime sum: {}".format(sum(truncatable_primes))

    print "Run time: {}".format(time.time() - t_start)

if __name__ == '__main__':
    main()