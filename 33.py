'''
Project Euler Problem #33
'''

def isValid(n,d):
    ans = []
    for i in range(n,10): #digits to append. Must be greater than or equal to numerator
        num = int(str(n) + str(i))
        den = int(str(i) + str(d))
        if num / den == n / d:
            ans.append((num,den))
    return ans

def gcd(a,b):
    while b:
        a,b = b,a%b
        return a

t_num = 1
t_den = 1
for d in range(1,10):
    for n in range(1,d): # numerator should be less than denominator
        res = isValid(n,d)
        if len(res) == 0:
            #print("None found for {}/{}".format(n,d))
            continue
        else:
            #print("For {}/{}: {}".format(n,d,res))
            t_num *= n
            t_den *= d

g = gcd(t_num, t_den)
print(t_num, '/', t_den)
print(t_num / g, '/', t_den / g)
