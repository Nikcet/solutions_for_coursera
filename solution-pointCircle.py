x, y, xc, yc, r = float(input()), float(input()), float(input()), \
                  float(input()), float(input())


def isPointInCircle(x, y, xc, yc, r):
    return (x-xc) ** 2 + (y-yc) ** 2 <= r ** 2


if isPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print("NO")
