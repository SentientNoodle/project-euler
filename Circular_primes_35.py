import sys
sys.path.insert(0, "/home/isaac/Desktop/Python/")
import isaac
import math

primes = []

def is_prime(n):
    if n < 0:
        n *= -1

    if n < 2 or n == 4:
        return False
    elif n < 6:
        primes.append(n)
        return True

    unbroken = True
    for x in primes:
        if x > int(math.sqrt(n)):
            unbroken = False
            break

        if n % x == 0:
            return False

    if unbroken:
        for x in range(primes[len(primes)-1], int(math.sqrt(n)), 2):
            if n % x == 0:
                return False

    primes.append(n)
    return True

def rotate(n):
    x = list(str(n))
    x.insert(0, x[len(x)-1])
    return int("".join(x[:-1]))

nums = []
answer = 0
for x in range(1000000):
    i = x
    if i not in nums:
        subnums = []
        prime = True

        for f in range(len(str(i))):
            i = rotate(i)
            subnums.append(i)

            if not(is_prime(i)) or str(x)[-1:] == "0":
                prime = False
                break

        if prime:
            print x
            print subnums
            nums += subnums

print "Answer: " + str(len(set(nums)))
