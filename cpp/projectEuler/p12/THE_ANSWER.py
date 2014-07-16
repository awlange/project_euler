TARGET = 501

def numFactors(n):
  if n == 1:
    return 1

  count = 0;
  i = 2
  while i*i <= n:
    if n % i == 0:
      count += 1 + (i * i != n)
    i += 1

  # Add 1 and n
  return count + 2

def main():

  n = 1
  left = 1
  n_factors_left = 1
  while 1:
    right = n+1
    if right % 2 == 0:
      right /= 2
    n_factors_right = numFactors(right)

    if n_factors_left * n_factors_right >= TARGET:
      print "Found: n = ", n
      print "Factors: ", n_factors_left * n_factors_right
      print "Triangle number is: ", left*right
      break

    left = right
    n_factors_left = n_factors_right
    n += 1


if __name__ == '__main__':
  main()
