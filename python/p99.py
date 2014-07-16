import math


max_x = 0.0
max_n = -1
with open("/Users/alange/programming/projectEuler/files/base_exp.txt") as f:
    n = 0
    for line in f:
        n += 1
        base, _, exponent = line.partition(',')
        x = float(exponent) * math.log(float(base))
        if x > max_x:
            max_x = x
            max_n = n

print max_n