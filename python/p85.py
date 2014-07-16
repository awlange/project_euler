"""
No. rectangles on x by y grid = [x(x+1)/2] * [y(y+1)/2]
Triangle numbers multiplied
"""

import time


def triangle(x):
    return (x**2 + x)/2

start = time.time()

MAXIMUM = 2 * 10**6
closest = (MAXIMUM, 1, 1, 1)

x = 1
tri_x = 1
while tri_x < MAXIMUM:
    x += 1
    tri_x = triangle(x)

    y = 1
    n_rex = tri_x
    while n_rex < MAXIMUM:
        y += 1
        tri_y = triangle(y)
        n_rex = tri_x * tri_y

        diff = abs(MAXIMUM - n_rex)
        if diff < closest[0]:
            closest = (diff, x, y, x*y)

print closest
print "Time: ", time.time() - start