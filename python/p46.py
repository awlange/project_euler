# p < m
# m = p + 2*x*x
# (m - p)/2 = x*x

import math


def get_primes_up_to_n(n):
    # For convenience, let list be of size n+1, so that we can use list[n] as indexing. (1 based indexing)
    # For example, list[4] = false
    # Initialize all to true
    prime_list = [True for _ in range(n+1)]
    i = 2
    while i*i <= n:
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
        i += 1

    primes = []
    for i in range(2, n+1):
        if prime_list[i]:
            primes.append(i)

    return primes


def is_perfect_square(x):
    t = (int)(math.sqrt(x))
    return t*t == x


# p < m
# m = p + 2*x*x
# (m - p)/2 = x*x
def composite_number_check(m, prime_list):
    # assume m is an odd composite number
    result = False
    i = 0
    p = prime_list[i]
    while p <= m and not result:
        m_p = m - p
        if m_p % 2 == 0:
            if is_perfect_square(m_p/2):
                result = True
        i += 1
        p = prime_list[i]

    return result


def main2():
    smallest = 1
    max_prime = 1000

    # Searching for odd composite numbers
    i = 33
    while smallest == 1:
        prime_list = get_primes_up_to_n(max_prime)
        # Search up to max prime
        while i < max_prime:
            if i not in prime_list:
                if not composite_number_check(i, prime_list):
                    smallest = i
                    break
            i += 2

        # If not found, then we expand our max prime for next iteration
        max_prime *= 2
        print max_prime

    print "Smallest: {}".format(smallest)

if __name__ == '__main__':
    main2()