cur = 1
nxt = 1
total = 0
while cur <= 4000000:
    if cur % 2 == 0:
        total += cur
    cur, nxt = nxt, cur+nxt
print('total:', total) 
