answer = 0
n = 1
jump = 0

while n < 1002001:
    jump += 2

    for x in range(4):
        answer += n
        n += jump

print n
print answer + n
