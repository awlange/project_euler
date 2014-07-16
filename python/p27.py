import math


def is_prime(n, prime_list=None):

    # # Gotta be > 1  ## Assumed true always here
    # if n < 2:
    #     return False

    # Base for loop
    if n == 2:
        return True

    # Quick even check to let loop have stride of 2
    if n % 2 == 0:
        return False

    # # Check if in the prime list first
    # if prime_list and n in prime_list:
    #     return True

    # Factorization bound
    sqrtn = int(math.sqrt(n))

    # Skip all even numbers b/c those are obviously not prime
    for i in range(3, sqrtn+1, 2):
        if n % i == 0:
            return False

    return True


# def get_primes_up_to(n):
#     prime_truths = [True for _ in range(n+1)]
#     i = 2
#     while i*i <= n:
#         if prime_truths[i]:
#             for j in range(i*i, n+1, i):
#                 prime_truths[j] = False
#         i += 1
#
#     primes = []
#     for i in range(2, n+1):
#         if prime_truths[i]:
#             primes.append(i)
#
#     return primes
def get_primes_up_to(n):
    """
    New, improved faster version
    """
    prime_list = [True for _ in xrange(n+1)]
    i = 3
    while i*i <= n:
        if prime_list[i]:
            for j in xrange(i*i, n+1, i):
                prime_list[j] = False
        i += 2

    primes = [2]
    for i in xrange(3, n+1, 2):
        if prime_list[i]:
            primes.append(i)

    return primes


def main():

    primes_1000 = get_primes_up_to(1000)
    # Add in the negative range
    primes_1000.extend([-x for x in primes_1000])

    # Since n=0 at start, b must be prime
    # Given the prompt, expect that the max should be equal or above 40
    # consecutive n's, so the following must be prime:
    # 1521 + 39*a + b

    most = 0
    keep_a = 0
    keep_b = 0
    for a in range(-1000, 1001):
        for b in primes_1000:
            if is_prime(1521 + 39*a + b):
                n = 0
                while 1:
                    m = n*(n + a) + b
                    if not is_prime(m):
                        break
                    n += 1
                if n > most:
                    most = n
                    keep_a = a
                    keep_b = b

    print most, keep_a, keep_b, keep_a * keep_b



if __name__ == '__main__':
    main()