n=int(input())
b=[]
for i in range(n):
    q=input().split()
    b.append(q)
q1=input().split()
a=int(q1[0])
a1=int(q1[1])
for i in range(a):
    for j in range(a1):
        print(b[i][j], end=' ')
    print()
