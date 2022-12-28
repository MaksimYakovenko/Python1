n = int(input())
def lcm(a, b):
	m = a*b
	while a*b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return m // (a + b)
k = 1
for i in range(2, n+1):
	k = lcm(k, i)
print(k)
