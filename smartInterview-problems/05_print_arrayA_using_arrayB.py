# Enter your code here. Read input from STDIN. Print output to STDOUT
first_size = int(input())
first_array = list(map(int, input().split()))

second_size = int(input())
second_array = list(map(int, input().split()))

result = []

for i in range(len(second_array)):
    currentValue = second_array[i]
    if ((currentValue < len(first_array))):
        result.append(first_array[currentValue])
    else:
        result.append(-1)

print(*result)
