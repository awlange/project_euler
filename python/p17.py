"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

ones = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]
teens = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
twenty_up = [
    '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]
hundred = 'hundred'
hundred_and = 'hundredand'
one_thousand = 'onethousand'

n = 0
for i in range(1, 1000):

    word = ''
    number = str(i)

    if i < 20:
        word = teens[i]
    elif i < 100:
        one = int(number[len(number)-1])
        ten = int(number[len(number)-2]) - 1
        word = twenty_up[ten] + ones[one]
    elif i % 100 == 0:
        hund = int(number[len(number)-3])
        word = ones[hund] + hundred
    else:
        one = int(number[len(number)-1])
        ten = int(number[len(number)-2])
        hund = int(number[len(number)-3])
        word = ones[hund] + hundred_and

        if ten*10 + one < 20:
            word += teens[ten*10 + one]
        else:
            word += twenty_up[ten-1] + ones[one]

    print i, word

    n += len(word)

n += len(one_thousand)

print n