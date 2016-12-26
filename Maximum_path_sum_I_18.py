fn = raw_input("File name: ")

f = open("Data/"+fn,"r+")
l = list(f)

triangle = []
for line in l:
    triangle.append((line.strip()).split(" "))

triangle = triangle[::-1]

for row in range(len(triangle)):
    for i in range(len(triangle[row])-1):
        n = max([int(triangle[row][i]), int(triangle[row][i+1])])
        triangle[row+1][i] = int(triangle[row+1][i]) + n

triangle = triangle[::-1]
print triangle[0][0]
