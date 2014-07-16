digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def is_pandigital(sn):
    for d in digits:
        if d not in sn:
            return False
    return True


def advance_Fibonacci(n, F_n, F_n_1, F_n_2, target_n):
    while True:
        F_n = F_n_1 + F_n_2
        if n == target_n:
            break

        F_n_2 = F_n_1
        F_n_1 = F_n
        n += 1

    return n, F_n, F_n_1, F_n_2


n = 3
sF_n_2 = '1'
sF_n_1 = '1'

last_n = 3
F_n_2 = 1
F_n_1 = 1
F_n = 2

times_found = 0
while True:
    # Only keep the last 9 digits, makes things much faster
    sF_n = str(int(sF_n_1) + int(sF_n_2))[-9:]

    if is_pandigital(sF_n):
        print "Found: {}".format(n)
        # times_found += 1
        # if times_found > 2:
        #     break

        last_n, F_n, F_n_1, F_n_2 = advance_Fibonacci(last_n, F_n, F_n_1, F_n_2, n)
        if is_pandigital(str(F_n)[:9]):
            print "Holy shit! {}".format(n)
            break

    # Update for next iteration
    n += 1
    sF_n_2 = sF_n_1
    sF_n_1 = sF_n