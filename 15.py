'''
Project Euler Problem #15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''
# for N x N grid X,Y = N+1, N+1
N = 20
X,Y = N+1, N+1

path = [[0 for x in range(X)] for y in range(Y)]
path[0][1], path[1][0] = 1, 1

for y in range(Y):
    for x in range(X):
        if x-1 >= 0: #if there exists path from left
            path[y][x] += path[y][x-1]
        if y-1 >= 0: #if there exists path from above
            path[y][x] += path[y-1][x]

for row in path:
    print(row)
