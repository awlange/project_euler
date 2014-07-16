def read_matrix(filename):
    matrix = []
    with open(filename) as f:
        for line in f:
            matrix.append([int(x) for x in line.split()])
    return matrix


def main():
    matrix = read_matrix('/Users/alange/programming/projectEuler/files/p345_example.txt')

    sorted_rows = {}
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append((matrix[i][j], j))
        row.sort(reverse=True)
        sorted_rows[i] = row

    for r in sorted_rows:
        print r, sorted_rows[r]

    # Initial guess is max element for each row
    # max_elements


if __name__ == '__main__':
    main()