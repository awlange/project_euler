"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left
column and finishing in any cell in the right column, and only moving up, down, and right,
is indicated in red and bold; the sum is equal to 994.
"""

# Note: Pretty sure we have to use Dijkstra's algorithm
# Hey, I was able to implement it! Hooray! But it's slow, really slow. Lemmie try and optimize.
# After viewing threads, realized that the queue was the bottleneck. Now, the queue
# doesn't contain everything, only what it needs.


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
INFINITY = 2**32


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

    global_min = None
    for i in range(len(matrix)):
        print i
        distance, previous = dijkstra(matrix, (i, 0))

        min_val = distance[0][-1]
        for d in distance:
            min_val = d[-1] if d[-1] < min_val else min_val

        if not global_min or min_val < global_min:
            global_min = min_val

    print "Minimum path sum: {}".format(global_min)

if __name__ == '__main__':
    main()