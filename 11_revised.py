'''
Project Euler Problem #11

From the 20 x 20 grid, What is the greatest product of four adjacent numbers
in the same direction(up, down, left, right, or diagonally) in the 20x20 grid?
'''
# imports
import operator
from functools import reduce

GRID = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

GRID_SIZE = 20

TEST_GRID = '01 02 03 04 \
01 02 03 04 \
01 02 03 04 \
01 02 03 04'

class Grid(object):
    '''
    n x n grid object
    '''
    def __init__(self, s, size):
        '''
        input:
            s, str - str of grid values divided by space
            size, int - size of the grid
        desc: initializes grid
        '''
        self.size = size
        split_s = s.split()
        self.grid = [split_s[i * size:(i+1) * size] for i in range(size)]

### other ###
    def getSubGrid(self, n):
        '''
        input: n, int size of sub grid
        desc: units of subgrid 
        '''
        points = []
        for row in range(self.size - n + 1):
            for col in range(self.size - n + 1):
                points.append((row, col))
    
        grids = []
        for r,c in points:
            grid = [[self.grid[r+rOffset][c+cOffset] for cOffset in range(n)] for rOffset in range(n)]
            grids.append(self.toString(grid))
        return grids        

### calc methods ###
    def calcHorizontal(self):
        '''
        input: None
        desc: calculate all multiplications of horizontal values in grid,
            and return the values in list
        '''
        return [reduce(operator.mul, map(int, row)) for row in self.grid]

    def calcVertical(self):
        '''
        input: None
        desc: ref to calcHorizontal desc. vertical.
        '''
        return [reduce(operator.mul, map(int, [self.grid[row][col] for row in range(self.size)])) for col in range(self.size)]

    def calcDiagonal(self):
        return [reduce(operator.mul, map(int, [self.grid[i][i] for i in range(self.size)])), reduce(operator.mul, map(int, [self.grid[i][self.size-i-1] for i in range(self.size)]))]

    def findMax(self):
        '''
        input: None
        desc: returns max from all possible mults
        '''
        return max(self.calcHorizontal() + self.calcVertical() + self.calcDiagonal())

## Helper methods
    def toGrid(self, s):
        '''
        input: s, str - str of grid values divided by space
        desc: returns 2D list of given grid values
        '''
        split_s = s.split()
        return [split_s[i * size:(i+1) * size] for i in range(self.size)]

    def toString(self, g):
        '''
        input: g, Grid
        output: string
        '''
        return ' '.join([' '.join(map(str, row)) for row in g])

    def getSize(self):
        return self.size

    def setSize(self, newSize):
        self.size = newSize

    def getGrid(self):
        return self.grid

    def setGrid(self, s):
        '''
        input:
            s, str - new str of grid values divided by spaces
        '''
        self.grid = self.toGrid(s)

    def __str__(self):
        s = ''
        for row in self.grid: s += ' '.join(row) + '\n'
        s += '\n'
        return s

if __name__=='__main__':
    g = Grid(TEST_GRID, 4)
    assert g.getSize() == 4, 'size is not properly set'
    print(g)
    
    assert g.calcHorizontal() == [24, 24, 24, 24], '[calcHorizontal Test] Error'
    assert g.calcVertical() == [1, 16, 81, 256], '[calcVertical Test] Error'
    assert g.calcDiagonal() == [24, 24], '[calcDiagonal Test] Error'
    print(g.findMax())
    print(g.getSubGrid(2))
    
    g = Grid(GRID, 20)
    print(g)
    t = g.getSubGrid(4)
    temp = []
    for sg in t:
        temp.append(Grid(sg, 4).findMax())
    print(max(temp))

