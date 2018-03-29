'''
Mathematical approach to #15

The number of paths is to arrange 20 '-'s and 20 '|'s.

Thus, 40!/(20!*20!)
'''

from functools import reduce
from operator import mul

print(reduce(mul, range(1, 41))/(reduce(mul, range(1,21))**2))
