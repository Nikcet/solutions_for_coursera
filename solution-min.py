unit = int(input())
n = unit
unitMin = 1

if unit > 2:
    while n >= 2:
        if unit % n == 0:
            unitMin = n
        n = n - 1
else:
    unitMin = unit

print(unitMin)
