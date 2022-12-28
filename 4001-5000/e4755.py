m,n,k=int(input()), '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' 'A' 'B' 'C', ''
while m>0:  
   k=n[m%13]+k
   m//=13
print(k)
