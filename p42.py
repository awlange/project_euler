ordA = ord('A') - 1


def name_score(name):
    score = 0
    for c in name:
        score += ord(c) - ordA
    return score


def main():

    names = []
    filename = "/Users/alange/programming/projectEuler/files/words.txt"
    f = open(filename, 'r')
    for line in f:
        names = line.split(',')

    # Compute all name scores
    scores = []
    max_score = 0
    for name in names:
        score = name_score(name)
        max_score = max(max_score, score)
        scores.append(score)

    # Generate triangle numbers until above max score
    triangle_numbers = []
    t = 0
    n = 1
    while t < max_score:
        t = (n * (n+1)) / 2
        triangle_numbers.append(t)
        n += 1

    # Find out how many scores are in the triangle number list
    n_triangle_words = 0
    for score in scores:
        if score in triangle_numbers:
            n_triangle_words += 1

    print "Number of triangle words: ", n_triangle_words


if __name__ == '__main__':
    main()