"""
n the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
"""


def get_matrix_from_file(filename):
    matrix = []
    with open(filename) as f:
        for line in f:
            line = line.split(',')
            row = []
            for element in line:
                row.append(int(element))
            matrix.append(row)
    return matrix


def compute_sub_matrix_min(matrix, N, i, j, potential_matrix):
    right_limit = j == N-1
    down_limit = i == N-1
    if right_limit and down_limit:
        return matrix[i][j]
    if right_limit:
        return matrix[i][j] + potential_matrix[i+1][j]
    if down_limit:
        return matrix[i][j] + potential_matrix[i][j+1]

    # Otherwise, choose the minimum from the right or down
    return matrix[i][j] + min(potential_matrix[i+1][j], potential_matrix[i][j+1])


def main():
    path = '/Users/alange/programming/projectEuler/files/'
    matrix = get_matrix_from_file(path + 'matrix.txt')
    # matrix = get_matrix_from_file(path + 'matrix_example.txt')

    N = len(matrix)

    potential_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            potential_matrix[i][j] = compute_sub_matrix_min(matrix, N, i, j, potential_matrix)

    # for row in potential_matrix:
    #     print row

    print "Minimum path: {}".format(potential_matrix[0][0])

if __name__ == '__main__':
    main()