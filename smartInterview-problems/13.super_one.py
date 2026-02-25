
# Enter your code here. Read input from STDIN. Print output to STDOUT
# on progress only not compeleted yet 
# link: https://hive.smartinterviews.in/contests/smart-interviews-basic/problems/super-one?page=0&pageSize=100
row, col = list(map(int, input().split()))
elements = []
for i in range(row):
    temp = list(map(int, input().split()))
    elements.append(temp)

counter1 = 0
for i in range(1, row - 1):
    counter = 0
    for j in range(1, col - 1):
        if (elements[i][j] == 1):
            for u in range(j - 1, j + 2):
                if (elements[i - 1][u] == 0):
                    counter += 1
            for s in range(j - 1, j + 2):
                if ((s != j) and elements[i][s] == 0):
                    counter += 1
            for d in range(j - 1, j + 2):
                if (elements[i + 1][d] == 0):
                    counter += 1
            if (counter == 8):
                counter1 = counter
                break
if (counter1 == 8):
    print('Yes')
else:
    print('No')
