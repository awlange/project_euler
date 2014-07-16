def sumArithmetic(n):
  return (n*(n + 1)) / 2

def sumSquares(n):
  return (n*(n+1)*(2*n+1))/6

n = 100
x = sumArithmetic(n)
print (x*x - sumSquares(n))
