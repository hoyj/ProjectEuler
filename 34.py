'''
Project Euler Problem #34
'''

f = [0] * 10;
f[0] = 1
f[1] = 1
def fac(n):
    if f[n] == 0:
        f[n] = n * fac(n-1)
    return f[n]

def getSum(n):
    tmp_n = n
    tot = 0
    while(tmp_n != 0):
        digit = tmp_n % 10
        tot += fac(digit)
        tmp_n = tmp_n // 10
    return tot

for i in range(10):
    print(str(i) + '!:',fac(i))

ans = []
for i in range(11, 100000):
    if(getSum(i) == i):
        ans.append(i)
        print(i)
print(ans)
print(sum(ans))
