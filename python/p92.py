"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 - 32 - 13 - 10 - 1 - 1
85 - 89 - 145 - 42 - 20 - 4 - 16 - 37 - 58 - 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

CACHE_LIMIT = 1000000
cache = {}


number_of_89s = 0
cache_hits = 0

for n in range(1, 10**7):

    m = n
    while not (m == 1 or m == 89):

        if m in cache:
            cache_hits += 1
            m = cache[m]
        else:
            m_orig = m
            m = 0
            for i in str(m_orig):
                m += int(i) * int(i)

    if n < CACHE_LIMIT and n not in cache:
        cache[n] = m

    #print n, m
    if n % 100000 == 0:
        print n

    if m == 89:
        number_of_89s += 1

print "\n89s found: {}".format(number_of_89s)
print cache_hits