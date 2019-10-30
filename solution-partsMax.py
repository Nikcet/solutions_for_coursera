n = int(input())
iMax = 0
i = 0
while n != 0:
    if iMax < n:
        iMax = n
        i = 1
    elif iMax == n:
        i += 1

    n = int(input())

print(i)
