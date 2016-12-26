import sys
sys.path.insert(0, "/home/isaac/Desktop/Python/")

import isaac

sums = []

try:
    for i in xrange(3, 2540160):
        n = 0

        for s in str(i):
            n += isaac.factorial(int(s))

        if n == i:
            sums.append(i)
except KeyboardInterrupt:
    print "\n" + str(i)

print sum(sums)
