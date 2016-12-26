numbers = [1, 1]
f = 0
index = 2

try:
    while len(str(f)) < 1000:
        f = numbers[index - 1] + numbers[index - 2]
        numbers.append(f)

        index += 1
except KeyboardInterrupt:
    print f

print len(numbers)
