a, b, c = [int(d) for d in input().split()]
if a == 0:
    exit()
D = (b*b - 4*a*c)
if D < 0:
    print("No roots")
elif D == 0:
    x = (-b+0)/(2*a)
    if x - int(x) == 0:
        print("One root:",int(x))
    else:
        print("No roots")
else:
    x1 = (-b + D **0.5)/(2*a)
    x2 = (-b - D **0.5)/(2*a)
    if x1 > x2:
        print("Two roots:",int(x2),int(x1))
    else:
        print("Two roots:",int(x1),int(x2))
