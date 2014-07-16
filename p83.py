"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
"""

# Going to repurpose Dijkstra's algorithm from p82_2

import sys


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


# Just some big number
INFINITY = sys.maxint


def dijkstra(matrix, start):
    N = len(matrix)
    rN = range(N)
    distance = [[INFINITY for _ in rN] for _ in rN]
    previous = [[None for _ in rN] for _ in rN]

    i = start[0]
    j = start[1]
    distance[i][j] = matrix[i][j]

    q = [(distance[i][j], i, j)]

    while q:
        q.sort()
        u = q.pop(0)
        if u[0] == INFINITY:
            break

        u_d = u[0]
        u_i = u[1]
        u_j = u[2]

        u_neighbors = []
        if u_i + 1 < N:  # down
            u_neighbors.append((distance[u_i+1][u_j], u_i+1, u_j))
        if u_i - 1 >= 0:  # up
            u_neighbors.append((distance[u_i-1][u_j], u_i-1, u_j))
        if u_j + 1 < N:  # right
            u_neighbors.append((distance[u_i][u_j+1], u_i, u_j+1))
        if u_j - 1 >= 0: # left
            u_neighbors.append((distance[u_i][u_j-1], u_i, u_j-1))

        for v in u_neighbors:
            v_i = v[1]
            v_j = v[2]
            alt = u_d + matrix[v_i][v_j]
            if alt < distance[v_i][v_j]:
                distance[v_i][v_j] = alt
                previous[v_i][v_j] = (u_i, u_j)
                q.append((alt, v_i, v_j))

    return distance, previous


def main():
    path = '/Users/alange/programming/projectEuler/files/'
    matrix = get_matrix_from_file(path + 'matrix.txt')
    # matrix = get_matrix_from_file(path + 'matrix_example.txt')
    # matrix = get_matrix_from_file(path + 'matrix_example2.txt')

    distance, previous = dijkstra(matrix, (0, 0))

    print "Minimum path sum: {}".format(distance[-1][-1])

if __name__ == '__main__':
    main()