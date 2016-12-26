foo = []
n = 1
index = 1
r = 0
lengths = []

try:
    for i in range(1, 1000):
        n = 1
        index = 1
        r = 0
        foo = []

        while True:
            if n < i:
                n *= 10
                index *= 10
            elif n % i != 0:
                if [n, i] in foo:
                    lengths.append(len(foo) - foo.index([n, i]))
                    break

                foo.append([n, i])
                n = n % i
            else:
                lengths.append(0)
                break
except KeyboardInterrupt:
    print i

print lengths.index(max(lengths))
print max(lengths)
