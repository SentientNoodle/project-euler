import sys
import time

answer = ""
stringthing = "0123456789"
#char1 = ""
#char2 = ""

def next(a):
#    global char1
#    global char2

    s = list(a)

    char1 = ""
    char2 = ""
    index = 0

    for x in s[:-1][::-1]:
        if int(x) < int(s[s.index(x) + 1]):
            char1 = x
            break

    try:
        for y in s[::-1]:
            if int(y) > int(char1):
                char2 = y
                break
    except:
#        print char1
        pass

    index = s.index(char1) + 1

    s[s.index(char1)] = "R"
    s[s.index(char2)] = char1
    s[s.index("R")] = char2

    return "".join(s[:index]) + "".join(sorted(s[index:]))

start = time.time()
for x in range(1000000):
    answer = stringthing
    stringthing = next(stringthing)
end = time.time()

print answer
print "\nTime: " + str(end-start) + " seconds."
