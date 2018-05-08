
pandigital = '123456789'
max_n = 0
for n in range(9499, 9233, -1):
    s = ''
    i = 1
    while True:
        new_s = s + str(n*i)
        if len(set(new_s)) != len(new_s) and len(new_s) > 9:
            break
        s = new_s
        i += 1
        #print('s:', s)

    if len(s) == 9 and ''.join(sorted(s)) == pandigital:
        print('Found:', s)
        max_n = n
        break

print('Max pandigital:',max_n)
