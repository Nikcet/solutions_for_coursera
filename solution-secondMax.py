n = int(input())
iMax = 0
iMed = 0

while n != 0:
    if iMax < n:
        iMed = iMax
        iMax = n
    elif iMed < n:
        iMed = n
    n = int(input())

print(iMed)
