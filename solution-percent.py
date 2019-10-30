p, x, y = int(input()), int(input()), int(input())

totalXY = x * 100 + y
x = (x * 100 + y) * (100 + p)
totalX = x // 10000
totalY = (x % 10000) // 100
print(totalX, totalY)
