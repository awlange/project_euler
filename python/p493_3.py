"""
70 balls, 7 colors, 10 balls/color, 20 picks. Expected number of distinct colors?

E = sum_{d=1}^{N_{colors}} P(d) * d

where d is number of distinct colors, P(d) is prob of d


notes:
denominator is: 70 * 69 * 68 ... 51

"""

from scipy import special

# compute denominator
d = 70
f = 1.0
for i in range(20):
    f *= 1.0 / d
    d -= 1

print(special.binom(70 + 20 - 1, 20))
print(special.binom(70, 20))

