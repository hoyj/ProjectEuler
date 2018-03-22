'''
Project Euler Problem #10

What is the sum of prime numbers below 2,000,000?
'''

def isPrime(n):
    if n == 1:
        return False
    elif n in [2, 3]:
        return True
    for d in range(2, int(pow(n, 1/2)) + 1):
        if n % d == 0:
            return False
    return True

def prime_number_generator():
    n = 3
    yield 2
    yield 3
    while True:
        n += 2
        if isPrime(n):
            yield n

def primalityTest(n):
    prime_sum = 0
    p_now = 0
    gen = prime_number_generator()

    while p_now <= n:
        prime_sum += p_now
        p_now = next(gen)

    print(prime_sum)

def sieveTest(n):
    arr = [i for i in range(3, n+1, 2)]
    primes = [2]
    while len(arr) > 0:
        print(len(arr))
        p = arr.pop(0)
        primes.append(p)
        arr = [n for n in arr if n % p != 0]
    print(sum(primes))
    # CODE REVIEW
    # arr = [n for n in arr if n % p != 0]
    # creates an array every time. INEFFICIENT
    # Rather, as sieveTest2 is doing, only manipulate a single array.

def sieveTest2(n):
    b, p, ps = [True] * (n+1), 2, []
    for p in range(2, n+1):
        if b[p]:
            ps.append(p)
            for i in range(p, n+1, p):
                b[i] = False
    print(sum(ps))

def sieveTest3(n):
    m = (n-1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i += 1; p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1; p += 2
    print(sum(ps))

def timer(f, n):
    from time import time
    start = time()
    f(n)
    end = time() - start
    print(f, '--- %s seconds ---' % round(end, 2))

if __name__=='__main__':
    N = 2000000
    timer(sieveTest2,N)
    timer(primalityTest, N)
    timer(sieveTest3, N)
