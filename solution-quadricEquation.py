from math import sqrt
a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif D == 0:
    x = -b / (2 * a)
    print(x)
