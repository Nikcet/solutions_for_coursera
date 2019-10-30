x = int(input())
y = int(input())
i = 1

while x <= y:
    if x == y:
        i = i
    else:
        i = i + 1
    x = (x * 0.1) + x

print(i)
