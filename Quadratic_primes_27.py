import sys
sys.path.insert(0, "/home/isaac/Desktop/Python")
import isaac
import math

n = 0
x = 0
coefficients = []
lengths = []

try:
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0

            while isaac.is_prime(x) or n == 0:
                x = math.pow(n, 2) + (a * n) + b
                n += 1

            lengths.append(n - 1)
            coefficients.append([a, b])
except KeyboardInterrupt:
    print "\n" + str(a)
    print b
    print
print coefficients[lengths.index(max(lengths))]
print coefficients[lengths.index(max(lengths))][0] * coefficients[lengths.index(max(lengths))][1]
