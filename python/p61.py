from p32 import all_permutations


def triangle(n):
    return (n*n + n) / 2


def square(n):
    return n*n


def pentagonal(n):
    return (n*(3*n-1)) / 2


def hexagonal(n):
    return (n*(2*n-1))


def heptagonal(n):
    return (n*(5*n-3)) / 2


def octagonal(n):
    return n*(3*n-2)


def halves(n):
    if not (1000 <= n <= 9999):
        print "Fuck!"
    sn = str(n)
    return int(sn[:2]), int(sn[2:])
    # note the the 2nd numbers with a leading zero will end up as a single digit,
    # but that's not a problem because they won't be found in the key sets since the key sets always have 2 digits


class Number:
    def __init__(self, halves, type, n):
        self.halves = halves
        self.type = type
        self.n = n

    def __str__(self):
        return ':'.join([str(self.halves), self.type, str(self.n)])


def build_map(input_list):
    result = dict()
    # for half in input_list:
    #     tmp_list = result.get(half[0])
    #     if tmp_list:
    #         tmp_list.append(half[1])
    #     else:
    #         tmp_list = [half[1]]
    #     result[half[0]] = tmp_list

    for number in input_list:
        tmp_list = result.get(number.halves[0])
        if tmp_list:
            tmp_list.append(number)
        else:
            tmp_list = [number]
        result[number.halves[0]] = tmp_list

    return result


def search(polygons):
    for key, vals0 in polygons[0].iteritems():
        for val0 in vals0:
            if polygons[1].get(val0.halves[1]):
                for val1 in polygons[1].get(val0.halves[1]):
                    if polygons[2].get(val1.halves[1]):
                        for val2 in polygons[2].get(val1.halves[1]):
                            # if val2.halves[1] == key:
                            #     if val0.n != val1.n != val2.n:
                            #         return [val0, val1, val2]
                            if polygons[3].get(val2.halves[1]):
                                for val3 in polygons[3].get(val2.halves[1]):
                                    if polygons[4].get(val3.halves[1]):
                                        for val4 in polygons[4].get(val3.halves[1]):
                                            if polygons[5].get(val4.halves[1]):
                                                for val5 in polygons[5].get(val4.halves[1]):
                                                    if key == val5.halves[1]:
                                                        if val0.n != val1.n != val2.n != val3.n != val4.n != val5.n:
                                                            return [val0, val1, val2, val3, val4, val5]

def main():
    triangle_range = range(45, 141)
    square_range = range(32, 100)
    pentagonal_range = range(26, 82)
    hexagonal_range = range(32, 101)
    heptagonal_range = range(21, 64)
    octagonal_range = range(19, 59)

    triangles = build_map([Number(halves(triangle(n)), 'triangle', n) for n in triangle_range])
    squares = build_map([Number(halves(square(n)), 'square', n) for n in square_range])
    pentagons = build_map([Number(halves(pentagonal(n)), 'pentagon', n) for n in pentagonal_range])
    hexagons = build_map([Number(halves(hexagonal(n)), 'hexagon', n) for n in hexagonal_range])
    heptagons = build_map([Number(halves(heptagonal(n)), 'heptagon', n) for n in heptagonal_range])
    octagons = build_map([Number(halves(octagonal(n)), 'octagon', n) for n in octagonal_range])

    # for t, vals in triangles.iteritems():
    #     print t, [str(val) for val in vals]

    # polygons = [triangles, squares, pentagons]
    polygons = [triangles, squares, pentagons, hexagons, heptagons, octagons]

    for permutation in all_permutations(polygons):
        results = search(permutation)
        if results:
            x = ''
            total = 0
            for number in results:
                x += str(number) + "||"
                total += int(str(number.halves[0]) + str(number.halves[1]))
            print x, total



if __name__ == '__main__':
    main()