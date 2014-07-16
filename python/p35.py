# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?


def get_primes_up_to_n(n):
    # For convenience, let list be of size n+1, so that we can use list[n] as indexing.
    # For example, list[4] = false

    # Initialize all to true
    prime_list = [True for _ in range(n+1)]

    i = 2
    while i*i <= n:
        if prime_list[i]:
            for j in range(i*i, n+1, i):
                prime_list[j] = False
        i += 1

    return prime_list


def permute_string(s):
    t = s[len(s)-1]
    for i in range(0, len(s)-1):
        t += s[i]
    return t

LIMIT = 1000001

def main():

    num_circular = 0

    prime_list = get_primes_up_to_n(LIMIT)
    for i in range(2, LIMIT):
        if prime_list[i]:
            is_circular = True
            if i < 10:
                pass
            else:
                i_str = str(i)
                p = permute_string(i_str)
                while is_circular and p != i_str:
                    if not prime_list[int(p)]:
                        is_circular = False
                    p = permute_string(p)

            if is_circular:
                num_circular += 1

    print num_circular





if __name__ == '__main__':
    main()
