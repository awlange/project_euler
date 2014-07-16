def factorial(n):
    # dumb factorial
    if n <= 1:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

# Factorial values:
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880

# digits: 0 min --> 1 = 0123456789
#       : 0 max --> 362880 = 0987654321
#       : 1 min --> 362881 = 1023456789
#       : 1 max --> 725760 = 1987654320
#       : 2 min --> 725761 = 2013456789
#       : 2 max --> 1088640 = 2987654310
# Thus, leading digit is 2
# 2nd digit:
# 20 min --> 725761 = 2013456789
# 20 max --> 766080 = 2098765431
# 21 max --> 806400 = 2198765430
# 23 max --> 846720 = 2398765410
# 24 max --> 887040 = 2498765310
# 25 max --> 927360 = 2598764310
# 26 max --> 967680 = 2698754310
# 27 max --> 1008000 = 2798654310
# Thus, 2nd digit is 7
# 3rd digit: (1000000 -
# 270 min --> 967681 = 2701345689

million = 1000000
# million = 362880
fac = [factorial(x) for x in range(0, 10)]

x = [0] * 10
n = 0
for i in range(9, 0, -1):
    fi = fac[i]
    while n + fi < million:
        n += fi
        x[i] += 1

print n
print x

# Start with lowest digit available of set
# Number of permutations till we move on to the next digit
# x = [0, 0, 2, 2, 1, 5, 2, 6, 6, 2]

digits = [a for a in range(0, 10)]

num = ""

for i in range(9, -1, -1):
    print x[i], digits
    num += str(digits.pop(x[i]))
    #print num

print num



