n=int(input())
c=[]
for i in range(n):
    c1=[]
    a=input().split()
    for j in a:
        c1.append(int(j))
    c.append(c1)
sumMain = 0
sumSecondary = 0
for i in range(n):
    sumMain += c[i][i]
    sumSecondary += c[i][n-i-1]
print(sumMain, sumSecondary)
