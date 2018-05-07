'''
Project Euler Question #37
'''
from math import floor
from time import time

def isPrime(n):
    if n == 1: return False
    elif n in [2,3]: return True
    elif n % 2 == 0: return False
    sqrt_n = floor(n ** 0.5)
    for i in range(2,sqrt_n+1):
        if n % i == 0: #composite
            return False
    return True

def check(p):
#    print("======Check", p, "========")
    n_len = len(str(p))
    left = p // 10
    right = p % (10 ** (n_len - 1))
    n_len -= 1
    while(n_len > 0):
#        print("n_len:", n_len, "Check left:", left, "right:", right)
        if isPrime(left) and isPrime(right):
            left = left // 10
            right = right % (10 ** (n_len - 1))
            n_len -= 1
        else:
            return False
    return True

time_s = time()
res = [2,3,5,7]
ans = []
i = 11
while True:
    if isPrime(i):
        if check(i):
            print(i)
            ans.append(i)
            if len(ans) >= 11:
                break
    i += 2
print('Final:', ans)
print("Sum:", sum(ans))
print("%.4f"%(time() - time_s))
