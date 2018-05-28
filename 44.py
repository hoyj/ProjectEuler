from math import sqrt
def pen(n):
    return n * (3*n - 1) // 2

def isPentagonal(x):
    i = (sqrt(24 * x + 1) + 1) // 6
    return (sqrt(24 * x + 1) + 1) / 6 == i

i = 1
pList = [] # list containing p that have already been calculated
while True:
    p = pen(i)
    for q in pList[::-1]:
        if isPentagonal(abs(p-q)) and isPentagonal(abs(p+q)):
            # found pentagonal condition
            print('Min:',abs(p-q))
            exit(0)
    pList.append(p)
    i += 1
