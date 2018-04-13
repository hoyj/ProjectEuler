'''
Project Euler Problem #25
'''

def fib(cur, nxt):
    cur, nxt = nxt, cur+nxt
    return (cur,nxt)

cur = 1; nxt = 1; count = 1
while(len(str(cur)) < 1000):
    cur,nxt = fib(cur, nxt);
    count += 1

print("count:", count);


