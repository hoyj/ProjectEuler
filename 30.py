'''
Project Euler Problem #30

Approach: get all possible combinations of digits and find answer
'''

import itertools

nums = range(10)
#change combination to numbers
def inNum(p, s):
    if len(p) != len(s):
        return False
    st = list(p)
    for c in s:
        if int(c) in st:
            st.remove(int(c))
        else:
            return False
    return True

ans = set()

for i in range(1,7):
    print("i:", i)
    for p in itertools.combinations_with_replacement(nums,i):
        n = sum(map(lambda x: x**5, p))
        if inNum(p, str(n)):
            ans.add(n)
ans.remove(0)
ans.remove(1)
print('result: ', ans)
print('sum:', sum(ans))
