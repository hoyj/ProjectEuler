def getDigits(n, exp):
    print(n, exp)
    res = 1
    for _ in range(exp):
        res = (res * n) % (10 ** 10)
    return res

total = 0
for i in range(1,1000):
    total += getDigits(i, i)
print(total % 10000000000)
