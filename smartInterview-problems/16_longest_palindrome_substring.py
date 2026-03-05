# longest palindrome substring
a = 'aabbaacc'
def isPalindrome(myString):
  # print(myString)
  reversedString = myString[::-1]
  if (reversedString == myString):
    return (reversedString)
  else:
    return 0

for i in range(len(a)):
  res = []
  if (i != len(a)-1):
    for j in range(i + 1, len(a)):
      if (a[i] == a[j]):
        tempRes = isPalindrome(a[i:j+1])
        res.append(tempRes)
  if (len(res) > 0):
    print(res)
  else:
    break
