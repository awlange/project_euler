ordA = ord('A') - 1


def name_score(name):
    score = 0
    for c in name:
        score += ord(c) - ordA
    return score


def main():

    names = []
    filename = "/Users/alange/programming/projectEuler/files/names.txt"
    f = open(filename, 'r')
    for line in f:
        names = line.split(',')

    names.sort()

    total = 0
    for i in range(len(names)):
        name = names[i]
        name = name[1:len(name)-1]
        total += name_score(name) * (i+1)

    print total


if __name__ == '__main__':
    main()