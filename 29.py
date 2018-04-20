'''
Project Euler Problem #29

Count all occurences of pow(a,b) where 2<=a<=100 and 2<=b<=100.
Overlapping numbers are not counted again.
ex) 2^4 == 4^2 are considered equal and thus counts as 1
'''

base = range(2,101)
exp = range(2,101)

res = set()

for b in base:
    for e in exp:
        res.add(b**e)

print(len(res))
