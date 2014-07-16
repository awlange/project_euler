"""
Find the number of characters saved by writing each of these in their minimal form.
"""

import time


def num_chars(numerals):
    total = 0
    for num in numerals:
        total += len(num)
    return total


def get_numerals():
    numerals = []
    with open("/Users/alange/programming/projectEuler/files/roman.txt") as f:
        for line in f:
            numerals.append(line.strip('\n'))
    return numerals

num_map = {'I': 1,
           'IV': 4,
           'V': 5,
           'IX': 9,
           'X': 10,
           'XL': 40,
           'L': 50,
           'XC': 90,
           'C': 100,
           'CD': 400,
           'D': 500,
           'CM': 900,
           'M': 1000}

inv_num_list = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]

"""
i.	 Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
ii.	 I can only be placed before V and X.
iii. X can only be placed before L and C.
iv.	 C can only be placed before D and M.
"""
def roman_to_arabic(r):
    val = 0
    tmp = len(r) - 1
    i = 0
    while i < len(r):
        d = r[i]
        if i < tmp:
            if d + r[i+1] in num_map:
                val += num_map[d + r[i+1]]
                i += 2
            else:
                val += num_map[d]
                i += 1
        else:
            val += num_map[d]
            i += 1

    return val


def arabic_to_min_roman(a):
    aa = a
    rr = ''
    for inv_num in inv_num_list:
        n = inv_num[0]
        r = inv_num[1]
        while aa >= n:
            aa -= n
            rr += r
    return rr


def main():
    t_start = time.time()

    original_numerals = get_numerals()
    original_chars = num_chars(original_numerals)
    arabic_numerals = [roman_to_arabic(r) for r in original_numerals]
    min_roman_numerals = [arabic_to_min_roman(a) for a in arabic_numerals]
    min_chars = num_chars(min_roman_numerals)

    print original_chars, min_chars, original_chars - min_chars

    print "Run time: {}".format(time.time() - t_start)


if __name__ == '__main__':
    main()