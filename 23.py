'''
Project Euler Problem #23
'''
import math;


def isAbundunt(n):
    if n < 12: return False

    ab_total = 1
    sqrt_n = n**0.5
    for i in range(2, math.ceil(sqrt_n)):
        if n % i == 0:
            ab_total += i + n // i
    if math.floor(sqrt_n) ** 2 == n: ab_total += sqrt_n 
    return ab_total > n

ab_arr = [i for i, x in enumerate(map(isAbundunt,range(28124))) if x]
n_arr = [False] * 28124;
print("len(ab_arr) =", len(ab_arr))

for i in range(len(ab_arr)):
    for j in range(i, len(ab_arr)):
        total = ab_arr[i] + ab_arr[j]
        if total > 28123: break
        n_arr[total] = True

print(sum([i for i, x in enumerate(n_arr) if not x]))

