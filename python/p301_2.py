M = 31

# Tree traversal, pre-order
def traverse(num):
  if len(num) == M:
    #print '0' + num
    return 1
  elif len(num) > M:
    return 0
  else:  
    return traverse(num + '0') + traverse(num + '11')

# Note: all zeroes one will account for the max value
print traverse('')
