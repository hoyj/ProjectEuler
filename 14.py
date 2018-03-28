'''
Project Euler Problem #14

For a positive integer n, we repeat the following process,

    if n is even: n -> n / 2
    if n is odd:  n -> 3n + 1

ex) n = 13
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Which starting number, under one million, produces the longest chain?
'''
import time

def mySeq():
    '''
    time taken: average 23 seconds
    '''
    MIL = 1000000
    max_seq_count = (0,0) # number, max_seq_count
    for i in range(MIL, 0, -1):
        n = i
        seq_count = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            seq_count += 1
        if seq_count >= max_seq_count[1]:
            max_seq_count = (i, seq_count)
    print(max_seq_count)

LIMIT = 1000000

def otherSeq():
    '''
    code by "icelemon"
    time taken: average 2 seconds
    '''
    collatz_length = [0] * LIMIT
    max_length = [1,1]
    collatz_length[1] = 1

    for i in range(1, LIMIT):
        n, s = i, 0
        TO_ADD = []
        while n > LIMIT - 1 or collatz_length[int(n)] < 1:
            TO_ADD.append(n)
            if n % 2 == 0: n = n/2
            else: n = 3*n + 1
            s += 1

        for j in range(s):
            m = TO_ADD[j]
            if m < LIMIT:
                ''' 
                Explanation of new_length formula
                collatz_length[int(n)]: is the length from n(the known path) to 1
                s - j: is the length to n(the known path) from m
                Thus, to find the total path length from m, we utilize the already known path
                  (collatz_length[int(n)]) and add to length to that n(s-j).
                '''
                new_length = collatz_length[int(n)] + s - j
                collatz_length[int(m)] = new_length
                if new_length > max_length[1]: max_length = [i, new_length]

def timer(f):
    start = time.time()
    f()
    end = time.time() - start
    print(f.__name__, '-- %s seconds--' % round(end, 2))

if __name__ == '__main__':
    timer(mySeq)
    timer(otherSeq)
