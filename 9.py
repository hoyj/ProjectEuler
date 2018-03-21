'''
Project Euler Problem #9

A pythagorean triplet is a set of three natural numbers, a<b<c, for which,
a^2 + b^2 = c^2

For instance, 3^2 + 4^2 = 5^2.
There exists exactly one Pythagorean triplet for which a+b+c = 1000.
Find the product abc.
'''

# a can be at max 332 for it to satisfy the conditions.

def try1(): # 199374425
    count = 0
    for a in range(1,1001): # if a <= 332, a+1 <= b <= 333
        for b in range(1, 1001):
            for c in range(1, 1001):
                count += 1
                if a < b  and b < c and a+b+c == 1000 and a**2 + b**2 == c**2:
                    print(a,b,c, 'count:', count)
                    return (a,b,c)
    print('error')

def try2():
    '''
    Approach:
    tried to shorten unnecessary loops by assuming max value that a,b,c can reach.
    range of a: a cannot surpass 332. Else, no numbers b,c exist.
    range of b: we find b_max by (1000 -a) // 2 since 1000 - a - b = c indicates
    1000 - a = b + c and for some number X where b <= X & c <= X
    1000 - a = X + X = 2X
    thus, (1000 - a) // 2 = X
    '''
    count = 0
    for a in range(1, 333):
        b_max = (1000 - a) // 2
        if b_max ** 2 == 1000 - a: # if they are equal then it already fails the condition a < b < c
            # Thus shorten b_max by 1
            print('surprised if it came here:', a, b_max)
            b_max -= 1
        for b in range(1, b_max+1):
            count += 1
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a,b,c, 'count:', count)
                return (a,b,c)

if __name__=='__main__':
#    a,b,c = try1()
    a,b,c = try2()
    print(a*b*c)
