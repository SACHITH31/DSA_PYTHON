# cook your dish here

testCases = int(input())

def reachWt(weight, totalSum):
    if (weight == 1):
        return totalSum + 20
    elif (weight == 2):
        return totalSum + 30
    elif (weight == 0):
        return totalSum 
    else:
        totalSum += 30
        weight = weight - 2
        return reachWt(weight, totalSum)

for i in range(testCases):
    weight = int(input())
    res = reachWt(weight, 0)
    print(res)