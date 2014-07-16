# Seed number under 1 million with the longest Collatz sequence
# n even -> n/2
# n odd _ 3*n + 1

# Use >> to divide by 2
# Can probably memoize some of the first so many numbers

#LIMIT = 1000000
LIMIT = 5

storage = {}

def getNext(n):
  if n % 2 == 0:
    return n >> 1
  return 3*n + 1

def getCollatz(n):
  # Check storage
  if n < 10000 and n in storage:
    return storage[n]

  n_orig = n
  length = 0
  while n != 1:
    n = getNext(n)
    length += 1

  # Store lengths with n_orig under 10000
  if n_orig < 10000:
    storage[n_orig].put(length)

  return length

def main():
  longest = 0
  getCollatz(13)
  for n in range(1,LIMIT):
    longest = max(longest, getCollatz(n))
  print "Longest found: ", longest
  print storage

if __name__ == '__main__':
  main()
