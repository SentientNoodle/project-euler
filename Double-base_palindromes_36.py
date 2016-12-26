import math
import sys
sys.path.insert(0, "/home/isaac/Desktop/Python")
import isaac

nums = []
def isPal(n):
    x = str(n)
    y = x[0:int(math.floor(len(x)/2))]
    if len(x)%2==0:
        z = x[int(math.ceil(len(x)/2)):len(x)]
    else:
        z = x[int(math.ceil(len(x)/2)+1):len(x)]
    if y[::-1] == z:
        return True
    else:
        return False

for x in range(1,1000000):
    if isPal(x) and isPal(isaac.toBase(x,2)):
        print x
        nums.append(int(x))

print sum(nums)
