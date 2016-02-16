"""
Let f(N) be the number of points with integer coordinates that are on a circle passing through
(0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?


Square enclosed by circle, centered at (N/2, N/2).
r^2 = (N/2)^2 + (N/2)^2 = N^2 / 2
r = N / sqrt(2)

shifting center to origin, conditions are that circle passes through M = N/2
(-M, -M), (M, -M), (-M, M), and (M, M)

number of points will be divisible by 4 since circle, 1 for each quadrant by symmetry
so, let's just work in quadrant I with center at origin, such that we have circle passing through (M, M)

"""


def main():
    pass


if __name__ == "__main__":
    main()
