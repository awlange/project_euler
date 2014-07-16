import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.n_ab = None
        self.n_bc = None
        self.n_ca = None

    def dot(self, n, m):
        return n[0]*m[0] + n[1]*m[1]

    def sub(self, m, n):
        return m[0] - n[0], m[1] - n[1]

    def scale(self, a, n):
        return n[0] * a, n[1] * a

    def neg(self, v):
        return -v[0], -v[1]

    def normalize(self, v):
        return self.scale(1.0 / math.sqrt(self.dot(v, v)), v)

    def rotate(self, v):
        theta = 0.5 * math.pi
        x = v[0] * math.cos(theta) - v[1] * math.sin(theta)
        y = v[0] * math.sin(theta) + v[1] * math.cos(theta)
        return x, y

    def sign_check(self, v, w):
        if self.dot(v, w) < 0.0:
            return False
        return True

    def compute_normals(self):
        # Get normal vectors
        self.n_ab = self.rotate(self.normalize(self.sub(self.b, self.a)))
        self.n_bc = self.rotate(self.normalize(self.sub(self.c, self.b)))
        self.n_ca = self.rotate(self.normalize(self.sub(self.a, self.c)))

        # Change sign based on third point
        # We want a positive dot product with the normal to indicate that
        # the point is on the interior of the triangle
        self.n_ab = self.n_ab if self.sign_check(self.n_ab, self.c) else self.neg(self.n_ab)
        self.n_bc = self.n_bc if self.sign_check(self.n_bc, self.a) else self.neg(self.n_bc)
        self.n_ca = self.n_ca if self.sign_check(self.n_ca, self.b) else self.neg(self.n_ca)

    def contains_origin(self):
        if self.sign_check(self.n_ab, self.neg(self.a)) \
                and self.sign_check(self.n_bc, self.neg(self.b)) \
                and self.sign_check(self.n_ca, self.neg(self.c)):
            return True
        return False


def main():
    n_contains = 0
    with open('/Users/alange/programming/projectEuler/files/triangles.txt') as f:
        for line in f:
            coords = [float(x) for x in line.split(',')]
            a = (coords[0], coords[1])
            b = (coords[2], coords[3])
            c = (coords[4], coords[5])
            t = Triangle(a, b, c)
            t.compute_normals()
            if t.contains_origin():
                n_contains += 1

    print n_contains


if __name__ == '__main__':
    main()