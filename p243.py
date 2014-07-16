import time

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def get_divisors(n):
    # Ignoring 1 and n divisors
    # Sqrt limit trick helps a lot
    divisors = []
    m = 2
    while m*m <= n:
        if n % m == 0:
            divisors.append(m)
            divisors.append(n/m)
        m += 1
    return divisors


def compute_resilience2(d):
    # This one is a little faster
    tot = 1
    n = 2
    divisors = get_divisors(d)

    while n < d:
        keep = True
        for divisor in divisors:
            if n % divisor == 0:
                keep = False
                break
        if keep:
            tot += 1
        n += 1
    return float(tot) / float(d-1)


def compute_resilience(d):
    tot = 0
    n = 1
    while n < d:
        if gcd(n, d) == 1:
            tot += 1
        n += 1
    return float(tot) / float(d-1)


def main():
    ts = time.time()

    # ratio = float(15499) / float(94744)
    ratio = 0.22

    d = 2
    while compute_resilience2(d) > ratio:
        d += 1

    print "Final d: {}".format(d)

    print "Time: {}".format(time.time() - ts)

if __name__ == '__main__':
    main()
