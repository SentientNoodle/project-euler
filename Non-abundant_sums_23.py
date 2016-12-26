import math
import time

start = time.time()

answer = 0
numList = []
abundant = []
a = [1]

for i in range(12, 28124):
    for n in range(2, int(math.ceil(math.sqrt(i))) + 1):
        if i % n == 0:
            a.append(n)
            a.append(i/n)

    a = set(a)
    a = sum(a)

    if a > i:
        abundant.append(i)

    a = [1]

print "What an abundant list of numbers!"

try:
    numList = range(28124)

    for x in abundant:
        for y in range(abundant.index(x), len(abundant)):
            z = abundant[y]

            if x + z > 28123:
                break

            numList[x + z] = 0

    answer = sum(numList)
except KeyboardInterrupt:
    print sum(numList)

end = time.time()

print "\nFound answer: " + str(answer) + " in " + str(end - start) + " seconds."
