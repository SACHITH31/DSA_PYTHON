# Enter your code here. Read input from STDIN. Print output to STDOUT
rows, columns = list(map(int, input().split()))
elements = []

for i in range(rows):
    temp = list(map(int, input().split()))
    elements.append(temp)

result = []

for i in range(len(elements)):
    tempResult = []
    temp = 0
    if (i == 0):
        result = elements[i]
        continue
    else:
        for j in range(len(elements[i])):
            result[j] = result[j] + elements[i][j]

for i in range(len(result)):
    print(result[i])
