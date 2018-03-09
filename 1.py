'''
Project Euler Problem #1
Find the sum of all multiples of 3 and multiples of 5 under 1000
'''

N = 999
max3 = N // 3
max5 =  N // 5
max15 = N // 15

a = (max3 * (max3 + 1)) / 2
b = (max5 * (max5 + 1)) / 2
c = (max15 * (max15 + 1)) / 2

print('Result:', 3*a + 5*b - 15*c)


