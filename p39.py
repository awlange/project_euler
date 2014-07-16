# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

# a^2 + b^2 = c^2
# a + b + c = p
# c = p - (a + b)
# c^2 = [p - (a + b)]^2

# a < c
# b < c
# c < p

import time


def main():
    t_start = time.time()

    max_p = 0
    max_solutions = 0

    for p in range(120, 1001):
        n_solutions = 0
        for a in range(1, p):
            a2 = a*a
            for b in range(a, p):
                c = p - (a + b)
                c2 = c*c
                b2 = b*b
                a2_plus_b2 = a2 + b2
                if a2_plus_b2 > c2:
                    break
                elif a2_plus_b2 == c2:
                    n_solutions += 1

        if n_solutions > max_solutions:
            max_solutions = n_solutions
            max_p = p

    print max_p


    print "Run time: {}".format(time.time() - t_start)

if __name__ == '__main__':
    main()