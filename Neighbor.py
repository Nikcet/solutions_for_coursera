numList = list(map(int, input().split()))

for i in range(1, len(numList), 2):
    numList[i - 1], numList[i] = numList[i], numList[i - 1]

print(*numList)
