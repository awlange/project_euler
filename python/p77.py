"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

We'll be needing some theory for this one on partitions.

So, just realized this is a variation on the change making problem, where we have
a set of coins adding up to a total. Just here, our coins are primes numbers.
This is like p31, so will reuse code

Computed answer: 71
I'm surprised the result is such a small number!
"""

import time
from p27 import get_primes_up_to


def get_coins(diff, max_coin, coins):
    if diff == 0:
        return 1
    if diff < 0:
        return 0
    result = 0
    for coin in coins:
        if coin <= max_coin and coin <= diff:
            result += get_coins(diff - coin, coin, coins)
    return result


def main():
    start = time.time()

    n = 10
    primes = get_primes_up_to(n)
    partitions = get_coins(n, primes[-1], primes)
    while partitions < 5000:
        n += 1
        if n > primes[-1]:
            primes = get_primes_up_to(2*n)
        partitions = get_coins(n, primes[-1], primes)

    print n

    print "Time: {}".format(time.time() - start)

if __name__ == '__main__':
    main()