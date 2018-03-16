'''
Project Euler Problem #6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# Approach

def sumOfSquares(n):
    return n * (n+1) * (2 * n + 1) / 6

def squareOfSum(n):
    return (n * (n+1) / 2) ** 2

n = 100
print(squareOfSum(n), '-', sumOfSquares(n), '=', squareOfSum(n)-sumOfSquares(n))
