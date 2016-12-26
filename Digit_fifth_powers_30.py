import math

answer = 0

def foo(l):
    lsum = 0

    for x in l:
        lsum += math.pow(int(x), 5)

    return lsum

try:
    for n in xrange(1000000):
        l = list(str(n))

        if foo(l) == n:
            print n
            answer += n
except KeyboardInterrupt:
    print "\n" + str(answer)

print "\n" + str(answer)
