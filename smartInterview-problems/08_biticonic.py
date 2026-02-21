# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
elements = list(map(int, input().split()))

result = False
for i in range(len(elements)):
    if (not (i == len(elements)-1)):
        checker = elements[i] < elements[i + 1]
        if(checker):
            result = checker
        else:
            result = elements[i] > elements[i + 1]
    else:
        break

if (result):
    print('true')
else:
    print('false')
  
