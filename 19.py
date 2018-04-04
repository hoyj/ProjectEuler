'''
Project Euler Problem #19

Python implementation.
Pretty much the same as c implementation except, uses library.
Note the useful library 'calendar'.
'''
from calendar import weekday

count = 0
for yr in range(1901, 2001):
    for m in range(1, 13):
        if weekday(y, m, 1) == 6:
            count += 1

print(c)
