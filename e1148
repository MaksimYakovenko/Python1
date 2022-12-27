def gcd(a, b):
	while a*b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b

def lcm(a, b):
	m = a * b
	return m // gcd(a,b)

n = int(input())
for i in range(n):
	a, b = map(int, input().split())
	if a == gcd(a,b) and b == lcm(a, b):
		print(a, b)
	else:
		print(-1)
