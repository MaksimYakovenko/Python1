n=int(input())
a = [int(x) for x in input().split()]
a.reverse()
for i in range(n-1,0,-1):
    if a.count(a[i])>1:
        k=a.index(a[i])
        k1=a.pop(k)
a.reverse()
for i in range(len(a)):
    print(a[i],end=' ')
