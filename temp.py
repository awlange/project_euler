import math


def is_prime(n):

    # Gotta be > 1
    if n < 2:
        return False

    # Base for loop
    if n == 2:
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


def get_first_n_primes(n):



def main():
    primes = get_first_n_primes(10)
    print primes
    print sum(primes)


if __name__ == '__main__':
    main()