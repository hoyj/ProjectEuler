'''
Project Euler #50
'''

MAX = 1000000

num = [-1] * (MAX + 1)

def sieve(n):
    '''
    runs the number n through the sieve and takes two actions
    1. check if number is prime or not
    2. if prime, check other numbers as composite
    '''
    if num[n] != -1:
        return num[n] == 1
    else:
        i = 3
        while i * i <= n:
            if num[i] == 1 and n / i == 0:
                print('Came here...but this shouldnt occur if logical right?')
                num[n] = 0
                return False
            i += 1
        num[n] = 1
        for i in range(n*2, MAX+1, n):
            num[i] = 0
        return True

# set num array for sieve            
num[0],num[1],num[2] = 0,0,1
for i in range(4, MAX+1, 2):
    num[i] = 0
# run num line through sieve
for i in range(3, MAX+1, 2):
    res = sieve(i)
    #print(i, ':', res)

# extract primes from num array
primes = [i for i in range(len(num)) if num[i] == 1]
#print(primes)
f = []
p_sum = 0
for p in primes:
    p_sum += p
    f.append(p_sum)

window = len(primes)
for i in range(len(f)):
    for j in range(i-1, -1, -1):
        p_sum = f[i] - f[j]
        if p_sum > MAX: break
        if p_sum in primes:
            print('i:', i, 'j:', j, 'sum:', p_sum)
