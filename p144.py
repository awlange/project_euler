import math
import time


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(gamma, a):
    return gamma*a[0], gamma*a[1]


def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]


def length(a):
    return math.sqrt(a[0]*a[0] + a[1]*a[1])


def normalize(a):
    l = length(a)
    return a[0] / l, a[1] / l


def slope(a):
    return -4.0 * a[0] / a[1]


def angle(norm_a, point):
    m = normalize((1.0, slope(point)))
    # Rotate slope vector to become outward facing normal
    if point[1] < 0.0:
        m = rotate(m, -math.pi * 0.5)
    else:
        m = rotate(m, math.pi * 0.5)
    return math.acos(dot(norm_a, m))


def rotate(a, t):
    # Counter-clockwise rotation
    return math.cos(t)*a[0] - math.sin(t)*a[1], math.sin(t)*a[0] + math.cos(t)*a[1]


def compute_gamma(point, normal):
    a = 4.0 * normal[0]**2 + normal[1]**2
    b = 8.0 * point[0] * normal[0] + 2.0 * point[1] * normal[1]
    c = 4.0 * point[0]**2 + point[1]**2 - 100.0
    gamma = (-b + math.sqrt(b**2 - 4.0*a*c)) / (2.0 * a)
    return gamma


def ellipse(a):
    return 4.0*a[0]**2 + a[1]**2


def main():
    start = time.time()

    # Initialize
    a1 = (0.0, 10.1)
    a2 = (1.4, -9.6)

    n_hits = 1
    while True:
        # Compute
        a = sub(a2, a1)
        an = normalize(a)
        theta = angle(an, a2)
        # print "theta:", theta, theta*180.0/math.pi
        # Flip and rotate by 2 theta
        bn = rotate(an, math.pi + 2.0*theta)
        b1 = a2
        gamma = compute_gamma(b1, bn)
        # print "gamma:", gamma, scale(gamma, bn)
        b2 = add(b1, scale(gamma, bn))
        # print "b:", b1, b2, bn, ellipse(b2)

        # Check
        if -0.01 <= b2[0] <= 0.01 and b2[1] > 9.0:
            print b2
            break

        # Next iteration
        a2 = b2
        a1 = b1
        n_hits += 1


    print "Number of hits: {}".format(n_hits)
    print "Time: {}".format(time.time() - start)


if __name__ == '__main__':
    main()