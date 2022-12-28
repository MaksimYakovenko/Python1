x = int(input())
n = int(input())
a = []
for i in range(n):
	c = [int(i) for i in input().split()]
	a.append(c)

tmp = False

for i in range(n):
	for j in range(n):

		if a[j][i] == x:
			print('YES')
			tmp = True
			break
	if tmp:
		tmp = False
	else:
		print('NO')
