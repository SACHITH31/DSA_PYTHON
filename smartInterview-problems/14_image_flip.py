# Enter your code here. Read input from STDIN. Print output to STDOUT
row, col = list(map(int, input().split()))
elements = []

result = []
for i in range(row):
    temp = list(map(int, input().split()))
    elements.append(temp)

mainResult = []
for i in range(len(elements)):
    temp = list(reversed(elements[i]))
    for j in range(len(temp)):
        if (temp[j] == 0):
            mainResult.append(1)
        else:
            mainResult.append(0)
    print(*mainResult)
    mainResult = []
