# Decimal representation
[reference](https://eli.thegreenplace.net/2009/02/25/project-euler-problem-26/)  
**NOTE**: the ^ sign does not mean XOR but indicates exponent.  

According to the link above, the decimal representations can be divided into 3 types.  
1. Finite(ex. 1/4 = 0.25): 2^a * 5^b
2. Infinite but has recurring from start(ex. 1/7 = 0.(142857)): co-prime to 10
    - co-prime: if the divisors of a,b are only 1, then the two numbers a,b are co-prime.
3. Infinite but has recurring after some offset(ex. 1/14 = 0.0(714285)): is divisible by 2 or 5 and the remaining number is co-prime to 10

### How to find recurring number of digits and after how many offsets?
[reference](http://mathworld.wolfram.com/DecimalExpansion.html)  

- Any non-regular fraction m/n is periodic, and has a decimal period lambda(n) independent of m, which is at most n-1 digits long.
    - _decimal period_: the number of digits that recur. (ex. 0.(3) has 1 decimal period)
- The number of digits in the repeating portion of the decimal expansion of a rational number can also be found directly from the multiplicative order of its denominator.
    - When a rational number m/n with (m,n) = 1 is expanded, the period begins after _s_ terms and has length _t_, where _s_ and _t_ are the smallest numbers satisfying __10^s = (10^(s+t))mod n__
- ex. if n = 84
    - 10^0 = 1
    - 10^1 = 10
    - __10^2 = 16__
    - 10^3 = -8
    - 10^4 = 4
    - 10^5 = 40
    - 10^6 = -20
    - 10^7 = -32
    - __10^8 = 16__
- Since 10^8's value has already occurred at 10^2, 10^8 = 10^(2+6), where s = 2, t = 6. 1/84 = 0.01(190476)

### Applying the concept to problem #26
Since the problem asks to find the longest recurring cycle,  
1. Consider denominators that has factors co-prime to 10 else skip
2. For those selected, find s,t according to the formula mentioned above
3. Exchange max value whenever new max cycle is found


