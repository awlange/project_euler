def self_pow_10_digits(n):
    return int(trim_string_to_ten(str(pow(n, n))))


def trim_string_to_ten(s):
    if len(s) <= 10:
        return s
    else:
        return s[len(s)-10:len(s)]

total = 0
for n in range(1, 1001):
    total += self_pow_10_digits(n)
    total = int(trim_string_to_ten(str(total)))

# Pad with leading zeroes
stotal = str(total)
if len(stotal) < 10:
    while len(stotal) < 10:
        stotal = '0' + stotal

print stotal