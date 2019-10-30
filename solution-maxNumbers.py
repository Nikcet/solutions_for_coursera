n = int(input())
i = 1
iMin = 0
iMax = 0
while n != 0:
    if i == n:
        iMin += 1
    else:
        i = n
        if iMax > iMin:
            iMax = iMax
        else:
            iMax = iMin
        iMin = 1
    n = int(input())

if iMax > iMin:
    iMax = iMax
else:
    iMax = iMin

print(iMax)
