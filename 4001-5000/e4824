n = int(input())
def p(n):
    i = 2
    p = []
    while i * i <= n:
        while n % i == 0:
            p.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        p.append(int(n))
    return p


print(sorted(p(n)))
