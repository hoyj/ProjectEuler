# Question 2 TIP
###### This method is useful when we are supposed to find the sum of the fibonacci numbers upto n'th fibonacci number.

F: Fibonacci number  
F(n): nth Fibonacci number  
S(n): sum of fibonacci numbers upto nth  

Then,  
F(n+1) = F(n) + F(n-1)  
and with some transformation, it becomes  
F(n-1) = F(n+1) - F(n)

likewise-  
F(n-2) = F(n) - F(n-1)  
F(n-3) = F(n-1) - F(n-2)  
...  
F(1) = F(3) - F(2)  
F(0) = F(2) - F(1)

Adding the equations cancels each n'th fibonacci number-   
F(0) + F(1) + ... + F(n-1) = F(n+1) - F(1)  
Thus,  
S(n-1) = F(n+1) - F(1)  
S(n-1) = F(n+1) - 1

**S(n) = F(n+2) - 1**

This may not be useful for the problem since we do not know the nth fibonacci number below 4,000,000. **However**, this may become useful IF given conditions are met.  
This algorithm is said to only take **O(logN)**


```Python
MAX = 1000

# array for memoization
f = [0] * MAX

# returns n'th Fibonacci number
# using table f[]
def fib(n):
    n = int(n)
    
    # Base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # If fib(n) is already computed
    if f[n] == True:
        return f[n]

    k = (n+1)/2 if (n & 1) else n/2
    
    # Applying above formula [Note value n&1
    # is 1 if n is odd, else 0].
    f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) if (n & 1) else (2 * fib(k-1) + fib(k)) * fib(k)
    return f[n]

# Computes value of first Fibonacci numbers
def calculateSum(n):
    return fib(n+1) - 1

# This code is contributed by 
# Smitha Dinesh Semwal
# ref: https://www.geeksforgeeks.org/sum-fibonacci-numbers/
```
