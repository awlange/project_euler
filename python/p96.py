import time


class Grid:
    def __init__(self, name):
        self.grid = []
        self.name = name
        self.fixed = []  # list of (i, j) tuples that are fixed values for the grid
        self.available = []

    def __str__(self):
        s = self.name + "\n"
        for i in range(len(self.grid)):
            s += "".join([str(n) for n in self.grid[i]]) + "\n"
        return s[:-1]

    def add_row(self, row):
        self.grid.append(row)

    def set_fixed(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] > 0:
                    self.fixed.append((i, j))

    def verify(self):
        # rows
        for row in self.grid:
            if not self.verify_list(row):
                # print 'bad row', row
                return False

        # columns
        for j in range(9):
            column = [self.grid[i][j] for i in range(9)]
            if not self.verify_list(column):
                # print 'bad column', column
                return False

        # boxes
        for b in range(9):
            box = []
            row_offset = (b / 3) * 3
            col_offset = (b % 3) * 3
            for i in range(3):
                for j in range(3):
                    box.append(self.grid[row_offset + i][col_offset + j])
            if not self.verify_list(box):
                # print 'bad box', box
                return False

        return True

    def verify2(self):
        """
        Assume row and columns are okay, just check box
        """
        # boxes
        for b in range(9):
            box = []
            row_offset = (b / 3) * 3
            col_offset = (b % 3) * 3
            for i in range(3):
                for j in range(3):
                    box.append(self.grid[row_offset + i][col_offset + j])
            if not self.verify_list(box):
                # print 'bad box', box
                return False

        return True

    def verify_list(self, input_list):
        """
        Return false if [1-9] appears more than once in the list. Zero can appear any number of times.
        """
        counts = [0 for _ in range(0, 10)]
        for n in input_list:
            counts[n] += 1
        for c in counts[1:]:
            if c > 1:
                return False
        return True

    def top_three(self):
        return int("".join([str(i) for i in self.grid[0][:3]]))

    @staticmethod
    def next_element(ic, jc):
        # Move the index to the next element
        jc += 1
        if jc > 8:
            jc = 0
            ic += 1
        return ic, jc

    @staticmethod
    def prev_element(ic, jc):
        # Move the index to the previous element
        jc -= 1
        if jc < 0:
            jc = 8
            ic -= 1
        return ic, jc

    def get_available(self, ic, jc):
        # for the given element, return a list of available values based on
        # the current state of the grid. Also, require that available is
        # greater than the current value
        val = self.grid[ic][jc]
        row = set(self.grid[ic])
        col = set([self.grid[i][jc] for i in range(9)])
        taken_vals = row.union(col)
        available = []
        for a in range(val + 1, 10):
            if a not in taken_vals:
                available.append(a)

        return available
        # box might be too much effort
        # box = []
        # row_offset = (ic % 3) * 3
        # col_offset = (jc / 3) * 3
        # for i in range(3):
        #     for j in range(3):
        #         box.append(self.grid[row_offset + i][col_offset + j])

    def solve(self):
        """
        Solve sudoku
        """
        i = 0
        j = 0
        max_iter = 3
        itr = 0
        solved = False

        # while not solved and itr < max_iter:
        while not solved:
            while (i, j) in self.fixed:
                i, j = self.next_element(i, j)

            while not solved:
                # itr += 1
                if i > 8 or j > 8:
                    # Then we solved it!
                    solved = True
                    break

                # Raise the current element
                self.grid[i][j] += 1

                # if itr > 0:
                #     print itr, i, j
                #     print self.__str__()

                if self.grid[i][j] > 9:
                    # Backtrack
                    self.grid[i][j] = 0
                    i, j = self.prev_element(i, j)
                    while (i, j) in self.fixed:
                        i, j = self.prev_element(i, j)
                elif self.verify():
                    # Move forward
                    i, j = self.next_element(i, j)
                    break

    def solve2(self):
        """
        Solve sudoku, use the available list
        """
        i = 0
        j = 0
        max_iter = 100
        itr = 0
        solved = False

        while not solved:
        # while not solved and itr < max_iter:
            while (i, j) in self.fixed:
                i, j = self.next_element(i, j)

            while not solved:
            # while not solved and itr < max_iter:
            #     itr += 1
                if i > 8 or j > 8:
                    # Then we solved it!
                    solved = True
                    break

                self.available = self.get_available(i, j)
                # print i, j, self.available

                if len(self.available) == 0:
                    # Backtrack
                    self.grid[i][j] = 0
                    i, j = self.prev_element(i, j)
                    while (i, j) in self.fixed:
                        i, j = self.prev_element(i, j)
                    continue

                # Get next available
                self.grid[i][j] = self.available.pop(0)
                # print self.__str__()

                if self.verify2():
                    # Move forward
                    i, j = self.next_element(i, j)
                    while (i, j) in self.fixed:
                        i, j = self.next_element(i, j)


def readGrids():
    grids = []
    grid = None

    # with open('../file/tmp.txt', 'r') as f:
    with open('../file/p096_sudoku.txt', 'r') as f:
        for unstripped_line in f:
            line = unstripped_line.strip("\n")
            if line.split()[0] == 'Grid':
                if grid:
                    grid.set_fixed()
                    grids.append(grid)
                grid = Grid(line)
            else:
                grid.add_row([int(s) for s in line])
        grid.set_fixed()
        grids.append(grid)

    return grids


def main():
    start = time.time()

    total = 0
    for grid in readGrids():
        grid.solve2()
        print str(grid)
        total += grid.top_three()

    print "The answer: ", total
    print "Time: %s" % (time.time() - start)

if __name__ == '__main__':
    main()