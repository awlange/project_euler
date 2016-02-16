"""
70 balls, 10 colors, 20 picks. Expected number of distinct colors?

E = sum_{d=1}^{N_{colors}} P(d) * d

where d is number of distinct colors, P(d) is prob of d
"""

import time

nballs = 70
ncolors = 7
nc = nballs / ncolors
npicks = 2


# each element is the count of how many leaf nodes end with that many distinct colors
result_count = [0 for _ in range(ncolors+1)]


def pick(pick_level, balls, distinct):
    while 1:
        if pick_level >= npicks:
            nd = sum(distinct)
            result_count[nd] += 1
            #return

    # pick a color
    for color, n_balls_left in enumerate(balls):
        if n_balls_left > 0:
            new_balls = [b for b in balls]
            balls[color] -= 1
            new_distinct = [d for d in distinct]
            dbefore = distinct[color]
            distinct[color] |= 1
            pick(pick_level+1, new_balls, new_distinct)


def main():
    time_start = time.time()

    balls = [nc for _ in range(ncolors)]
    distinct = [0 for _ in range(ncolors)]

    pick(0, balls, distinct)

    print(result_count)

    expected = 0.0
    for n, x in enumerate(result_count):
        expected += float(x) * float(n)
    expected /= float(sum(result_count))
    print("%.12f" % expected)

    print("time: {}".format(time.time() - time_start))

if __name__ == '__main__':
  main()
