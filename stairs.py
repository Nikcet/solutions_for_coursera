n = int(input())
i = 0

for i in range(1, n + 1):
    print(*range(1, i + 1), sep='')
