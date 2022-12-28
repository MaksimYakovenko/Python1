if int(input())%2==0: print('Ok'); exit()
s=input()
for j in s:
    if s.count(j)%2: print(j); break
