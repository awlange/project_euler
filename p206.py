"""
Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
"""

import math
# Largest: 1929394959697989990
print math.sqrt(1929394959697989990.0)
N_MAX = 1389026624
# Smallest: 1020304050607080900
print math.sqrt(1020304050607080900.0)
N_MIN = 1010101010
#print N_MAX - N_MIN


def test(n):
    sn = str(n)
    if sn[0] == '1' and sn[2] == '2':
        if sn[4] == '3' and sn[6] == '4':
            if sn[8] == '5' and sn[10] == '6':
                if sn[12] == '7' and sn[14] == '8':
                    if sn[16] == '9' and sn[18] == '0':
                        return True
    return False

# even number, so must be even*even=even, means can take stride 2
# but since last is 0, can take stride 10
n = N_MIN
while not test(n*n):
    # if n % 10**6 == 0:
    #     print n
    n += 10

print n