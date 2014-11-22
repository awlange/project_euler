import math


def Tn(n):
    return (n*(n+1)) / 2


def Pn(n):
    return (n*(3*n-1)) / 2


def Hn(n):
    return n*(2*n-1)


def is_perfect_square(x):
    """
    Rule: Perfect squares can only end in 0, 1, 4, or 9 in base 16
    Helps to avoid the sqrt call 75% of the time!
    """
    d = int(x & 0xF)
    if d > 9:
        return False
    if d != 2 and d != 3 and d != 5 and d != 6 and d != 7 and d != 8:
        t = int(math.sqrt(x))
        return t*t == x
    return False


def main():
    t = 286
    p = 165
    h = 143
    done = False
    while not done:
        T = Tn(t)
        P = Pn(p)
        while P <= T:
            if P == T:
                H = Hn(h)
                while H <= T:
                    if H == T:
                        print T, t, p, h
                        done = True
                        break
                    h += 1
                    H = Hn(h)
                if H > T:
                    h -= 1
            p += 1
            P = Pn(p)
        if P > T:
            p -= 1
        t += 1




if __name__ == '__main__':
    main()