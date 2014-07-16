import math

from p27 import get_primes_up_to

MAX_N = 50 * 10**6
primes = get_primes_up_to(10**5)
square_primes = [p**2 for p in get_primes_up_to(int(math.sqrt(MAX_N)))]
cube_primes = [p**3 for p in get_primes_up_to(int(math.pow(MAX_N, 1.0/3.0)))]
fourth_primes = [p**4 for p in get_primes_up_to(int(math.pow(MAX_N, 1.0/4.0)))]
#print len(square_primes), len(cube_primes), len(fourth_primes)
# print square_primes
# print cube_primes
# print fourth_primes

# Need to account for double counting!!!
seen = set()

for p4 in fourth_primes:
    for p3 in cube_primes:
        p4p3 = p4 + p3
        if p4p3 < MAX_N:
            for p2 in square_primes:
                tot = p4p3 + p2
                if tot < MAX_N:
                    seen.add(tot)


print len(seen)