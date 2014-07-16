ROWS = 7
COLUMNS = 7


def get_matrix(filename):
    matrix = []
    with open(filename) as f:
        for line in f:
            row = line[:-1].split(',')  # drop the new line at the end of the line
            for i in range(len(row)):
                if row[i] == '-':
                    row[i] = 0
                else:
                    row[i] = int(row[i])
            print row
            matrix.append(row)
    return matrix


def get_matrix_weight(matrix):
    weight = 0
    for i in range(ROWS):
        for j in range(i+1, COLUMNS):
            weight += matrix[i][j]
    return weight


def is_matrix_connected(matrix):
    # Must have at least N-1 connections
    n_connections = 0

    # Each row sum must be non-zero
    for row in matrix:
        row_sum = 0
        for column in row:
            if column > 0:
                row_sum += column
                n_connections += 1
        if row_sum == 0:
            return False

    # n_connections were double counted, so divide by 2
    if n_connections / 2 < ROWS - 1:
        return False

    return True


def get_max_element_less_than_val(matrix, val=1000):
    max_i = 0
    max_j = 0
    max_val = 0
    for i in range(ROWS):
        for j in range(COLUMNS):
            mij = matrix[i][j]
            if max_val < mij < val:
                max_i = i
                max_j = j
                max_val = mij
    return max_i, max_j, max_val


def minimize_matrix(full_mat):
    mat = full_mat

    for i in range(ROWS):
        while 1:
            max_element_in_row = max(mat[i])
            j = mat[i].index(max_element_in_row)

            mat[i][j] = 0
            mat[j][i] = 0
            if is_matrix_connected(mat):
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                for row in mat:
                    print row
                continue

            mat[i][j] = max_element_in_row
            mat[j][i] = max_element_in_row
            break

    return mat


def main():
    matrix = get_matrix('/Users/alange/programming/projectEuler/files/network_example.txt')
    # print get_matrix_weight(matrix)
    min_mat = minimize_matrix(matrix)

    print "---------------"
    print "Min matrix result"
    print "---------------"
    for row in min_mat:
        print row
    print "weight:", get_matrix_weight(min_mat)

    #solution_matrix = get_matrix('/Users/alange/programming/projectEuler/files/network_solution.txt')
    #print get_matrix_weight(solution_matrix)


if __name__ == '__main__':
    main()


# [ 0, 16, 12,  0,  0,  0,  0]
# [16,  0,  0, 17,  0,  0,  0]
# [12,  0,  0,  0,  0,  0,  0]
# [ 0, 17,  0,  0, 18, 19,  0]
# [ 0,  0,  0, 18,  0,  0, 11]
# [ 0,  0,  0, 19,  0,  0,  0]
# [ 0,  0,  0,  0, 11,  0,  0]