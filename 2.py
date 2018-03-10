'''
Project Euler Problem #2
Find the sum of all fibonacci numbers that are below 4,000,000 and even
'''

cur = 1
nxt = 1
total = 0
while cur <= 4000000:
    if cur % 2 == 0:
        total += cur
    cur, nxt = nxt, cur+nxt
print('total:', total) 
