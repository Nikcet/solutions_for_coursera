def isPrime(n):
    i = 2
    while i <= n:
        if i > n ** 0.5:
            return True
        if n % i == 0:
            return False
        i += 1


n = int(input())

if isPrime(n):
    print('YES')
else:
    print('NO')
