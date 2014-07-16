# Want to do a sieve-like method

import pprint

import time
tStart = time.time()


RANGE_MAX = 101

dat = dict((i, dict((j, 1) for j in range(2, RANGE_MAX))) for i in range(2, RANGE_MAX))
#nums = dict((i, dict((j, i**j) for j in range(2, RANGE_MAX))) for i in range(2, RANGE_MAX))

# Mark off non-unique elements
for a in range(2, RANGE_MAX):
    apow = a
    for b in range(2, RANGE_MAX):
        apow *= a
        found = False
        for i in range(a+1, RANGE_MAX):
            ipow = i
            for j in range(2, RANGE_MAX):
                ipow *= i
                if ipow > apow:
                    break
                if apow == ipow:
                    dat[i][j] = 0
                    found = True
                    break
            if found:
                break


# Count unique elements
total = 0
for a in range(2, RANGE_MAX):
    for b in range(2, RANGE_MAX):
        total += dat[a][b]
print "Total unique elements: {}".format(total)

# Debugging...
# pprint.pprint(dat, indent=2, width=80)
# print ""
# pprint.pprint(nums, indent=2, width=100)

print "Run Time = " + str(time.time() - tStart)

