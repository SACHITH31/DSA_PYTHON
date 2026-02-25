# Enter your code here. Read input from STDIN. Print output to STDOUT
row, col = list(map(int, input().split()))

elements = []
for i in range(row):
    temp = list(map(int, input().split()))
    elements.append(temp)

tempResult = (row * col) / 2
counter = 0
for i in range(row):
    for j in range(col):
        if (elements[i][j] == 0):
            counter += 1
if (counter > tempResult):
    print('Yes')
else:
    print('No')
