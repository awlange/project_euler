# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
# product of an integer with (1,2, ... , n) where n > 1?

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
len_digits = len(digits)
len_digits_plus_one = len(digits) + 1
is_pan_range = range(1, len_digits_plus_one)
MAX_PANDIGITAL = 987654321

# 9 * 1 = 9 <-- largest first digit
# x * 2 = 87654321 <-- largest rest of digits
# So, x = 43827161 <-- largest multiplier

# Known not to be the largest: 918273645


def is_pandigital(sn):
    for d in digits:
        if d not in sn:
            return False
    return True

largest = 918273645
for i in range(9, 43827161):
    m = i
    sn = str(m)
    while len(sn) < 9:
        m += i
        sn += str(m)
    if len(sn) == 9:
        isn = int(sn)
        if isn > largest and is_pandigital(sn):
            largest = isn

print largest