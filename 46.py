'''
Project Euler Question #46
'''

def isPrime(n):
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    primes.append(n)
    return True

def Goldbach(n):
    if n in GoldbachNums:
        return True
    for p in primes:
        i = 1
        while (p + 2 * i * i <= n):
            if p + 2 * i * i == n:
                return True
            if (p + 2 * i * i) not in GoldbachNums:
                GoldbachNums.append(p+2*i*i)
            i += 1
    return False

primes = [2,3]
GoldbachNums = []
n = 3

while True:
    if not isPrime(n):
        if not Goldbach(n):
            print('Exception Found:', n)
            break
#        else:
#            print('Goldbach:', n)
#    else:
#        print('Prime:', n)
    n += 2
