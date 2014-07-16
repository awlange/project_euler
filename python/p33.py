import time

# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.

def main():
    t_start = time.time()

    fractions = []

    for n in range(11, 100):
        sn = str(n)
        for d in range(n+1, 100):
            sd = str(d)

            # Check for possible digit cancellation, ignore zero though
            cancel_digit = -1
            for digit_sd in sd:
                if digit_sd in sn:
                    cancel_digit = int(digit_sd)
                    break

            if cancel_digit > 0:
                # Attempt cancellation
                real_fraction = float(n) / float(d)

                cancelled_num = int(sn[0])
                if cancelled_num == cancel_digit:
                    cancelled_num = int(sn[1])

                cancelled_den = int(sd[0])
                if cancelled_den == cancel_digit:
                    cancelled_den = int(sd[1])

                if int(cancelled_den) == 0:
                    continue

                if float(cancelled_num) / float(cancelled_den) == real_fraction:
                    #print "[{}/{}]".format(sn, sd),
                    #print cancel_digit,
                    #print "[{}/{}]".format(cancelled_num, cancelled_den), real_fraction

                    fractions.append((cancelled_num, cancelled_den))

    print fractions

    # Compute product of fractions
    numerator = 1
    denominator = 1
    for fraction in fractions:
        numerator *= fraction[0]
        denominator *= fraction[1]

    print numerator, denominator, denominator / numerator

    print "Run Time = {} seconds".format(time.time() - t_start)


if __name__ == '__main__':
    main()