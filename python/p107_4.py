# ROWS = 6
# COLUMNS = 6
# ROWS = 7
# COLUMNS = 7
ROWS = 40
COLUMNS = 40

import random
import math


def is_matrix_connected(matrix):
    # Must be able to do a depth-first search to touch all nodes (or rows)
    # for the graph to be fully connected
    rows_visited = set([0])
    row_stack = []
    for column in range(COLUMNS):
        if matrix[0][column] > 0:
            row_stack.append(column)

    while len(row_stack) > 0:
        row = row_stack.pop()
        if row not in rows_visited:
            rows_visited.add(row)
            for column in range(COLUMNS):
                if matrix[row][column] > 0:
                    row_stack.append(column)

    return len(rows_visited) == ROWS


def is_matrix_connected_old(matrix):
    # Must have at least N-1 connections
    n_connections = 0

    # Each row sum must be non-zero
    for row in matrix:
        row_non_zeroes = 0
        for column in row:
            if column > 0:
                row_non_zeroes += 1
                n_connections += 1
        if row_non_zeroes == 0:
            return False
        elif row_non_zeroes == 1:
            # connection must have at least one other connection
            j = 0
            for column in row:
                if column > 0:
                    j = row.index(column)
                    break
            row_j = matrix[j]
            row_j_non_zeroes = 0
            for column in row_j:
                if column > 0:
                    row_j_non_zeroes += 1
            if row_j_non_zeroes == 1:
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
            if n_rows >= ROWS:
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
    result.reverse()
    return result


def print_matrix(matrix):
    for row in matrix:
        print row


def get_matrix_weight(matrix):
    weight = 0
    for row in matrix:
        for element in row:
            weight += element
    return weight / 2  # double counted


def get_random_element(matrix):
    i = random.randint(0, ROWS-1)
    j = random.randint(0, COLUMNS-1)
    mij = matrix[i][j]
    while mij == 0:
        i = random.randint(0, ROWS-1)
        j = random.randint(0, COLUMNS-1)
        mij = matrix[i][j]
    return mij, i, j


def copy_matrix(matrix):
    a = []
    for i in range(ROWS):
        row = []
        for j in range(COLUMNS):
            row.append(matrix[i][j])
        a.append(row)
    return a


def elements_connected(elements):
    if not len(elements) == ROWS-1:
        return False
    row_set = set()
    for element in elements:
        row_set.add(element[1])
        row_set.add(element[2])
    if len(row_set) == ROWS:
        return True
    return False


def compute_elements_weight(elements):
    w = 0
    for element in elements:
        w += element[0]
    return w


def main():
    # matrix = get_matrix('/Users/alange/programming/projectEuler/files/network_example.txt')
    matrix = get_matrix('/Users/alange/programming/projectEuler/files/network.txt')
    sorted_elements = make_sorted_list(matrix)
    full_weight = get_matrix_weight(matrix)

    # print_matrix(matrix)

    elements_kept = []
    for element in sorted_elements:
        elements_kept.append(element)

    # Randomize sorted elements?
    #random.shuffle(sorted_elements)

    # Starting from largest, remove elements as long as it's a valid removal
    for element in sorted_elements:
        elements_kept.remove(element)
        if not is_matrix_connected(build_matrix_from_elements(elements_kept)):
            elements_kept.append(element)

    best_weight = compute_elements_weight(elements_kept)

    print "Connected: ", is_matrix_connected(build_matrix_from_elements(elements_kept))

    print "Full weight: ", full_weight
    print "best weight: ", best_weight
    print "Saved weight: ", full_weight - best_weight


if __name__ == '__main__':
    main()