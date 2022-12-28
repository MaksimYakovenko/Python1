r= ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
d= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
a, s, n= input(), 0, ''
for j in range (2):
 for i in range (13):
  while a.find(r[i])==0:
    s+=d[i]
    a=a.replace(r[i], '' ,1)
 a=a.replace('+', '')
for i in range (13):
 for j in range (3):
  if s>=d[i]:
             n+=r[i]
             s-=d[i]
print(n)
