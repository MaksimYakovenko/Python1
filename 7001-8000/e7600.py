n = int(input())
# Перший варіант
if n == 1:
    s = 0
    for i in range(100, 1000):
        d1 = i // 100
        d2 = i // 10
        d3 = i % 10
        if  ((d1 % 2 ==0) and (d2 % 2 == 0) and (d3 % 2 == 0)):
            s += i
    print(s)
# Другий варіант
elif n == 2:
    count = 0
    for i in range(100, 1000):
        d1 = i // 100
        d2 = i % 100 // 10
        d3 = i % 10
        if d3 > d2 > d1:
            count += 1
    print(count)
# Третій варіант
elif n == 3:
    s = 0
    for i in range(100, 1000):
        d1 = i // 100
        d2 = i // 10
        d3 = i % 10
        if ((d1 % 2 == 1) and (d2 % 2 == 1) and (d3 % 2 == 1)):
            s += i
    print(s)
# Четвертий варіант
elif n == 4:
    count = 0
    for i in range(100, 1000):
        d1 = i // 100
        d2 = i % 100 // 10
        d3 = i % 10
        if d3 < d2 < d1:
            count += 1
    print(count)
# П'ятий варіант
elif n == 5:
    s = 0
    for i in range(100, 1000):
        d1 = i // 100
        d2 = i % 100 // 10
        d3 = i % 10
        if i == (d1**3 + d2**3 + d3**3):
            s += i
    print(s)
# Шостий варіант
elif n == 6:
    count = 0
    for i in range(100, 1000):
        d1 = i // 100
        d2 = i % 100 // 10
        d3 = i % 10
        if ((d1 != d2) and (d1 != d3) and (d2 != d3)):
            count += 1
    print(count)
