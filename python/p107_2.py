# ROWS = 7
# COLUMNS = 7
ROWS = 40
COLUMNS = 40


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


def get_matrix(filename):
    matrix = []
    n_rows = 0
    with open(filename) as f:
        for line in f:
            row = line[:-1].split(',')  # drop the new line at the end of the line
            for i in range(COLUMNS):
                if row[i] == '-':
                    row[i] = 0
                else:
                    row[i] = int(row[i])
            matrix.append(row[:COLUMNS])
            n_rows += 1
            if n_rows > ROWS:
                break
    return matrix


def build_matrix_from_elements(elements):
    matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
    for element in elements:
        matrix[element[1]][element[2]] = matrix[element[2]][element[1]] = element[0]
    return matrix


def make_sorted_list(matrix):
    result = list()
    for i in range(ROWS):
        for j in range(0, i+1):
            mij = matrix[i][j]
            if mij > 0:
                result.append((mij, i, j))
    result.sort()
    return result


def main():
    # matrix = get_matrix('/Users/alange/programming/projectEuler/files/network_example.txt')
    matrix = get_matrix('/Users/alange/programming/projectEuler/files/network.txt')
    for row in matrix:
        print row

    sorted_elements = make_sorted_list(matrix)

    full_weight = 0
    for element in sorted_elements:
        full_weight += element[0]

    weight = 0
    rows_kept = [0] # just to prevent being added below
    elements_kept = []
    for element in sorted_elements:
        if element[1] not in rows_kept:
            print element
            rows_kept.append(element[1])
            elements_kept.append(element)
            weight += element[0]
        elif element[2] not in rows_kept:
            # consider the transpose
            print element
            rows_kept.append(element[2])
            elements_kept.append(element)
            weight += element[0]

        if len(rows_kept) == ROWS:
            print "banana", len(rows_kept)
            break

    rows_kept.sort()
    print rows_kept, len(rows_kept)


    print "Full weight: ", full_weight
    print "Min weight: ", weight
    print "Saved weight: ", full_weight - weight

    tmp_matrix = build_matrix_from_elements(elements_kept)
    for row in tmp_matrix:
        print row


    i = 0
    while i < ROWS:

        orig_row = matrix[i]

        # Get row's max element
        row_max_element = (0, 0, 0)
        for j in range(COLUMNS):
            if tmp_matrix[i][j] > row_max_element[0]:
                row_max_element = (tmp_matrix[i][j], i, j)

        # Attempt to remove the max element
        for j in range(COLUMNS):
            if tmp_matrix[i][j] == 0 < orig_row[j] < row_max_element[0]:
                # swap elements
                tmp_matrix[i][j] = tmp_matrix[j][i] = orig_row[j]
                tmp_matrix[row_max_element[1]][row_max_element[2]] = 0
                tmp_matrix[row_max_element[2]][row_max_element[1]] = 0

                if is_matrix_connected(tmp_matrix):
                    i = -1  # go back to the first row and start all over
                    break

                # not valid swap, swap back
                tmp_matrix[i][j] = tmp_matrix[j][i] = 0
                tmp_matrix[row_max_element[1]][row_max_element[2]] = orig_row[j]
                tmp_matrix[row_max_element[2]][row_max_element[1]] = orig_row[j]

        i += 1

    weight = 0
    print "Min matrix:"
    for row in tmp_matrix:
        for element in row:
            weight += element
        print row
    weight /= 2  # double counted

    print "Full weight: ", full_weight
    print "Min weight: ", weight
    print "Saved weight: ", full_weight - weight


if __name__ == '__main__':
    main()