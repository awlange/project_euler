# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def get_digit_and_remainder(n, d):
    n *= 10
    return n / d, n % d


def divide(denom):

    remainders_seen = {}

    digits = ""

    # Start remainder at 1 b/c doing a unit division
    remainder = 1

    recurrence_done = False
    r_length = -1 # adjustment

    while not remainder == 0 and not recurrence_done:
        digit, remainder = get_digit_and_remainder(remainder, denom)
        digits += str(digit)

        # Check for recurrence
        if remainder in remainders_seen:
            remainders_seen[remainder] += 1
            r_length += 1
        else:
            remainders_seen[remainder] = 1

        # Go through recurrences twice, 1 to find, 2 to measure
        # Need to be wary of leading non-recurring digits
        if remainders_seen[remainder] == 3:
            recurrence_done = True

    # debugging
    # if recurrence_done:
    #     print "denom {} : 0.{} (recur length = {})".format(denom, digits, r_length)
    # else:
    #     print "denom {} : 0.{}".format(denom, digits)

    return r_length


def main():
    max_d = 0
    longest = 0
    for d in range(2, 1000):
        l = divide(d)
        if l > longest:
            longest = l
            max_d = d
    print max_d, longest

if __name__ == '__main__':
    main()

