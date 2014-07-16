"""
The palindromic number 595 is interesting because it can be written as the sum of consecutive
squares: 6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums,
and the sum of these palindromes is 4164. Note that 1 = 0**2 + 1**2 has not been included as this problem
is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10**8 that are both palindromic and can be written as the sum of
consecutive squares.
"""

from p55 import is_palindrome


def check_square_sum(n, squares_list, square_roll_sum):
    s = len(squares_list) - 1
    while s >= 0 and square_roll_sum[s] >= n:
        total = 0
        tot_list = []
        t = s
        while total < n:
            total += squares_list[t]
            tot_list.append(squares_list[t])
            if total == n and t != s:  # must be more than one consecutive squares, (ex. ignore 121 = 11**2)
                print n, tot_list
                return True
            t -= 1
        s -= 1

    return False


def main():
    squares_list = [1]
    square_roll_sum = []
    roll_sum = 0
    for square in squares_list:
        roll_sum += square
        square_roll_sum.append(roll_sum)

    n_found = 0
    n_sum = 0
    for n in range(1, 10**3):
        if n % 10**6 == 0:
            print "{}...".format(n)

        n2 = n*n
        if n*n > squares_list[-1]:
            squares_list.append(n2)
            square_roll_sum.append(square_roll_sum[-1] + n2)

        if is_palindrome(n) and check_square_sum(n, squares_list, square_roll_sum):
                n_found += 1
                n_sum += n

    print "n_found: {} n_sum: {}".format(n_found, n_sum)


if __name__ == "__main__":
    main()