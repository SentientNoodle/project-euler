import time

pandigitals = []
digits = [str(i) for i in range(1, 10)]

start_time = time.time()

try:
    for a in range(1, 10000):
        for b in range(1, 10000):
            if "0" in str(a) + str(b) + str(a * b):
                continue
            elif len(str(a) + str(b) + str(a * b)) != 9:
                continue
            else:
                x = digits[:]

                try:
                    for char in list(str(a) + str(b) + str(a * b)):
                        del x[x.index(char)]
                except ValueError:
                    continue

            pandigitals.append(a * b)
except KeyboardInterrupt:
    print a

end_time = time.time()

print sum(set(pandigitals))
print end_time - start_time
