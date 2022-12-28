n = int(input())
for i in range(n):
	k = int(input())
	mass = [0] * 1001
	for j in range(k):
		tmp = int(input())
		mass[tmp] += 1
	print(mass.index(max(mass)))
