'''
Project Euler Problem #36

Find number below 1,000,000 inclusive that is a palindrome in base 10 and base 2.
'''

def toBinary(n):
    if n == 0 or n == 1:
        return str(n);
    return toBinary(n//2) + str(n%2)

def isPalindrome(s):
    s_len = len(s)
    mid = s_len // 2 # if odd don't forget to start the next half + 1
    left = s[:mid]
    right = s[mid:] if s_len % 2 == 0 else s[mid+1:]
    return left == right[::-1]

ans = []
for i in range(1,1000001,2): 
    # skip by 2 because ending in 0 means first digit is 0, which cannot form a palindrome
    b = toBinary(i) # string format. Notice i is int format
    if isPalindrome(str(i)) and isPalindrome(b):
        print(i,':',isPalindrome(str(i)),isPalindrome(b))
        ans.append(i)
print(sum(ans))
