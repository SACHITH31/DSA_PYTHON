# Enter your code here. Read input from STDIN. Print output to STDOUT
row, col = list(map(int, input().split()))
elements = []

for i in range(row):
    temp = list(map(int, input().split()))
    elements.append(temp)

result = []

for i in range(col):
    temp = []
    for j in range(row):
        temp.append(elements[j][i])
    result.append(temp)

for i in range(len(result)):
    print(*result[i])
