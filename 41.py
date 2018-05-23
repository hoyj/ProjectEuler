'''
1 ~ n

pandigital then check for primality?
or
primality first then pandigital?

max range is 987654321
'''
import time
import sys

MAX = 987654321 
primes = [-1] * (MAX+1)

def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f+2) == 0: return False
        f += 6
    return True

def isPandigital(n):
    return ''.join(sorted(str(n))) == ''.join([str(i) for i in range(1, len(str(n)) + 1)])
        
def main():
    n = 7654321
    while not(isPandigital(n) and isPrime(n)): n -= 2
    print('Largest pandigital prime is', n)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
