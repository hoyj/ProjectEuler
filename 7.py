'''
Project Euler Problem #7

Find 10,001th prime number.
'''

# Thoughts: tried to change i's increment amount but it didn't show much difference in time.

def findPrime(n):
    primes = [2,3]
    i = 5
    count = 2
    while count < n:
        if not any(map(lambda x: i % x == 0, primes)):
            primes.append(i)
            count += 1
        i += 1
    print('count:', count, 'prime:', primes[-1])

def findPrime2(n):
    primes = [2,3]
    i = 5
    count = 2
    while count < n:
        if not any(map(lambda x: i % x == 0, primes)):
            primes.append(i)
            count += 1
        i += 2
    print('count:', count, 'prime:', primes[-1])

def timer(f, args):
    import time
    start = time.time()
    f(args)
    end = time.time() - start
    print('time taken to run f: %s seconds' % end)

if __name__ == '__main__':
    n = 10001
    timer(findPrime,n)
    timer(findPrime2,n)
