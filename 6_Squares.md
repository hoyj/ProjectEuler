# Sum of squares of numbers from 1 through n

We already know that the sum of numbers from 1 through n is n(n+1)/2  

We will use -  
1. x(x+1)/2
2. (x+1)^3 - x^3

Expanding 2) we get the following-  
(x+1)^3 - x^3 = x^3 + 3x^2 + 3x + 1 = 3x^2 + 3x + 1  

Inserting numbers 1 through n we get the following equations-  
(2^3) - 1^3 = 3(1^2) + 3(1) + 1  
(3^3) - 2^3 = 3(2^2) + 3(2) + 1  
...  
(n^3) - (n-1)^3 = 3(n-1)^2 + 3(n-1) + 1  
(n+1)^3 - n^3 = 3(n)^2 + 3(n) + 1  

Adding the equations above,  
(n+1)^3 - 1^3 = 3(**1^2 + 2^2 + 3^2 + ... + n^2**) + 3(**1+2+3+...+n**) + 1  

After inserting n(n+1)/2 for (1+2+3+..+n)  
(n+1)^3 - 1^3 = 3(1^2 + 2^2 + 3^2 + ... + n^2) + 3(n(n+1)/2) + 1  

Then we can reach the following  
1^2 + 2^2 + 3^2 + ... + n^2 = **n(n+1)(2n+1)/6**  
