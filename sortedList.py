# Отсортируйте данный массив, используя встроенную сортировку.

Num = int(input())
N = list(map(int, input().split()))

sortedList = sorted(N)

print(*sortedList)
