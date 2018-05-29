'''
Project Euler Question 45

every odd number is a member of Hn
T1 = H1
T3 = H2
T5 = H3
...
so we only need to find Tn that is equal to Pn

'''

from math import sqrt

n = 287
while True:
    Tn = n * (n+1) / 2
    x = (1 + sqrt(1 + 24 * Tn)) / 6
    if x == int(x):
        print('T{} = P{} = H{} = {}'.format(n, int(x), int(n/2), int(Tn)))
        break
    n += 2 # check only odds since T(2n+1) == H(n)
