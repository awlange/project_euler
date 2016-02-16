"""
square free

Borrowing some code from stack overflow b/c im lazy. It's what I had in mind anyways.
"""

from math import factorial as fac


def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom


# Print Pascal's triangle to test binomial()
def pascal(m):
    for x in range(m):
        row = [binomial(x, y) for y in range(x + 1)]
        print(row)

def pascal2(m):
    """
    Only go up to half, since its symmetric
    """

    all_rows = []

    for x in range(m):
        row = []
        prev_b = 0
        for y in xrange(x + 1):
            b = binomial(x, y)
            if prev_b >= b:
                break
            else:
                prev_b = b
                row.append(b)

        all_rows.append(row)
    return all_rows


def main():
    rows = pascal(20)




if __name__ == '__main__':
    #pascal(8)
    main()
