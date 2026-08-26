# cook your dish here

num = int(input())

if (num % 10 == 0):
    print(10)
else:
    tempNum = num // 10
    tempNum = tempNum * 10 + 10
    print(tempNum - num)
