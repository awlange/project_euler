# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
len_digits = len(digits)
MAX_PANDIGITAL = 987654321

product_cache = []

# Found on the interwebs
def all_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_permutations(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def is_pandigital(sn):
    # Note: sn is a list of integers
    for i in range(1, len(sn)+1):
        if not i in sn:
            return False
    return True

# digits = ['3', '9', '1', '8', '6', '7', '2', '5', '4']

def main():
    for perm in all_permutations(digits):
        # i is where the * operator goes
        for i in range(1, len(digits)):
            multiplicand = int(''.join(perm[0:i]))
            # j is where the = operator goes
            for j in range(i+1, len_digits):
                # Quick check to avoid impossible products, short circuit the loop
                if j-1 > len_digits - j:
                    break
                multiplier = int(''.join(perm[i:j]))
                product = int(''.join(perm[j:len_digits]))
                if multiplicand * multiplier == product:
                    if product not in product_cache:
                        product_cache.append(product)


    print sum(product_cache)

if __name__ == '__main__':
    main()