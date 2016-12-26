import math

terms = set([])

try:
    for a in range(2, 101):
        for b in range(2, 101):
            terms.add(math.pow(a, b))
except KeyboardInterrupt:
    print "\n" + str(a) + "^" + str(b)

print len(terms)
