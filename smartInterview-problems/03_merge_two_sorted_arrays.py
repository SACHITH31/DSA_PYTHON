# Enter your code here. Read input from STDIN. Print output to STDOUT
first_size = int(input())
first_array = list(map(int, input().split()))

second_size = int(input())
second_array = list(map(int, input().split()))

combined_array = list(first_array + second_array)

for i in range(len(combined_array)):
    for j in range(len(combined_array)):
        if(combined_array[i] < combined_array[j]):
            temp = combined_array[i]
            combined_array[i] = combined_array[j]
            combined_array[j] = temp
print(*combined_array)
