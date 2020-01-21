numList = list(map(int, input().split()))

maxNum = max(numList)
minNum = min(numList)

x = numList.index(maxNum)
y = numList.index(minNum)

numList[x], numList[y] = numList[y], numList[x]

print(*numList)
