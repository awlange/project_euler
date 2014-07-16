MAX_N = 10**8
# sqrt of MAX_N = 10**4


def is_palindrome(n):
    return str(n) == str(n)[::-1]


palindromes = set()

squares = [x**2 for x in range(1, 10**4 + 1)]
for i in range(len(squares)):
    sum_of_squares = 0
    for j in range(i, len(squares)):
        if sum_of_squares > MAX_N:
            break
        sum_of_squares += squares[j]
        if is_palindrome(sum_of_squares) and sum_of_squares != squares[j]:
            palindromes.add(sum_of_squares)

print sum(palindromes)