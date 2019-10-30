n = int(input())


def MinDivisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1
        if i > n ** 0.5:
            return n


print(MinDivisor(n))
