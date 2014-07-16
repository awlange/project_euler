import math

prime_cache = {2: True, 3: True, 5: True, 7: True}


def is_prime(n):

    if prime_cache.get(n, False):
        return True

    # Gotta be > 1
    # if n < 2:
    #     return False
    #
    # Base for loop
    # if n == 2:
    #     return True

    # Quick even check to let loop have stride of 2
    if n % 2 == 0:
        return False

    # Factorization bound
    sqrtn = int(math.sqrt(n))

    # Skip all even numbers b/c those are obviously not prime
    for i in range(3, sqrtn+1, 2):
        if n % i == 0:
            return False

    prime_cache[n] = True

    return True


from p27 import get_primes_up_to


def get_divisors(n):
    # Sqrt limit trick helps a lot
    divisors = [1, n]
    m = 2
    while m*m <= n:
        if n % m == 0:
            divisors.append(m)
            divisors.append(n/m)
        m += 1
    return divisors


def get_special_divisors(n):
    if not is_prime(n+1):
        return []

    divisors = [1, n]
    m = 2
    while m*m <= n:
        if n % m == 0:
            n_over_m = n/m
            if not is_prime(m + n_over_m):
                return []
            divisors.append(m)
            divisors.append(n_over_m)
        m += 1
    return divisors


def is_special_divisor_number(n, prime_map):
    if not prime_map[n+1]:
        return False

    m = 2
    while m*m <= n:
        if n % m == 0:
            if not prime_map.get(m + n/m, False):
                return False
        m += 1
    return True


def get_prime_truth_map_up_to(n):
    prime_truths = {2: True}

    # Skip even numbers to cut down on time and memory
    i = 3
    while i <= n:
        prime_truths[i] = True
        i += 2

    i = 3
    while i*i <= n:
        if prime_truths[i]:
            for j in range(i*i, n+1, i):
                if j % 2:  # ignore even numbers
                    prime_truths[j] = False
        i += 2

    return prime_truths


def main():
    MAX_NUM = 10**8 + 1
    prime_map = get_prime_truth_map_up_to(MAX_NUM)
    print "done getting primes"
    total = 1  # b/c 1 works, 1 + 1 = 2 which is prime

    # Only even numbered n's need to be iterated over b/c must have that n+1 is prime,
    # and the only even number for which that is true is 2
    for n in range(2, MAX_NUM, 2):
        if n % 10**6 == 0:
            print "{}...".format(n)
        if is_special_divisor_number(n, prime_map):
            total += n

    print total


if __name__ == '__main__':
    main()

