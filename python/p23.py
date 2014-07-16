MAXIMUM = 28123 + 1
#MAXIMUM = 30 + 1


def get_proper_divisor_sum_list(maximum):
    # maximum non-inclusive
    v = [0]*maximum
    for n in range(1, maximum):
        i = 2*n
        while i < maximum:
            v[i] += n
            i += n
    return v


def get_abundant_number_list(maximum):
    # maximum non-inclusive
    divsum = get_proper_divisor_sum_list(maximum)
    a = []
    for i in range(1, maximum):
        if divsum[i] > i:
            a.append(i)
    return a


def main():
    abundant_numbers = get_abundant_number_list(MAXIMUM)

    #print abundant_numbers

    is_i_abundant_pair = [False for _ in range(MAXIMUM)]

    for i in range(len(abundant_numbers)):
        ai = abundant_numbers[i]
        for j in range(i, len(abundant_numbers)):
            aj = abundant_numbers[j]
            pair = ai + aj
            if pair >= MAXIMUM:
                break
            else:
                is_i_abundant_pair[pair] = True

    total = 0
    for i in range(len(is_i_abundant_pair)):
        #print i, is_i_abundant_pair[i]
        if not is_i_abundant_pair[i]:
            total += i

    print total

if __name__ == '__main__':
    main()