n = int(input())
r = 0
for i in range(10,100):
    q = i % 10
    w = i // 10
    e = i * n
    if e < 100:
        a = e % 10
        s = e // 10
        if (a + s) == (q + w):
            r += 1
    if e >= 100:
        f = e // 100
        g = e % 10
        h = e % 100 // 10
        if (f + g + h) == (q + w):
            r += 1
print(r)
