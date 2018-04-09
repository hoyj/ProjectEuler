with open("./tmp/names.txt", "r") as f:
    buf = f.read()
    names = sorted(buf.split(','))
    total = 0
    count = 0
    for name in names:
        count += 1
        score = 0
        for c in name[1:-1]:
            letterVal = ord(c) - 64
            score += letterVal
        print("{}, order: {}, score: {}, total: {}".format(name, count, score, total))
        total += score * count
    print(total)
