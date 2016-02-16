M = 11

"""
X(n, 2n, 3n) = 0 for n<=2^30

X is the nim-sum, computed by XOR of all heaps:

n ^ 2n ^ 3n

ex.
n  : 0001
2n : 0010
3n : 0011
r  : 0000

n ^ 2n = 0011
(n ^ 2n) ^ 3n = r = 0000

2n = n << 1

z = n ^ 2n

n  : 0010
2n : 0100
z  : 0110
3n : 0110
r  : 0000

n  : 0011
2n : 0110
z  : 0101
3n : 1001
r  : 1101

n  : 0001 0000
2n : 0010 0000
z  : 0011 0000
3n : 0011 0000
r  : 0000 0000

"""


def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(M+1)[::-1])

# a = n
# b = 2n
# c = 3n

nways = 0
a = 1
b = a << 1
c = a * 3
while a <= 2**(M-1): 
  if a ^ b ^ c == 0:
    nways += 1
    print a, b, c
    print toBinary(a)
    print toBinary(b)
    print toBinary(c)

  a += 1
  b = a << 1
  c = a * 3


print 'nways: {}'.format(nways)


