P = input()

F = {(0, 0):0}

x, y, dx, dy, s = 0, 0, 1, 0, 0

for p in P:
    if p == 'L': dx, dy = dy, -dx
    if p == 'R': dx, dy = -dy, dx
    if p == 'S':
        x, y, s = x+dx, y+dy, s+1
        if F.get((x,y)) is None:
            F[(x,y)] = 0
        else:
            print(s)
            s = -2
            break

if s > -2: print(-1)
