def tree_sum(data):

    sums = []
    for i in range(len(data)):
        sums.append([x for x in data[i]])

    i = len(data)
    while i > 1:
        i -= 1
        for j in range(len(data[i]) - 1):
            val = max(sums[i][j], sums[i][j+1])
            sums[i-1][j] += val

    return sums


def main():

    data = []

    # Read data from file
    path = "/Users/alange/programming/projectEuler/files/triangle.txt"
    f = open(path, 'r')
    for line in f:
        s = line.split()
        data.append([int(x) for x in s])

    sums = tree_sum(data)

    print sums[0][0]

if __name__ == '__main__':
    main()