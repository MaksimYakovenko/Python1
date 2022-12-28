a, b, c= [int(d) for d in input().split()]
if (a==b) and (a==c) and (b==c):
   print ("1")
elif (a==b) or (b==c) or (a==c):
   print("2")
else: 
   print("3")
