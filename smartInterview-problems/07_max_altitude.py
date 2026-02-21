# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
elements = list(map(int, input().split()))

max_values = []

for i in range(len(elements)):
    if ((i == 0) or (i == len(elements))):
        max_values.append(elements[i])
    else:
        currentValue = elements[i]
        tempResult = max_values[i - 1] + currentValue
        max_values.append(tempResult)
print(max(max_values))
