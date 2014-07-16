def isPalindrome(n):
  s = str(n)
  i = 0;
  j = len(s) - 1

  while i <= j:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1

  return True

def getIt():
  m = 0
  i = 999
  while i >= 100:
    j = 999
    while j >= i:
      p = i * j
      if p > m:
        if isPalindrome(p):
          m = p
      j -= 1
    i -= 1
  return m

print getIt()
