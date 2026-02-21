# Enter your code here. Read input from STDIN. Print output to STDOUT
first_size = int(input())
first_array = list(map(int, input().split()))

second_size = int(input())
second_array = list(map(int, input().split()))

result = []

for i in range(len(first_array)):
    for j in range(len(second_array)):
        if ((first_array[i] == second_array[j]) and (first_array[i] not in result)):
            result.append(first_array[i])

print(*result)
