"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""


def is_bouncy(n):
    sn = str(n)

    is_increasing = True
    is_decreasing = True

    last_digit = sn[0]
    i = 1
    while i < len(sn) and (is_increasing or is_decreasing):
        digit = sn[i]
        if digit < last_digit:
            is_increasing = False
        if digit > last_digit:
            is_decreasing = False
        last_digit = digit
        i += 1

    return not (is_increasing or is_decreasing)


n_bouncy = 0
m = 1
ratio = 0.0
while ratio != 0.99:
    if is_bouncy(m):
        n_bouncy += 1
    ratio = float(n_bouncy) / float(m)
    m += 1

print n_bouncy, m-1, ratio



