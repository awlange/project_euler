"""
Find the least value of n for which p(n) is divisible by one million.
"""

import time
from p76 import partition


def main():
    start = time.time()
    n = 1
    MILLION = 10**6
    while True:
        n += 1
        pn = partition(n)
        if pn >= MILLION and partition(n) % MILLION == 0:
            print "Found: ", n
            break

    print "Time: ", time.time() - start

if __name__ == '__main__':
    main()