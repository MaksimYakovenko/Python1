n1=input().split()
n=int(n1[0])
m=int(n1[1])
a=[]
for i in range(n):
    a1=[]
    k=input().split()
    for j in range(m):
        a1.append(int(k[j]))
    a.append(a1)
c=[]
q=input()
for i in range(n):
    c1=[]
    k1=input().split()
    for j in range(m):
        c1.append(int(k1[j]))
    c.append(c1)
v=0

for i in range(n):
    for j in range(m):
        if c[i][j]==1:
            v+=a[i][j]

print(v)
