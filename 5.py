'''
Project Euler Problem #5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Approach
# "Find the least common multiple(lcm)"
# lcm(a,b) = a * b // gcd(a,b)

def gcd(a,b):
    while b:
        a,b = b, a % b
    return a

def lcm(a,b):
    return (a * b) // gcd(a,b)

def test(n):
    for i in range(1,21):
        print(n,'%', i, '=', n%i == 0)

if __name__ == '__main__':
    from functools import reduce
    rng = range(1,21)
    res = reduce(lcm, rng)
    print(test(res)) 
