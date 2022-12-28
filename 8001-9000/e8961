n = int(input())
c = [int(i) for i in input().split()]
m = min(c)
s = 0
l = []

for i in range(n): 
    if c[i] == m:
        s = i
        break
print(m, end=' ') 
c.insert(s, c[0])
c.remove(c[s+1])
c.remove(c[0]) 
print(*c)
