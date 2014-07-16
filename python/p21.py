RANGE_MAX = 10000


def get_proper_divisor_sum(n):
    # Sqrt limit trick helps a lot
    divisor_sum = 1
    m = 2
    while m*m <= n:
        if n % m == 0:
            divisor_sum += m + n/m
        m += 1
    return divisor_sum


def main():

    numbers = [True for _ in range(0, RANGE_MAX+1)]

    amicable_number_sum = 0

    for a in range(1, RANGE_MAX):
        if numbers[a]:
            b = get_proper_divisor_sum(a)
            if b > a and get_proper_divisor_sum(b) == a:
                # Amicable number
                amicable_number_sum += a + b

                # Mark off to avoid recomputing
                numbers[b] = False

    print amicable_number_sum


if __name__ == '__main__':
    main()


# Noteworthy solution found on Project Euler by another:

# NUM = 10
# v=[0]*NUM
# sum = 0
#
# This generates the sum of proper divisor sums up to NUM
# Similar to sieve for primes, it adds each number into the elements into
# which it divides up to NUM.
# for value in range(1,NUM):
#    i = 2*value
#    while i < NUM:
#       v[i] += value
#       i += value
# The rest is just checking for amicable pairs
#for i in range(1,NUM):
#   if v[i] < NUM + 1:
#      if i == v[v[i]] and i != v[i]:
#         sum += i
#
#print(sum)