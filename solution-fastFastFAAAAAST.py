def power(a, n):
    if n == 0:
        return 1
    if n == 1 or n == -1:
        return a
    if n <= 0:
        if -n % 2 != 0:
            return power(1 / a, n + 1)
        if -n % 2 == 0:
            return power(1 / (a ** 2), n // 2)
    if n % 2 != 0:
        return a * power(a, n - 1)
    if n % 2 == 0:
        return power(a ** 2, n // 2)


a, n = float(input()), int(input())
print(power(a, n))
