# a < b < c, a + b + c = 1000, and a^2 + b^2 = c^2

# a^2 + b^2 = [1000 - (a+b)]^2
#           = 1000000 - 2000(a+b) + (a+b)^2
# 0 = 1000000 - 2000(a+b) + 2ab
# 0 = 500000 - 1000(a+b) + ab
# 500000 = 1000*(a+b) - a*b 

import math

def foo(a, b):
  return 1000*(a+b) - a*b == 500000

found = False
a = 0
while not found:
   a += 1
   for b in range(a+1, 1000-a):
       found = foo(a,b)
       if found:
           print a, b
           break

a2 = a*a
b2 = b*b
print a2, b2
c = math.sqrt(a2 + b2)
print a + b + c
print a*b*c
