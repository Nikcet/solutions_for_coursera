x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
z1 = 0
z2 = 0

if x1 > 0 and y1 > 0:
    z1 = 1
elif x1 > 0 > y1:
    z1 = 2
elif x1 < 0 and y1 < 0:
    z1 = 3
elif x1 < 0 < y1:
    z1 = 4

if x2 > 0 and y2 > 0:
    z2 = 1
elif x2 > 0 > y2:
    z2 = 2
elif x2 < 0 and y2 < 0:
    z2 = 3
elif x2 < 0 < y2:
    z2 = 4

if z2 == z1:
    print("YES")
else:
    print("NO")
