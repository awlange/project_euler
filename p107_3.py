ROWS = 6
COLUMNS = 6
# ROWS = 40
# COLUMNS = 40
MAX_TRIES = 10

import random
import math


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


def main():
    # matrix = get_matrix('/Users/alange/programming/projectEuler/files/network_example.txt')
    matrix = get_matrix('/Users/alange/programming/projectEuler/files/network.txt')
    sorted_elements = make_sorted_list(matrix)
    full_weight = get_matrix_weight(matrix)

    # ------- Form initial guess based on sorted elements ---------- #
    weight = 0
    rows_kept = [0]  # just to prevent being added below
    elements_kept = []
    for element in sorted_elements:
        if element[1] not in rows_kept:
            rows_kept.append(element[1])
            elements_kept.append(element)
            weight += element[0]
        elif element[2] not in rows_kept:
            # consider the transpose
            rows_kept.append(element[2])
            elements_kept.append(element)
            weight += element[0]

        if len(rows_kept) == ROWS:
            print "banana", len(rows_kept)
            break

    rows_kept.sort()
    #print rows_kept, len(rows_kept)

    print "Full weight: ", full_weight
    print "Guess weight: ", weight
    print "Saved weight: ", full_weight - weight

    # --- Monte Carlo minimization --- #
    best_matrix = build_matrix_from_elements(elements_kept)
    # best_matrix = get_matrix('/Users/alange/programming/projectEuler/files/network_best2.txt')
    best_weight = get_matrix_weight(best_matrix)
    current_matrix = copy_matrix(best_matrix)
    current_weight = get_matrix_weight(current_matrix)
    # print_matrix(current_matrix)
    # print ""

    denom = 10.0
    for n_iteration in range(100 + 1):

        denom *= 0.99999

        # 1. Randomly select a non-zero element from current_matrix and another from matrix
        # 2. Attempt swap:
        #   2a. If swap causes disconnect, reject.
        #   2b. If swap reduces weight, accept.
        #   2c. Else if swap increases weight, accept within Boltzmann prob
        # 3. Update tmp_matrix and best_matrix if necessary

        current_element = get_random_element(current_matrix)
        matrix_element = get_random_element(matrix)
        tmp_matrix = copy_matrix(current_matrix)
        tmp_matrix[current_element[1]][current_element[2]] = 0
        tmp_matrix[current_element[2]][current_element[1]] = 0
        tmp_matrix[matrix_element[1]][matrix_element[2]] = matrix_element[0]
        tmp_matrix[matrix_element[2]][matrix_element[1]] = matrix_element[0]

        n_tries = 1
        while not is_matrix_connected(tmp_matrix) and n_tries < MAX_TRIES:
            tmp_matrix[current_element[1]][current_element[2]] = current_element[0]
            tmp_matrix[current_element[2]][current_element[1]] = current_element[0]
            tmp_matrix[matrix_element[1]][matrix_element[2]] = 0
            tmp_matrix[matrix_element[2]][matrix_element[1]] = 0
            current_element = get_random_element(current_matrix)
            matrix_element = get_random_element(matrix)
            tmp_matrix[current_element[1]][current_element[2]] = 0
            tmp_matrix[current_element[2]][current_element[1]] = 0
            tmp_matrix[matrix_element[1]][matrix_element[2]] = matrix_element[0]
            tmp_matrix[matrix_element[2]][matrix_element[1]] = matrix_element[0]
            n_tries += 1

        if n_tries >= MAX_TRIES:
            print "continuing..."
            current_matrix[current_element[1]][current_element[2]] = current_element[0]
            current_matrix[current_element[2]][current_element[1]] = current_element[0]
            current_matrix[matrix_element[1]][matrix_element[2]] = 0
            current_matrix[matrix_element[2]][matrix_element[1]] = 0
            continue

        accept = False
        tmp_weight = get_matrix_weight(tmp_matrix)
        # print "------------", current_element, matrix_element
        # print_matrix(tmp_matrix)

        delta = tmp_weight - current_weight
        if denom < 1.0:
            break  # End when denom is small
        elif math.exp(-float(delta) / denom) > random.random():
            accept = True

        if accept:
            current_matrix = copy_matrix(tmp_matrix)
            current_weight = tmp_weight

            if current_weight < best_weight:
                best_matrix = current_matrix
                best_weight = current_weight
        else:
            current_matrix[current_element[1]][current_element[2]] = current_element[0]
            current_matrix[current_element[2]][current_element[1]] = current_element[0]
            current_matrix[matrix_element[1]][matrix_element[2]] = 0
            current_matrix[matrix_element[2]][matrix_element[1]] = 0

        if n_iteration % 100 == 0:
            print "Iteration {}: best: {} current: {} tmp: {} accept: {} denom: {}".format(
                n_iteration, best_weight, current_weight, tmp_weight, accept, denom)


    #print_matrix(best_matrix)
    # Write best to disk for reading in later
    with open('/Users/alange/programming/projectEuler/files/network_best.txt', 'w') as f:
        for row in best_matrix:
            for j in range(COLUMNS):
                f.write("{}".format(row[j]))
                if j < len(row) - 1:
                    f.write(",")
            f.write("\n")
    f.close()

    print "Full weight: ", full_weight
    print "Min weight: ", best_weight
    print "Saved weight: ", full_weight - best_weight


if __name__ == '__main__':
    main()