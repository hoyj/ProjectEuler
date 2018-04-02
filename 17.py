'''
Project Euler Problem #17

Count the number of characters (not including - or spaces) in the words from
1~1000
'''

WORDS = {
'1': 'one',
'2': 'two',
'3': 'three',
'4': 'four',
'5': 'five',
'6': 'six',
'7': 'seven',
'8': 'eight',
'9': 'nine',
'10': 'ten',
'11': 'eleven',
'12': 'twelve',
'13': 'thirteen',
'19': 'nineteen',
'20': 'twenty', # 21~29 = '20' + '#'
'30': 'thirty', # 31~39 = '30' + '#'
'1000': 'onethousand'
}

# 1 1~13 fixed
# 2 14~19 conditioned
    # if end in 've': ve -> f
    # if end in t, add 'een'
    # else add teen
# 3-1 20, 30 fixed
# 3-2 40~90 conditioned
    # if end in 've': ve -> f
    # if end in t, add 'y'
    # else add 'ty'
# 3 digits
# first digit + 'hundred and ' + last two digit ruled as before
def dictionary_creator(n):
    for i in range(1, n+1):
        if str(i) not in WORDS:
            WORDS[str(i)] = getEnglish(str(i))
    total = 0
    for k,v in WORDS.items():
        total += len(v)
        print('{} : {} , {}'.format(k,v,len(v)))
    print(total)

def getEnglish(s):
    '''
    :param s: string version of int
    returns english word without spaces
    '''
    #1 get digits
        #1 digit = check in dictionary
        #2 digit = check in ditionary, if not, then divide up into 10's and 1's then add.
    n = int(s)
    digits = len(s)

    if digits == 2:
        if s in WORDS:
            return WORDS[s]
        else:
            ones = n % 10
            tens = n - ones
            word = ''
            if tens == 10: # 14~19
                word = WORDS[str(ones)]
                if ones == 5: word = word[:-2] + 'f'
                elif ones == 8: word = word[:-1]
                word += 'teen'
            elif ones == 0:
                tens = n // 10
                word = WORDS[str(tens)]
                if tens == 5: word = word[:-2] + 'f'
                elif tens == 8: word = word[:-1]
                word += 'ty'
            else:
                word = getEnglish(str(tens)) + getEnglish(str(ones))
            WORDS[str(n)] = word
            return word
    elif digits == 3:
        if s in WORDS:
            return WORDS[s]
        else:
            tens = n % 100
            hundreds = n // 100
            word = ''
            if tens == 0:
                word = WORDS[str(hundreds)] + 'hundred'
            else:
                word = WORDS[str(hundreds)] + 'hundredand' + getEnglish(str(tens))
            WORDS[str(n)] = word
            return word
    else:
        return WORDS[s]

if __name__ == '__main__':
    dictionary_creator(1000)
    d = WORDS
    #print(d['288'])
    print('count:', len(d.values()))
    print(sum(map(len, d.values())))
