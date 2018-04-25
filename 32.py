'''
Project Euler Problem #32

Find sum of pandigital numbers

conditions for pandigital numbers
1. no 0 should be in equation
2. has either the format 1 digit x 4 digit = 4 digit or 2 digit x 3 digit = 4 digit
3. each digit is unique
'''
# assume is either 1 or 2 digit number. Thus, check for b and c
def isPandigital(a,b,c): # a,b,c are the number to be tested
    sa,sb,sc = map(str, [a,b,c])
    s = sa+sb+sc
    # test 1) c should not contain '0'
    if '0' in s: return False 
    # test 2) given a is either 1 or 2 digit number, b,c should match format
    if len(sa) == 1 and (len(sb) != 4 or len(sc) != 4):
        return False
    elif len(sa) == 2 and (len(sb) != 3 or len(sc) != 4):
        return False
    else:
    # test 3) each digit should be unique from 1-9 digits
        arr = set()
        for digit in s:
            if int(digit) not in arr:
                arr.add(int(digit))
        if len(arr) != 9:
            return False
        return True

ans = set()

for a in range(1,10):
    for b in range(1111,9877):
        if(isPandigital(a,b,a*b)):
            print("{} x {} = {}".format(a,b,a*b))
            ans.add(a*b)

for a in range(11, 99):
    for b in range(111,988):
        if(isPandigital(a,b,a*b)):
            print("{} x {} = {}".format(a,b,a*b))
            ans.add(a*b)

print(len(ans))
print(ans)
print(sum(ans))
