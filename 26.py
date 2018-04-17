'''
Project Euler Problem #26
'''

CP = [] #co-prime list
NCP = [0,1] #not co-prime list

def hasCoPrime(n):
    '''
    :param n: integer

    description: check whether the given input n is co-prime to 10 by checking
        the following.
        IF it can be fully divisible by 2 or 5 then it is not co-prime. Else, it is co prime.
    '''
    #use memoization to keep track of the co-primality of numbers
    #print("\nChecking coprimality of {}".format(n))
    if n in CP: #already co-prime
        #print("{} in CP".format(n))
        return True 
    if n in NCP:
        #print("{} in NCP".format(n))
        return False

    if n % 5 == 0:
        if hasCoPrime(n//5):
            CP.append(n)
            return True
        else:
            NCP.append(n)
            return False
    elif n % 2 == 0:
        if hasCoPrime(n//2):
            CP.append(n)
            return True
        else:
            NCP.append(n)
            return False
    else:
        #print("{} is neither divisible by 2 or 5.".format(n))
        CP.append(n)
        return True

def getST(n):
    # the value n assumes that n is coprime. Thus, it MUST have a reoccuring value
    # according to number theory approach

    modList = []
    k = 0
    #print("Working with 1/{}".format(n))
    while(True):
        #print("modList: "+ ','.join(map(str,modList)))
        rem = (10**k) % n
        s = 0
        t = 0
        #print("10^{} % {} = {}".format(k, n, rem))
        # first check if the value exists in the mods
        if rem in modList: # found previous occurence. Calculate s, t
            s = modList.index(rem)
            t = k - s
            #print("Found occurence at {}".format(s))
            return t
        else: # since it's not occurred yet, continue with mod
            modList.append(rem)
        k += 1

def main():
    '''
    1) for the number
    2) check if it has co-prime
    2->no) pass since it will not be recurring
    2->yes) check logs to calculate s and t values
    3) check returned t value with max and replace if value is bigger
    '''
    n = 2
    max_t = 0
    max_n = 0
    while(n <= 1000):
        if hasCoPrime(n):
            t = getST(n)
            #print("1/{} has {} digit cycle.".format(n, t))
            if max_t < t:
                max_n = n
                max_t = t
        n += 1
    print("Max occurence is 1/{}, where {} cycle exist.".format(max_n, max_t))

def test():
    for i in range(21):
        print("hasCoPrime({}) = {}".format(i, hasCoPrime(i)))

main()
