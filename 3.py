'''
Project Euler Problem #3
According to the Fundamental Theorem of Arithmetic, every integer greater than 1 either is a prime number itself or can be represented as the product of prime numbers except for the order of the factors.
Find the greatest prime number in the unique prime factorization of 600851475143
'''

# Approach: First use primality test(trial division). If it is not divisible by prime numbers between 2 to sqrt(n), then continue on with test Else, we can stop and state that n is a prime number.

from math import sqrt,floor

def findBiggestPrime(n):
    origN = n
    sqrtN = floor(sqrt(n))
    primes = []
    i = 2
    while i <= n:
        if n % i == 0:
            if i > sqrtN and len(primes) == 0:
                return origN
            primes.append(i)
            while n % i == 0:
                n /= i
        i += 1
    print(primes)
    return primes[-1]

if __name__ == '__main__':
    N = 600851475143
    N2 = 13195
    print(findBiggestPrime(N2))

