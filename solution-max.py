n = int(input())
maxN = n

while n > 0:
    if n > maxN:
        maxN = n
    n = int(input())

print(maxN)
