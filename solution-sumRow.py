n = float(input())
i = 1
j = 0

while i <= n:
    j = j + 1 / (i ** 2)
    i += 1

print('{0:.5f}'.format(j))
