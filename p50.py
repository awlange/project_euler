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


# NOTE: This algorithm is too slow right now... should go back and figure out better approach
def main():
    primes = get_primes_up_to_n(1000000)
    #print primes

    n_primes = len(primes)
    max_prime = primes[n_primes-1]

    longest_prime = 0
    longest_length = 1

    i = n_primes
    while i > 0:
        i -= 1

        if i % 1000 == 0:
            print 'Progress: {}'.format(i)

        length = 1
        j = i
        psum = primes[j]
        while psum <= max_prime:
            length += 1
            j -= 1
            psum += primes[j]
            if length > longest_length and psum in primes:
                longest_length = length
                longest_prime = psum

    print longest_prime, longest_length


if __name__ == '__main__':
    main()