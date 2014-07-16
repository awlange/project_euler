"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left
column and finishing in any cell in the right column, and only moving up, down, and right,
is indicated in red and bold; the sum is equal to 994.
"""


def copy_matrix(matrix):
    a = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j])
        a.append(row)
    return a


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


def compute_sub_matrix_min(matrix, i, j, potential_matrix, i_min, i_max, j_min, j_max):
    if potential_matrix[i][j]:
        return potential_matrix[i][j]

    up_limit = i == i_min
    down_limit = i == i_max
    right_limit = j == j_max

    up = potential_matrix[i-1][j] if not up_limit else None
    down = potential_matrix[i+1][j] if not down_limit else None
    right = potential_matrix[i][j+1] if not right_limit else None

    if not up and not down and not right:
        return None

    # get min option only if all options covered
    if up_limit:
        if right_limit and down:
            return matrix[i][j] + down
        if right and down:
            return matrix[i][j] + min(right, down)
    if down_limit:
        if right_limit and up:
            return matrix[i][j] + up
        if right and up:
            return matrix[i][j] + min(right, up)
    options = []
    if right:
        options.append(right)
    if up:
        options.append(up)
    if down:
        options.append(down)

    return matrix[i][j] + min(options)


def is_matrix_filled(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j]:
                return False
    return True


def main():
    path = '/Users/alange/programming/projectEuler/files/'
    # matrix = get_matrix_from_file(path + 'matrix.txt')
    # matrix = get_matrix_from_file(path + 'matrix_example.txt')
    matrix = get_matrix_from_file(path + 'matrix_example2.txt')

    N = len(matrix)

    global_min_first_column_element = None

    for end_i in range(3, 4):
        # print end_i

        i_min = end_i
        i_max = end_i
        j_min = N-1
        j_max = N-1

        potential_matrix = [[None for _ in range(N)] for _ in range(N)]
        potential_matrix[end_i][-1] = matrix[end_i][-1]

        while not is_matrix_filled(potential_matrix):
            i_min = i_min - 1 if i_min > 0 else 0
            i_max = i_max + 1 if i_max < N-1 else N-1
            j_min = j_min - 1 if j_min > 0 else 0
            j_max = j_max + 1 if j_max < N-1 else N-1
            for i in range(i_min, i_max+1):
                for j in range(j_min, j_max+1):
                    potential_matrix[i][j] = compute_sub_matrix_min(matrix, i, j, potential_matrix, i_min, i_max, j_min, j_max)

            print "-----------------"
            print i_min, i_max, j_min, j_max
            print "-----------------"
            for row in potential_matrix:
                print row

        # print "-----------------"
        # for row in potential_matrix:
        #     print row

        min_first_column_element = potential_matrix[0][0]
        for i in range(1, N):
            if min_first_column_element > potential_matrix[i][0]:
                min_first_column_element = potential_matrix[i][0]

        print end_i, min_first_column_element

        if not global_min_first_column_element or global_min_first_column_element > min_first_column_element:
            global_min_first_column_element = min_first_column_element

    print global_min_first_column_element




if __name__ == '__main__':
    main()