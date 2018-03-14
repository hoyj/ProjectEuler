'''
Project Euler Problem #4

A palindrome is something that is symmetrical. 
For example, 9009 is a palindrome.
Find the biggest palindrome number from multiplication of two three digit integers.
'''

def isPalindrome(s, mode=1):
    '''
    input: s, string
    output: True, False, boolean
    '''
    # base case
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False

def findNumbers(n):
    '''
    input: n, int
    return tuple of 3 digit numbers or None if none found
    '''
    for i in range(100, 1000):
        for j in range(100, 1000):
            if i * j == n:
                return (i,j)
    return None

maxPalindrome = 998001
minPalindrome = 10000


for n in range(maxPalindrome, minPalindrome - 1, -1):
    if isPalindrome(str(n)):
        numbers = findNumbers(n)
        if type(numbers) == tuple:
            print('n:', n, numbers)
            break

