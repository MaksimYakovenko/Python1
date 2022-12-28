x,y = [float(n) for n in input ().split()]
z = (2*x*y)/(x**2+y**2)**0.5-(x+y-1)**2/(x*y)
print("%.3f"% z)
