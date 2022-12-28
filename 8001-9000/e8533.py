n=input().split()
a=int(n[0])
b=int(n[1])
c=0
d=[]
for i in range(a,b+1):
    k=i
    for j in range(4):
        c=i%10
        i=i//10
        d.append(c)
    if (d[0]==d[1] or d[0]==d[2] or d[0]==d[3]) or d[1]==d[2] or d[1]==d[3] or d[2]==d[3]:
        pass
    else:
        print(k, end=' ')
    d=[]
