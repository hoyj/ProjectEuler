'''
Project Euler Question #39
'''

a = 1
p = [0] * 1001
for a in range(1, 334):
    b = a
    while True:
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c > 1000: break
        if c == int(c): 
            c = int(c)
            print(a,b,c)
            if (a ** 2 + b ** 2 == c ** 2):
                print(a,b,c)
                p[a+b+c] += 1
        b += 1

most_p = -1
for i in p:
    if i > most_p:
        most_p = i
print(p.index(most_p), most_p)
