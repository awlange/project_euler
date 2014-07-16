import math

# simple prime checker
def isPrime(n):
  # Base for loop
  if (n < 3):
    return True
  # Quick even check to let loop have stride of 2
  if (n % 2 == 0):
    return False
  # Factorization bound
  sqrtn = int(math.sqrt(n))
  # Skip all even numbers b/c those are obviously not prime
  for i in range(3, sqrtn+1, 2):
    if (n % i == 0):
      return False
  return True

# simple prime factorizer
def getPrimeFactors(n):
  primes = []
  for i in range(2, n+1):
    if not n % i and isPrime(i):
      primes.append(i)
  return primes

# simple factorizer, exclude n 
def getFactors(n):
  factors = []
  for i in range(1, n):
    if not n % i:
      factors.append(i)
  return factors

def isPerfectSquare(x):
  t = (int)(math.sqrt(x))
  return t*t == x

def isTriangleNumber(x):
  return isPerfectSquare(8*x + 1)

def computeTriangleN(x):
  return (math.sqrt(8*x + 1) - 1) / 2

def power(x, n):
  if n <= 0:
    return 1
  m = x
  for i in range(1,n):
    m *= x
  return m

# -------------------------------------------
def main():

  triangle_nums = []

  primes = [2, 3, 5, 7, 9]

  for n in range(501,600):
    factors = getFactors(n)
    if len(factors) > 0:
      print n, primes, factors

      exponents = [0 for _ in primes]

      level = 0
      fax = [[] for _ in primes]
      for f in factors:
        fax[level].append(f-1)

      while len(fax[0]) != 0:
        if len(fax[level]) == 0:
          level -= 1
          continue

        #print "  ---  ", level, exponents, fax
        exponents[level] = fax[level].pop()

        # update for next iteration
        if level+1 < len(primes):
          level += 1
          for f in factors:
            fax[level].append(f-1)

        # visit node
        exp_prod = 1
        for i in range(len(primes)):
          exp_prod *= exponents[i] + 1
        if exp_prod == n:
          # Valid exponent combo
          prod = 1
          for i in range(len(primes)):
            prod *= power(primes[i], exponents[i])
          #print "exp_prod = ", exp_prod, " prod = ", prod
          if isTriangleNumber(prod):
            t = computeTriangleN(prod)
            print "Triangle number: ", t, " from exponents: ", exponents
            triangle_nums.append(computeTriangleN(prod))

  print "TRIANGLE NUMBERS FOUND:"
  print triangle_nums

if __name__ == '__main__':
  main()
