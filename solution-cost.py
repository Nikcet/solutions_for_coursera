A = int(input())
B = int(input())
N = int(input())
Ba = 0

if B >= 100:
    Ba = B // 100
    B = B % 100
else:
    B = B % 100

A = A + Ba

totalCostRub = N * A
totalCostKop = N * B

if totalCostKop >= 100:
    totalCostRub = totalCostRub + totalCostKop // 100
    totalCostKop = totalCostKop % 100

print(totalCostRub, totalCostKop)
