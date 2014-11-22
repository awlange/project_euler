import math

from p45 import is_perfect_square

# (1, 1, 2, 1, 1, 2)

def minimize_sequence(seq):
    if len(seq) < 2:
        return seq


    n = 0
    while n < len(seq) - 1:
        n += 1
        if len(seq) % n == 0:
            min_seq = seq[:n]
            ndiv = len(seq) / n

            n_good = True
            for d in range(ndiv):
                for i in range(n):
                    if min_seq[i] != seq[d*n + i]:
                        n_good = False
                        break
                if not n_good:
                    break
            if n_good:
                # Found a minimum!
                print "Minimized from {} to {}".format(len(seq), len(min_seq))
                print seq, min_seq
                return min_seq

    return seq



def compute_period(n):
    a0 = int(math.sqrt(n))

    aseq = []  # a_i sequence
    abd_keep = (1, 1, 1)
    b = a0
    d = 1
    i = -1
    while 1:
        i += 1
        a = a0 if i == 0 else aseq[i-1]
        d = (n - b * b) / d
        abd = (a, b , d)
        # print "adb:", a, b, d

        # Check if we are repeating
        if i == 1:
            abd_keep = abd
        elif i > 1 and abd_keep == abd:
            break

        # Determine b, which is <= a0
        c = a0
        while 1:
            x = b + c
            if x % d == 0:
                aseq.append(x / d)
                b = c
                break
            c -= 1

    # Check if we can minimize this sequence any more
    fin = minimize_sequence(aseq[:-1])
    # fin = aseq[:-1]
    print n, a0, fin, len(fin)
    return len(fin)


def main():

    # print minimize_sequence([1, 1, 2, 1, 1, 2, 1, 1, 2])
    #print minimize_sequence([1, 1, 1, 1, 1, 1])
    n_odds = 0
    for n in range(1, 10000 + 1):
        if not is_perfect_square(n):
            if compute_period(n) % 2 == 1:
                n_odds += 1

    print n_odds

if __name__ == '__main__':
    main()