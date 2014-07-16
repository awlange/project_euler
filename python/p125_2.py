import math
from p55 import is_palindrome

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
TWO_DIGIT_PALINDROMES = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']


def get_palindromes_with_n_digits(n_digits):
    if n_digits <= 0:
        return None
    if n_digits % 2:
        return odd_palindromes(n_digits)
    return even_palindromes(n_digits)


def even_palindromes(n_digits):
    # May contain palindromes with leading zero
    last_set = TWO_DIGIT_PALINDROMES
    n_digits -= 2
    while n_digits > 0:
        n_digits -= 2
        this_set = []
        for p in last_set:
            for d in DIGITS:
                this_set.append(d + p + d)
        last_set = this_set
    return last_set


def odd_palindromes(n_digits):
    # May contain palindromes with leading zero
    last_set = DIGITS
    n_digits -= 1
    while n_digits > 0:
        n_digits -= 2
        this_set = []
        for p in last_set:
            for d in DIGITS:
                this_set.append(d + p + d)
        last_set = this_set
    return last_set


def get_all_palindromes_below_n(n):
    sn = str(n)
    n_digits = len(sn)
    palindromes = []
    for m in range(1, n_digits+1):
        palindromes += get_palindromes_with_n_digits(m)

    # Remove elements that have a leading zero
    for p in palindromes:
        if p[0] == '0':
            palindromes.remove(p)

    palindromes = [int(p) for p in palindromes]  # convert from the string to the integer
    while True:
        p = palindromes.pop()
        if p < n:
            palindromes.append(p)
            return palindromes


def check_square_sum(n, squares_list):
    rseek = int(math.sqrt(n))-1
    lseek = rseek - 1
    window_sum = squares_list[rseek]
    while lseek >= 0:
        window_sum += squares_list[lseek]
        if window_sum == n:
            return True
        lseek -= 1
        if window_sum > n:
            rseek -= 1
            lseek = rseek - 1
            window_sum = squares_list[rseek]

    return False


def main():
    MAX_N = 10**8
    palindromes = get_all_palindromes_below_n(MAX_N)

    squares_list = []
    n = 1
    while n*n <= MAX_N:
        squares_list.append(n*n)
        n += 1

    print "There are {} palindromes and {} squares.".format(len(palindromes), len(squares_list))

    n_found = 0
    n_sum = 0
    for n in palindromes:
        if check_square_sum(n, squares_list):
            n_found += 1
            n_sum += n

    print "n_found: {} n_sum: {}".format(n_found, n_sum)


if __name__ == '__main__':
    main()


# This is not the right answer:
# There are 17937 palindromes and 9999 squares.
# n_found: 157 n_sum: 3027101256
# There are 21888 palindromes and 10000 squares.
# n_found: 172 n_sum: 3229373789

# no. palindromes < 10**8 = 19998