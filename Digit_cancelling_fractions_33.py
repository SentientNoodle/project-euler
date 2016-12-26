def xFunc(n):
    if n == 0:
        return 1
    else:
        return 0

for b in range(11, 100):
    for a in range(10, b):
        if "0" in str(a) or "0" in str(b):
            continue

        if str(a)[0] in str(b):
            if int(str(a)[1]) / float(int(str(b)[xFunc(str(b).index(str(a)[0]))])) == a / float(b):
                print str(a) + "/" + str(b)
        elif str(a)[1] in str(b):
            if int(str(a)[0]) / float(int(str(b)[xFunc(str(b).index(str(a)[1]))])) == a / float(b):
                print str(a) + "/" + str(b)
