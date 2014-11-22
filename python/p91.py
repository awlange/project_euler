
# a = dist(1, 0)
# b = dist(2, 0)
# c = dist(1, 2)
# a**2 + b**2 = c**2
# a**2 + b**2 + c**2 = 2*c**2



MAX = 51
count = 0

for x1 in range(0, MAX):
    x1_2 = x1*x1
    for y1 in range(0, MAX):
        da2 = float(x1_2 + y1*y1)
        if da2 > 0:
            for x2 in range(0, MAX):
                x2_2 = x2*x2
                x2_min_x1_2 = (x2 - x1)**2
                for y2 in range(0, MAX):
                    db2 = x2_2 + y2*y2
                    dc2 = x2_min_x1_2 + (y2 - y1)**2
                    if db2 > 0 and dc2 > 0:

                        # get the max of the three distances, which is the true c**2
                        c2 = max(da2, db2, dc2)
                        if da2 + db2 + dc2 == 2*c2:
                            count += 1

print count / 2