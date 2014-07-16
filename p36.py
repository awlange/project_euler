def is_palindrome(s):
    if not isinstance(s, basestring):
        s = str(s)
    result = True
    i = 0
    j = len(s)-1
    while i < j and result:
        if s[i] != s[j]:
            result = False
        i += 1
        j -= 1
    return result


def base10_to_base2(n):
    # Returns string in binary
    m = n
    d = 2
    n_base2 = ''
    while m > 0:
        n_base2 = str(m % d) + n_base2
        m /= 2
    return n_base2


def main():
    palindrome_sum = 0
    for n in range(0, 1000000):
        if is_palindrome(n) and is_palindrome(base10_to_base2(n)):
            palindrome_sum += n

    print "Palindrome sum: {}".format(palindrome_sum)


if __name__ == '__main__':
    main()