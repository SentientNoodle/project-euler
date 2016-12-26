import time

one = [i for i in range(0, 201)]
two = [i for i in range(0, 201) if i % 2 == 0]
five = [i for i in range(0, 201) if i % 5 == 0]
ten = [i for i in range(0, 201) if i % 10 == 0]
twenty = [i for i in range(0, 201) if i % 20 == 0]
fifty = [i for i in range(0, 201) if i % 50 == 0]
hunnit = [i for i in range(0, 201) if i % 100 == 0]

combinations = 1

start_time = time.time()

try:
    for a in one:
        for b in two:
            count = a + b

            if count > 200:
                break

            for c in five:
                count = a + b + c

                if count > 200:
                    break

                for d in ten:
                    count = a + b + c + d

                    if count > 200:
                        break

                    for e in twenty:
                        count = a + b + c + d + e

                        if count > 200:
                            break

                        for f in fifty:
                            count = a + b + c + d + e + f

                            if count > 200:
                                break

                            for g in hunnit:
                                count = a + b + c + d + e + f + g

                                if count == 200:
                                    combinations += 1
                                elif count > 200:
                                    break
except KeyboardInterrupt:
    print a

end_time = time.time()
 
print combinations
print end_time - start_time
