from p268 import get_primes_up_to

import math


def is_prime(n):

    # Gotta be > 1 <-- guaranteed true here
    # if n < 2:
    #     return False

    # Base for loop
    # if n == 2: <-- guaranteed false here
    #     return True

    # Quick even check to let loop have stride of 2
    if not n % 2:
        return False

    # Factorization bound
    sqrtn = int(math.sqrt(n))

    # Skip all even numbers b/c those are obviously not prime
    for i in range(3, sqrtn+1, 2):
        if n % i == 0:
            return False

    return True


def get_next_prime(prime_list, n, current_prime):
    if n <= current_prime:
        return current_prime
    prime = prime_list.pop(0)
    while n > prime:
        prime = prime_list.pop(0)
        if not prime_list:
            prime_list = get_primes_up_to(2*n)
    return prime, prime_list


def main():
    FOUR = [1, 2, 3, 4]
    prime_list = get_primes_up_to(1024)


    # length = step + 1
    step = 2
    n = 9
    n_diagonals = 5
    n_primes = 3

    # next_prime = get_next_prime(prime_list, n, 7)

    while True:
        step += 2
        for _ in FOUR:
            n += step

            # next_prime, prime_list = get_next_prime(prime_list, n, next_prime)
            # if n == next_prime:
            if is_prime(n):
                n_primes += 1

        n_diagonals += 4

        ratio = float(n_primes) / float(n_diagonals)
        print step+1, n_primes, n_diagonals, ratio
        if ratio < 0.1:
            print "length: {}".format(step+1)
            break


if __name__ == '__main__':
    main()