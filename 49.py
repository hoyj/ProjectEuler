MIN = 1001
MAX = 10000

def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

FOUND = 0
for i in range(MIN, MAX, 2):
    if isPrime(i):
        offset = 2
        while offset < 5000:
            j = i + offset
            k = j + offset
            if isPrime(j) and isPrime(k):
                print(i,j,k)
                if sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
                    print('FOUND:', i,j,k)
                    FOUND += 1
                    if FOUND == 2:
                        exit(0)
            offset += 2

