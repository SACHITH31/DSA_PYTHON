# Enter your code here. Read input from STDIN. Print output to STDOUT

row, col = list(map(int, input().split()))

elements = []
result = []
for i in range(row):
    temp = list(map(int, input().split()))
    elements.append(temp)

for i in range(row):
    if (i % 2 == 0):
        for j in range(col):
            result.append(elements[i][j])
    else:
        for j in range(col - 1, -1, -1):
            result.append(elements[i][j])

print(*result)
