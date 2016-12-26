fib1 = 1
fib2 = 2
fibSum = 0

evenFibs = []

while fib2 <= 4000000:
    if fib2 % 2 == 0:
        evenFibs.append(fib2)

    fibSum = fib1 + fib2
    fib1 = fib2
    fib2 = fibSum

print sum(evenFibs)
