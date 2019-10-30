a, b, c = int(input()), int(input()), int(input())

if a > b:
    a, b = b, a
else:
    a, b = a, b
if a > c:
    a, c = c, a
else:
    a, c = a, c
if b > c:
    b, c = c, b

if a <= b <= c:
    print(a, b, c)
else:
    print("NO")
