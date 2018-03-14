'''
Project Euler Problem #4_different answer. This compares my answer to ones by others. 
My approach was to find the palindromes first and for each palindrome, find whether three digit numbers exists. 
However, considering n**2 times taken every time a palindrome is found, it is better to go through n**2 times ONCE,
and finding the max palindrome from the list.
This was evident, when I ran the two tests, where my solution took more than a minute to run whereas the other solution
took less than a second.

A palindrome is something that is symmetrical. 
For example, 9009 is a palindrome.
Find the biggest palindrome number from multiplication of two three digit integers.
'''
import time

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

def test1():
    maxPalindrome = 998001
    minPalindrome = 10000

    palindromes = []
    for n in range(maxPalindrome, minPalindrome - 1, -1):
        if isPalindrome(str(n)):
            numbers = findNumbers(n)
            if type(numbers) == tuple:
                #print('n:', n, numbers)
                palindromes.append(n)
    print(len(palindromes))

def test2():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(str(i*j)):
                palindromes.append(i*j)
    print(len(palindromes), len(set(palindromes)))

def timer(f):
    start = time.time()
    f()
    end = time.time() - start
    print('time taken:', end)

if __name__=='__main__':
    timer(test1)
    timer(test2)
