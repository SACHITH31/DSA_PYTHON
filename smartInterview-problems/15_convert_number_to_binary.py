# convert number to bits
num = int(input())
temp = num
res = ''

while (temp != 0):
  temRem = temp % 2
  temp = temp // 2
  res += str(temRem)
print(res[::-1])
