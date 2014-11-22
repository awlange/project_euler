

def check(n, d):
    if n % d == 0:
        # Multiply by digit_sum until we reach/exceed n
        m = d
        while m < n:
            m *= d
        if m == n:
            return True
    return False


def main():
    seq = []
    n = 9
    d = 1
    while len(seq) < 30:
        n += 1
        if n % 10 == 0:
            d = sum([int(s) for s in str(n)])
        else:
            d += 1
        if d > 1 and check(n, d):
            print n
            seq.append(n)

    print seq


if __name__ == '__main__':
    main()