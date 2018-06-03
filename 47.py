nums = [[],[]] # contains list of prime factors

def group(lst):
    n = lst[0]
    sub_res = n
    res = []
    for i in range(1,len(lst)):
        if lst[i] == n:
            sub_res *= lst[i]
        else:
            res.append(sub_res)
            n = lst[i]
            sub_res = n
    res.append(sub_res)
    return res

def getPrimeFactors(n):
    if n < len(nums):
        return nums[n]
    else:
        factors = []
        for i in range(len(nums)-1, 1, -1):
            if n % i == 0: #if divisible, then 
                factors = nums[i] + getPrimeFactors(n // i)
                break
        if len(factors) == 0:
            factors.append(n) #if there are no factors, it indicates prime
        nums.append(factors)
        return factors

def getPrimeFactorsSet(n):
    if n < len(nums):
        return nums[n]
    else:
        factors = set()
        for i in range(len(nums)-1, 1, -1):
            if n % i == 0: #if divisible, then 
                factors.update(nums[i])
                factors.update(getPrimeFactors(n // i))
                break
        if len(factors) == 0:
            factors.add(n) #if there are no factors, it indicates prime
        nums.append(factors)
        return factors

n = 2
count = 0
COND = 4
while True:
    if count == COND:
        print(n-COND)
        break
    pf = getPrimeFactorsSet(n)
    if len(pf) == COND:
        count += 1
    else:
        count = 0
    n += 1
    if count > 2:
        print(n, len(pf),'count:',count)

