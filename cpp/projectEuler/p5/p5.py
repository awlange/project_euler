# First integer that is evenly divisble by all integers from 1 to 20

# Notes:
# Must be an even number b/c 2 divides, so can take stride 2
# Well, really, we can take stride of 20
# of the numbers, we really only need to test the ones that are not factoriable by lower numbers

# Factor groups (excluding 1 b/c duh):
# 20 | 2 4 5 10
# 19 |
# 18 | 2 9
# 17 |
# 16 | 2 8 4
# 15 | 3 5
# 14 | 2 7
# 13 |
# 12 | 2 3 4 6
# 11 |
#---- 10 an below are redundant with above
fax = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
#fax = [10, 9, 8, 7, 6]

def factorizable(n):
  for f in fax:
    if n % f != 0:
      return False
  return True

step = 20
n = 2520
while not factorizable(n):
  n += step
print n
