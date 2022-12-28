lst = ["+", "-", "*", "", "/", "//", "%"]
n = input()
n = list(n)
count = 0
for l, k in enumerate(n):
    if k == n[l - 1]:
        if k == "*":
            n[l] = ""
            del n[l - 1]
        elif k == "/":
            n[l] = "//"
            del n[l - 1]

for i in n:
    if i == " ":
        del n[i]

for i in lst:
    for g in n:
        if i == g:
            count += 1
print(count)
