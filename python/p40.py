target_digit = 1
product = 1
digits = 0
for n in range(1, 1000000 + 1):
    sn = str(n)
    len_sn = len(sn)

    if digits + len_sn >= target_digit:
        while len_sn >= 0:
            if digits + len_sn == target_digit:
                d = int(sn[len_sn-1])
                product *= d
                print 'd{}: {}'.format(target_digit, d)
                target_digit *= 10
                break
            len_sn -= 1

    digits += len(str(n))

print 'Product: {}'.format(product)
