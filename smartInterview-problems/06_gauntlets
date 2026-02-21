# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
elements = list(map(int, input().split()))

result = {}

for i in range(len(elements)):
    counter = 1
    for j in range(i + 1, len(elements)):
        if ((elements[i] == elements[j]) and (elements[i] not in result.keys())):
            counter += 1
    if (counter >= 2):
        result[elements[i]] = counter // 2
print(sum(result.values()))
