def Move2(n, s, f):
   if n > 0:
       tmp = 6 - s - f
       if tmp == 2:
           Move2(n-1, s, f)
           print(n, s ,tmp)
           Move2(n-1, f, s)
           print(n, tmp ,f)
           Move2(n-1, s, f)
       else:
           Move2(n-1, s, tmp)
           print(n, s ,f )
           Move2(n-1, tmp, f)
 
n = int(input())
 
Move2(n, 1, 3)
