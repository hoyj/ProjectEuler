'''
Project Euler Question 42
'''

def getSum(word):
    total = 0
    for c in word:
        total += ord(c) - 64
    return total

def isTriWord(word_sum):
    if word_sum in tri_num: return True
    else:
        n = 1
        while n * (n+1) / 2 < word_sum:
            n += 1
        if n * (n+1) / 2 == word_sum:
            #print('{} x ({} + 1) / 2 = {}'.format(n, n, word_sum))
            tri_num.append(word_sum)
            return True
        return False

tri_num = []

with open("./tmp/words.txt") as f:
    data = f.read()
    data = [word[1:-1] for word in data.split(',')]
    data.sort()
    count = 0
    for word in data:
        word_sum = getSum(word)
        if isTriWord(word_sum):
            #print('word_sum: {}, word:{}'.format(word_sum, word))
            count += 1
    print('Total of {} tri-words were found.'.format(count))
        
    
